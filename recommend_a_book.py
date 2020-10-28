from book_similarity import BookSimilarity

class BookRecommender:
    '''
        Wrapper class that includes all steps and functions for retrieving book corpus, cleaning
        data, getting a user book selection, and returning recommendations based on that selection
    '''

    def __init__(self, update=False):
        if update:
            BookSimilarity().update_book_corpus()


    def display_recommendations(self):
        bs = BookSimilarity()
        title, author, top_n = self.get_user_conditions()
        self.recommendations = bs.get_book_recommendations(title, author, top_n)
        print('We think these titles are great follow-ups to {} by {}:'
                .format(title.title(), author.title()))
        for book in self.recommendations:
            book_row = bs.book_df.iloc[book[0]] 
            if int(book[1]) != 1:
                print(book_row['title'].title(),'by', book_row['author'].title())


    def get_user_conditions(self):
        title, author = input('What book have you read recently?\n'), None
        while title is None:
            title = input('Uh Oh! We didn\'t get that. What book did you read?\n')
        author = input('OK! What\'re the author\'s first and last names?\n')
        while author is None:
            author = input('We missed that author! Who wrote {} again?\n'.format(title))     
        return title, author, 6



#moment of truth
#BookSimilarity().update_book_corpus()
BookRecommender().display_recommendations()