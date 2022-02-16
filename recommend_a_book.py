from book_similarity import BookSimilarity
from google_books import GoogleBooks
import pandas as pd

class BookRecommender:
    '''
        Wrapper class that includes all steps and functions for retrieving book corpus, cleaning
        data, getting a user book selection, and returning recommendations based on that selection
    '''

    # only run this to update total book list during down times
    def __init__(self, update=False):
        if update:
            BookSimilarity().update_book_corpus()
    
    # check if corpus has this book before finding recommendations (come back to change print statements)
    def find_book(title=None, author=None):
        books = pd.read_csv('all_books.csv')
        isbns = list(books.primary_isbn13)
        gb = GoogleBooks(title, author)
        retrieved_book = gb.get_book()
        if int(retrieved_book['isbn13']) in isbns: 
            print('book already there')
        else: #append to dataframe to update corpus if it isn't already there
            if retrieved_book: 
                print('book found, adding...')
                books.append(retrieved_book, ignore_index=True)
                print('...done!')
                books.to_csv('all_books.csv', index=False) 
                print('corpus updated')
            else:
                print('book not found, not added')
        return books

    # get recommendations based on what the user has entered
    def display_recommendations(self, book_title, book_author, n=6):
        bs = BookSimilarity()
        title, author, top_n = book_title, book_author, n
        self.recommendations = bs.get_book_recommendations(title, author, top_n)
        return self.recommendations


#moment of truth (testing here)
BookRecommender(update=False).display_recommendations("the vanishing half", "brit bennett")