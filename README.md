# the-library-is-open

After learning about APIs and as a fan of machine learning algorithms, this is an attempt at creating a recommender system of books/authors for a user. It was originally supposed to be a book recommender system, but the API to use changed some main components this idea was centered around, so until then, we were going to do poems. However, we come back to books and find a way!

Also note, this was decided on October 7, 2020 -> Toni Morrison's Nobel Prize winning anniversary (1993) and what also happens to be Toni Braxton's birthday - a day I affectionately call **Toni Day**. It is therefore appropriate to do this with legendary wordsmiths in mind! :blue_heart:

Onward :muscle:

## Data

The book information and ratings are compiled from the [Open Library API](https://openlibrary.org/dev/docs/api/books). The list of books itself is compiled from the [New York Times Bestseller's Books API](https://developer.nytimes.com/docs/books-product/1/overview). Because of access key compliance, the file that loads the list of book ISBNs is not included as it is just for the data generation stage.
