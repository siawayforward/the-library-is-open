from google_books import GoogleBooks
import pandas as pd



books = pd.read_csv('books_1.csv')


def find_book(title=None, author=None):
    isbns = list(books.primary_isbn13)
    gb = GoogleBooks(title, author)
    retrieved_book = gb.get_book()
    if int(retrieved_book['primary_isbn13']) in isbns: 
        print('book already there')
    else: #append to dataframe to update corpus if it isn't already there
        if retrieved_book: 
            print('book found, adding...')
            books.append(retrieved_book, ignore_index=True)
            print('...done!')
            books.to_csv('books_1.csv', index=False) 
            print('corpus updated')
        else:
            print('book not found, not added')
    return books


    


find_book(title='my sister the serial killer')


