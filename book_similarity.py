#modules
from nyt_bestsellers import TimesBestsellers
from time import time
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from string import punctuation
import pandas as pd


class BookSimilarity:

    def __init__(self):
        start = time()
        nyt = TimesBestsellers()
        self.books = nyt.get_book_list()
        # check computation time
        m, s = str(int((time() - start)//60)), int((time() - start)%60)
        print('Time: {}:{:02d}m - done getting books history from the all lists\n'.format(m,s))
        print('Total books:', str(len(self.books))) 

    
    def get_book_recommendations(self, title, author, top_n=10):
        '''
            Get the `top_n` number of recommendations for given `book_title` and `author`
        '''
        TimesBestsellers().find_book(title, author)
        self.compute_feature_similarities()
        target = self.book_df[(self.book_df['title'] == title) & self.book_df['author'] == author]
        recommendations = self.similarity_scores[target.index.item()]
        self.top_recommendations = sorted(recommendations, key=lambda x: x[1])[:top_n]
        return self.top_recommendations


    def compute_feature_similarities(self):
        self.create_books_dataframe()
        self.vectorize_text_features()
        self.similarity_scores = cosine_similarity(self.vector_df)


    def vectorize_text_features(self):
        # create tfidf vectors
        vectorizer = TfidfVectorizer()
        self.tfidf_vectors = vectorizer.fit_transform(self.book_df['target'])
        self.tfidf_features = vectorizer.get_feature_names()


    def create_books_dataframe(self):
        book_list = []
        for book in self.books:
            book = self.pre_process_book_data(book)
            item = {'title': book.title, 'author': book.author, 'description': book.description, 
                    'target': book.title + ' ' + book.description, 'isbn13': book.primary_isbn13}
            book_list.append(item)
        # create dataframe of data
        self.book_df = pd.DataFrame(book_list)

    
    def pre_process_book_data(self, book):
        # lower case removing punctuation and stopwords
        book.title = book.title.lower()
        book.description = book.description.lower().translate(str.maketrans('', '', punctuation))
        book.description = ' '.join([w for w in book.description.split()
                                    if w not in stopwords.words('english')])
        # creating dataframe with title, author, synopsis before lemmatizing, vectorizing
        return book    