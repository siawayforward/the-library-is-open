from numpy import place
from recommend_a_book import BookRecommender as br
import pandas as pd
import streamlit as st
from PIL import Image


# title for page
st.title("The Library is Open!")

# description and image
st.write("""
        As a huge fan of Drag Race, the name of this is inspired by RuPaul's Drag Race. Ru, 
        I don't intend to make money from this so you still own 51% of that whole company, 
        ma'am. Much love!
        """)
image = Image.open('rupaul-library.gif')
st.image(image, "Ru Paul noting to the queens in the reading challenge that the library is indeed about to be OPEN!")

# create streamlit objects to interact with   
header = None 
with st.form(key='ask_form', clear_on_submit=True):
    title = st.text_input('What book have you read recently?')
    author = st.text_input('OK! What\'re the author\'s first and last names?')
    # buttons
    search_button = st.form_submit_button("Hit Me!!")

    if search_button:
        if title=="" and author=="":
            st.info("If you wanna be searching somethin, you got to be typing somethin (both title and author) hihiiii!")
        elif (title=="" and author!="") or title=="":
            st.info("We need us a book to search, friend! Please enter one")
        elif author=="":
            st.info("Who wrote {}? We didn't quite get that".format(title))
        else:
            #see if book is in bestsellers list or can be retrieved from google books first
            loadstate = st.text('Let\'see about this one!')
            books = br.find_book(title, author)

            loadstate.text('Found your book! Finding you recommendations...')
            recommendations = br().display_recommendations(title.lower(), author.lower())

            recommendations_header = 'We think these titles are great follow-ups to **{}** by **{}**:'\
                .format(title.title(), author.title())
            no_recs = 'Sorry, we couldn\'t find your next obsession this time :('

            if len(recommendations) > 1:
                header = st.info(recommendations_header)
                # display recommendations
                for book in recommendations:
                    book_row = books.iloc[book[0]] 
                    if int(book[1]) != 1:
                        st.write("-",book_row['title'].title(),'by', book_row['author'].title())
            else:
                st.info(no_recs)

    # clearing results
    reset_button = st.form_submit_button("Can we start over?")