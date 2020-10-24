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

    
    def get_book_recommendations(self, title, author, top_n=10):
        '''
            Get the `top_n` number of recommendations for given `book_title` and `author`
        '''
        

       
    def compute_feature_similarities(self):
        self.create_books_dataframe()
        self.vectorize_text_features()
        similarity_scores = cosine_similarity(self.vector_df)
        self.sorted_similarities = sorted(self.sorted_similarities)
        #revisit this method - completed when you were sleepy
        

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


'''
    DONE - get the list of list names
    get the list of books from the lists (only store ISBN) 
    DONE - how do we get all lists from the beginning of time?
    use descriptions, genre to make recommendations
    DONE - we could make tdidf vectorizers and use those to calculate cosine-similarity
    - suggest top 10 books with highest similarity scores
    engine:
    - you enter a book title and author
    - we search the repo of books from NYT best sellers and give a recommendation
    - if book not in New York Times list, search for book data in open library API
        = From there, get details of book and then add it to the book_df
        = calculate its similarity score and add to the similarities list

'''