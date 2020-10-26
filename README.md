# the-library-is-open

After learning about APIs and as a fan of machine learning algorithms, this is an attempt at creating a recommender system of books/authors for a user. It was originally supposed to be a book recommender system, but the API to use changed some main components this idea was centered around, so until then, we were going to do poems. However, we come back to books and find a way!

Also note, this was decided on October 7, 2020 -> Toni Morrison's Nobel Prize winning anniversary (1993) and what also happens to be Toni Braxton's birthday - a day I affectionately call **Toni Day**. It is therefore appropriate to do this with legendary wordsmiths in mind! :blue_heart:

Onward :muscle:

## Data

The book information and ratings are compiled from the [New York Times Bestseller's Books API](https://developer.nytimes.com/docs/books-product/1/overview). Because of access key compliance, the file that loads the keys is not included as it is just for the data generation stage. Sometimes, a user will search for a title that was not in the Bestseller's list. For that, [Google's Books API](https://developers.google.com/books) is used to get the details of the title in order to still get the user a well-informed recommendation. That key is also read in from the file.

For replication, store your NYT Books and Google books in a `keys.txt` file in the same directory as the other files. The values should be stored on the two lines as follows (copy and paste the below, even with spaces, and just replace the API key strings):
> nyt, `<api-key-string>`
> google, `<api-key-string>`

To just run the recommender system with already retrieved data, use the `recommend_a_book.py` script.

## Instructions *

- Download all `.py` files from the repository and the `books.csv` file
- To run on your terminal, use command

```cmd
    python recommend_a_book.py
```

*Currently working on production version
*The instructions above are for system once completed - still in process
