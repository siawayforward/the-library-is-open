#modules
import collections
import json
import requests

class OpenLibrary():

    def __init__(self):
        #defined named tuple of all book's characteristics
        self.Text = collections.named_tuple('Book', 
                    ['title', 'author', 'genre', 'synopsis', 'year', 'ISBN', 'avg_rating', 'current_rank'])

    def load_books(self):
        pass

    def retrieve_book_details(self, target_title):
        #DO API STUFF HERE
        self.book = self.Text(target_title, #works
                            self.get_author(), 
                            self.get_book_themes(), #works
                            self.get_synopsis(), #works
                            self.get_original_release_year(), #edition
                            self.get_ISBN(), #edition
                            self.get_pages(), #edition
                            self.get_average_rating(),
                            self.get_current_rank())      

'''
general information about a book that may have multiple editions (works API)
Works API - example: https://openlibrary.org/works/OL45883W.json
Edition API - example: https://openlibrary.org/books/OL7353617M.json

Books API - has everything except average rating and current rank
But we also get the goodreads ID which might help with rank/ratings
We could use the works API to get the ID from the title and use that to get details?
Books API (generic): https://openlibrary.org/api/books?bibkeys=ISBN:9780980200447&jscmd=details&format=json

    def get_author(self):
        pass

    def get_book_genre(self):
        pass

    def get_synopsis(self):
        pass

    def get_release_year(self):
        pass

    def get_average_rating(self):
        pass

    def get_current_rank(self):
        pass
    
    def get_user_ratings(self):
        pass
'''