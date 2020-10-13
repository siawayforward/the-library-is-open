#modules
import json
import requests

class goodreads():

    def __init__(self):
        pass

    def load_books(self):
        pass

    def book(self, target_title):
        #get all book's characteristics
        self.book = {}
        self.book['title'] = self.get_title()
        self.book['author'] = self.get_author()
        self.book['genre'] = self.get_book_genre()
        self.book['synopsis'] = self.get_synopsis()
        self.book['year'] = self.get_release_year()
        self.book['avg_rating'] = self.get_average_rating()
        self.book['current_rank'] = self.get_current_rank()

    def get_title(self, target_title):    
        self.book_title = target_title    
        return self.book_title        

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
