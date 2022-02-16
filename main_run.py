from recommend_a_book import BookRecommender as br
import pandas as pd
import streamlit as st
from PIL import Image


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
title = st.text_input('What book have you read recently?')
author = st.text_input('OK! What\'re the author\'s first and last names?')

# buttons
search_button = st.button("Hit Me!!")
reset_button = st.button("Can we start over?")

if search_button:
    while title=="":
        title = st.text_input('Uh Oh! We didn\'t get that. What book did you read?')
    while author=="":
        author= st.text_input('We missed that author! Who wrote {} again?'.format(title))

# reset to start over
if reset_button:
    title = st.text_input('What book have you read recently?')
    author = st.text_input('OK! What\'re the author\'s first and last names?')

#see if book is in bestsellers list or can be retrieved from google books first
loadstate = st.text('Let\'see about this one!')
books = br.find_book(title, author)

loadstate.text('Found your book! Finding you recommendations...')
recommendations = br().display_recommendations(title, author)

recommendations_header = 'We think these titles are great follow-ups to {} by {}:'.format(title, author)
no_recs = 'Sorry, we couldn\'t find your next obsession this time :('

if len(recommendations) > 1:
    loadstate.text(recommendations_header)
    # display recommendations
    for book in recommendations:
        book_row = books.iloc[book[0]] 
        if int(book[1]) != 1:
            st.write(book_row['title'].title(),'by', book_row['author'].title())
else:
    loadstate.text(no_recs)

