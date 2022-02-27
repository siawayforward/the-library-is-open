#modules
from google_books import GoogleBooks
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np


class BookSimilarity:

    def __init__(self):
        self.book_df = pd.read_csv('all_books.csv').reset_index()

    
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

    def vectorize_text_features(self):
        # create tfidf vectors
        """
        Transform the text from the book features (name, authors, description, publication year) into
        vectors that will be used to compute book feature similarity.
        """
        vectorizer = TfidfVectorizer()
        self.tfidf_vectors = vectorizer.fit_transform(self.book_df['target'].replace(np.nan, "n/a"))
        self.tfidf_features = vectorizer.get_feature_names_out()   

    def compute_feature_similarities(self):
        """
        Compute book similarities by computing cosine similarity based on vector transformations
        """
        #get data from file
        self.vectorize_text_features()
        self.similarities = cosine_similarity(self.tfidf_vectors)



