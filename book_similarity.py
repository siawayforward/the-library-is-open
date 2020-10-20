#modules
#from nyt_bestsellers import TimesBestsellers
from time import time
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from string import punctuation
import pandas as pd
import re
nltk.download('all')

'''
def load_data():

    start = time()
    books = TimesBestsellers().get_book_list()
    m, s = str(int((time() - start)//60)), int((time() - start)%60)

    print('Time: {}:{:02d}m - done getting books history from the all lists\n'.format(m,s))
    print('Total books:', str(len(books.all_books)))


def clean_book_data(book):
    #lower case removing punctuation
    book['title'] = re.sub(book['title'].lower())
    book['synopsis'] = book['synopsis'].lower().translate(str.maketrans('', '', punctuation))
    #removing stopwords
    book['synopsis'] = ' '.join([w for w in book['synopsis'].split() 
                                if w not in stopwords.words('english')])
    #creating dataframe with title, author, synopsis before lemmatizing, vectorizing
    book_df = pd.DataFrame()
'''


