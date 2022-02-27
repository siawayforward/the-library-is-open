import requests
import pandas as pd
from retrieve_api_keys import get_API_keys
from pprint import PrettyPrinter
import streamlit as st


pp = PrettyPrinter(indent=4)

class GoogleBooks:
    '''
        This class uses the Google Books API to get the details of a book that is not in the 
        New York Times Best sellers list and adds it to the corpus to get a recommendation for the
        reader
    '''
    def __init__(self, title=None, author=None):
        #self.headers = {'api-key': get_API_keys()[1], 'q': None, 'inauthor': None}
        self.headers = {'api-key': st.secrets.api_keys.google, 'q': None, 'inauthor': None}
        self.book_ep = 'https://www.googleapis.com/books/v1/volumes'
        if title: self.headers['q'] = title
        if author: self.headers['inauthor'] = author

    
    def get_book(self):
        retrieved_book = None
        try:
            response = requests.get(self.book_ep, params=self.headers)
            top_result = response.json()['items'][0]['volumeInfo']
            rating = None
            if 'averageRating' in top_result.keys():
                rating = top_result['averageRating']
            retrieved_book = {
                'title': top_result['title'],
                'author': ', '.join(top_result['authors']),
                'description': top_result['description'],
                'target': None,
                'primary_isbn13': top_result['industryIdentifiers'][0]['identifier'],
                'weeks': None,
                'rating': rating,
                'genre': ', '.join(top_result['categories'])
            }
            print(retrieved_book)
        except: 
            print('Failed to find or retrieve book requested.')
            print('Recommendation will be based on title and author only')
        return retrieved_book



    



#gb = GoogleBooks(title='Vanishing Half')
#gb.get_book()