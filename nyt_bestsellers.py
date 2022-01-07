import json
import requests
from datetime import datetime as dt, timedelta
from dataclasses import dataclass
from time import time
import pandas as pd
from collections import namedtuple
from pprint import PrettyPrinter
from retrieve_api_keys import get_API_keys
from nltk.corpus import stopwords
from string import punctuation

pp = PrettyPrinter(indent=4)



def pre_process_book_data(book):
    # lower case removing punctuation and stopwords
    if book['title']:
        book['title'] = book['title'].lower()
    if book['description']:
        book['description'] = book['description'].lower().\
                        translate(str.maketrans('', '', punctuation))
        book['description'] = ' '.join([w for w in book['description'].split()\
                                if w not in stopwords.words('english')])
    return book



class TimesBestsellers:
    '''
        Class to retrieve the list of New York Times Bestsellers books in any fiction and 
        non-fiction categories from the new millenium
    '''
    def __init__(self):
        self.list_ep = 'https://api.nytimes.com/svc/books/v3/lists'
        self.list_names_ep = 'https://api.nytimes.com/svc/books/v3/lists/names'
        self.headers = {'api-key': get_API_keys()[0], 'list': None, 'published_date': None}    
        self.dt = '%Y-%m-%d'
        self.get_lists()


    def get_lists(self):
        self.list_names = []
        response = requests.get(self.list_names_ep, params=self.headers)
        for result in response.json()['results']:
            cadence, cadence_days = result['updated'], 7 #weekly as default
            if cadence == 'MONTHLY':
                cadence_days = 30
            self.list_names.append({'name': result['list_name_encoded'], 'cadence': cadence_days,
                                    'first': result['oldest_published_date'],
                                    'current': result['newest_published_date']})


    def get_book_list(self):
        # get list of ISBNs for books that have appeared on NYT Bestseller lists
        self.all_books, self.all_isbns = [], []
        for lbl in self.list_names:
            while dt.strptime(lbl['first'], self.dt) < dt.strptime(lbl['current'], self.dt):
                #store params in headers object that will be used to send the API request       
                self.headers['published_date'] = dt.strptime(lbl['current'],self.dt).strftime('%Y-%d-%m')
                self.headers['list'] = lbl['name']
                try:
                    self.access_book_from_API()
                except: 
                    pass
                new_date = dt.strptime(lbl['current'], self.dt) - timedelta(days=lbl['cadence'])
                lbl['current'] = new_date.strftime(self.dt)
        self.store_books_data()


    def access_book_from_API(self):
        response = requests.get(self.list_ep, params=self.headers)
        for book in response.json()['results']:
            txt = book['book_details'][0]
            item = {'genre': response.json()['results'][0]['display_name'],
                    'title': txt['title'], 
                    'author': txt['author'], 
                    'description': txt['description'],
                    'isbn13': txt['primary_isbn13'],
                    'weeks': int(book['weeks_on_list']),
                    'rating': None}
            #we want books that appeared enough times on the list to be captured. One hit wonders, sorry!
            if item['isbn13'] not in self.all_isbns: #and item['weeks'] >= 5:
                    self.all_books.append(item)
                    self.all_isbns.append(item['isbn13'])


    def store_books_data(self):
        for book in self.all_books:
            book = pre_process_book_data(book)
            if book['title'] and book['description'] and book['author'] and book['isbn13']:
                book['target'] = book['title'] + ' ' + book['author'] + ' ' + book['description']
        #alert for number of books added
        m, s = str(int((time() - start)//60)), int((time() - start)%60)
        print('Total books so far:', str(len(self.all_books)), 'now at {}:{:02d}m'.format(m,s))
        # create dataframe of data and save 
        self.book_df = pd.DataFrame(self.all_books)
        self.book_df.to_csv('all_books.csv', index=False)
        #logging
        m, s = str(int((time() - start)//60)), int((time() - start)%60)
        print('Total books:', str(len(self.all_books)), 'now at {}:{:02d}m'.format(m,s))
        
        
#add a method to update the repo i.e. if we were to update the whole book list, we could start from
# the last time we did this like by latest publication date or release date. Total books so far: 2532 now at 74:21m






start = time()
nyt = TimesBestsellers()
nyt.get_book_list()
'''
test = nyt.list_names[0]['current']
print(test)
print(datetime.strptime(test, nyt.dt))
'''
