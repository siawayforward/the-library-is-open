from book_similarity import BookSimilarity

class BookRecommender:
    '''
        Wrapper class that includes all steps and functions for retrieving book corpus, cleaning
        data, getting a user book selection, and returning recommendations based on that selection
    '''

    def display_recommendations(self):
        book_sim = BookSimilarity()
        title, author, top_n = self.get_user_conditions()
        self.recommendations = self.book_sim.get_book_recommendations(title, author, top_n)

        print('We think these titles are a great follow-up to {} by {}:'
                .format(title, author))
        for book in self.recommendations:
            book_row = self.book_sim.book_df.iloc[book[0]] 
            print(book_row['title'].title(),'by', book_row['author'].title())


    def get_user_conditions(self):
        title = input('What book have you read recently?\n')   
        while title is None:
            title = input('Uh Oh! We didn\'t get that. What book did you read?\n')
            author = input('OK! What\'re the author\'s first and last names?\n')
            while author is None:
                author = input('We missed that author! Who wrote {} again?\n'.format(title))     
        return title, author, 5



#moment of truth
x = BookRecommender()
x.display_recommendations()