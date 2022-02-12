from google_books import GoogleBooks
#from book_similarity import BookSimilarity
import pandas as pd
import streamlit as st
from PIL import Image


books = pd.read_csv('all_books.csv')

def find_book(title=None, author=None):
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


def get_recommendations(title):
    #see if book is in bestsellers list or can be retrieved from google books first
    # this should all be after getting inputs so maybe set parameters for this method too.
    # let's do this tomorrow, IM SO PROUD OF YOU SIA!
    find_book(title)
"""   
      def get_user_conditions(self):
            title, author = input('What book have you read recently?\n'), None
        while title is None:
            title = input('Uh Oh! We didn\'t get that. What book did you read?\n')
        author = input('OK! What\'re the author\'s first and last names?\n')
        while author is None:
            author = input('We missed that author! Who wrote {} again?\n'.format(title))     
        return title, author, 6  
"""
    

# title for page
st.title("The Library is Open!")

# description and image
st.text("""
        As a huge fan of Drag Race, the name of this is inspired by RuPaul's Drag Race. Ru, I don't intend
        to make money from this so you still own 51% of that whole company, ma'am. Much love!
        """)
image = Image.open('rupaul-library.gif')
st.image(image, "Ru Paul noting to the queens in the reading challenge that the library is indeed about to be OPEN!")

# create streamlit objects to interact with



#test
#get_recommendations(title='my sister the serial killer')
