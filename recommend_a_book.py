from book_similarity import BookSimilarity

class BookRecommender:
    '''
        Wrapper class that includes all steps and functions for retrieving book corpus, cleaning
        data, getting a user book selection, and returning recommendations based on that selection
    '''

    # only run this to update total book list during down times
    def __init__(self, update=False):
        if update:
            BookSimilarity().update_book_corpus()

    # get recommendations based on what the user has entered
    def display_recommendations(self, book_title, book_author, n=6):
        bs = BookSimilarity()
        title, author, top_n = book_title, book_author, n
        self.recommendations = bs.get_book_recommendations(title, author, top_n)
        return self.recommendations


#moment of truth (testing here)
BookRecommender(update=False).display_recommendations("the vanishing half", "brit bennett")