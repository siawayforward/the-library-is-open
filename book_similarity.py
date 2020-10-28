#modules
from nyt_bestsellers import TimesBestsellers
from google_books import GoogleBooks
from time import time
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from string import punctuation
import pandas as pd


class BookSimilarity:

    def __init__(self):
        self.books = pd.read_csv('books.csv').reset_index()

    
    def get_book_recommendations(self, title, author, top_n=10):
        '''
            Get the `top_n` number of recommendations for given `book_title` and `author`
        '''
        GoogleBooks(title, author)
        self.compute_feature_similarities()
        target = self.book_df[(self.book_df['title'] == title)].index.values[0]
        pairs = list(enumerate(self.similarities[target]))
        self.recommendations = sorted(pairs, key=lambda x:x[1], reverse=True)[0:top_n]
        return self.recommendations


    def compute_feature_similarities(self):
        #get data from file
        self.book_df = pd.read_csv('books.csv').reset_index()
        self.vectorize_text_features()
        self.similarities = cosine_similarity(self.tfidf_vectors)


    def vectorize_text_features(self):
        # create tfidf vectors
        vectorizer = TfidfVectorizer()
        self.tfidf_vectors = vectorizer.fit_transform(self.book_df['target'])
        self.tfidf_features = vectorizer.get_feature_names()


    def store_books_data(self):
        book_list = []
        for book in self.books:
            book = self.pre_process_book_data(book)
            if book.title and book.description and book.author and book.primary_isbn13:
                item = {'title': book.title, 'author': book.author, 
                    'description': book.description, 
                    'target': book.title + ' ' + book.description, 'isbn13': book.primary_isbn13}
            book_list.append(item)
        # create dataframe of data and save
        self.book_df = pd.DataFrame(book_list)
        self.book_df.to_csv('books.csv', index=False)

    
    def pre_process_book_data(self, book):
        # lower case removing punctuation and stopwords
        if book.title:
            book.title = book.title.lower()
        if book.description:
            book.description = book.description.lower().\
                            translate(str.maketrans('', '', punctuation))
            book.description = ' '.join([w for w in book.description.split()\
                                    if w not in stopwords.words('english')])
        # creating dataframe with title, author, synopsis before lemmatizing, vectorizing
        return book    


    def update_book_corpus(self):
        start = time()
        nyt = TimesBestsellers()
        self.books = nyt.get_book_list()
        self.store_books_data()
        # check computation time
        m, s = str(int((time() - start)//60)), int((time() - start)%60)
        print('Time: {}:{:02d}m - done getting books history from the all lists\n'.format(m,s))
        print('Total books:', str(len(self.books))) 
