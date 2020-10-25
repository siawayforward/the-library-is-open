import json
import requests
from datetime import datetime, timedelta
from dataclasses import dataclass
from time import time
from collections import namedtuple
from pprint import pprint
from retrieve_api_keys import *
from google_books import GoogleBooks

@dataclass
class Book:
    '''
        store the details of a book that has appeared on the New York Times Bestseller list
    '''
    title: str
    author: str
    description: str
    primary_isbn13: int


class TimesBestsellers:
    '''
        Class to retrieve the list of New York Times Bestsellers books in any fiction and 
        non-fiction categories from the new millenium
    '''
    def __init__(self):
        self.list_ep = 'https://api.nytimes.com/svc/books/v3/lists'
        self.search_date = datetime.now() # debut date of NYT Bestsellers is Oct 12 1931
        self.list_names = ['hardcover-fiction', 'hardcover-nonfiction', 'paperback-nonfiction',
                           'paperback-books', 'young-adult-paperback']
        self.headers = {'api-key': get_API_keys()[0],
                        'published-date': None, 'list': None}    


    def get_book_list(self):
        self.all_books = []
        # get list of ISBNs for books that have appeared on NYT Bestseller lists
        for name in self.list_names:
            self.headers['list'] = name
            start = time()
            while datetime(2000, 1, 1) < self.search_date:
                self.headers['published-date'] = self.search_date.strftime('%Y-%m-%d')
                try:
                    self.access_book_from_API(self.headers['list'])
                except: 
                    print('failing {}'.format(self.headers['published-date']))
                finally:
                    self.search_date = self.search_date - timedelta(days=7)
        return self.all_books


    def access_book_from_API(self, name):
        print('\ngetting books history from the {} lists'.format(name))
        response = requests.get(self.list_ep, params=self.headers)
        for book in response.json()['results']:
            txt = book['book_details'][0]
            item = Book(txt['title'], txt['author'], txt['description'], txt['primary_isbn13'])
            self.all_books.append(item)


    def find_book(self, title, author):
        titles = {book.title for book in self.all_books}
        authors = {book.author for book in self.all_books}
        if title in titles and authors[titles.index(title)] == author: 
            pass
        else:
            retrieved_book = GoogleBooks().get_book(title, author)
            if retrieved_book: self.all_books.append(retrieved_book)
            else:
                self.all_books.append(
                    Book(title=title, author=author, description='', primary_isbn13=0))