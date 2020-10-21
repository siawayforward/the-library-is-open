#modules
from nyt_bestsellers import TimesBestsellers, Book
from time import time
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from string import punctuation
import pandas as pd


class BookSimilarity:

    def __init__(self):
        start = time()
        self.books = TimesBestsellers().get_book_list()
        # check computation time
        m, s = str(int((time() - start)//60)), int((time() - start)%60)
        print('Time: {}:{:02d}m - done getting books history from the all lists\n'.format(m,s))
        print('Total books:', str(len(books.all_books))) 

    
    def get_book_recommendations(self, text, top_n):
        '''
        Get the `top_n` number of recommendations for given `text`
        '''
        pass   

       
    def compute_feature_similarities(self):
        pass


    def process_text_features(self):
        self.send_to_dataframe()
        # create tfidf vectors
        vectorizer = TfidfVectorizer()
        tfidf_vectors = vectorizer.fit_transform(list(self.book_df['target']))
        tfidf_features = vectorizer.get_feature_names()
        # store values in dataframe with book identifier
        


    def send_to_dataframe(self):
        book_list = []
        for book in self.books:
            book = self.pre_process_book_data(book)
            item = {'title': book.title, 'author': book.author, 'description': book.description, 
                    'target': book.title + ' ' + book.description, 'isbn13': book.primary_isbn13}
            book_list.append(item)
        # create dataframe and have isbn as index
        self.book_df = pd.DataFrame(book_list).set_index('isbn13')

    
    def pre_process_book_data(self, book):
        # lower case removing punctuation and stopwords
        book.title = book.title.lower()
        book.description = book.description.lower().translate(str.maketrans('', '', punctuation))
        book.description = ' '.join([w for w in book.description.split()
                                    if w not in stopwords.words('english')])
        # creating dataframe with title, author, synopsis before lemmatizing, vectorizing
        return book    