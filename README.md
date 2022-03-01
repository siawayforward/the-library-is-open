# the-library-is-open

After learning about APIs and as a fan of machine learning algorithms and systems (the equitable ones anyway), this is an attempt at creating a recommender system of books for a user. It was originally supposed to be a broad book recommender system, but the API to use changed some main components this idea was centered around, so until then, we were going to do poems. However, we came back to books and found a way! To accomplish this, a smaller universe of book selections is used - thanks to The New York Times Bestseller's List.

Also note, this was decided on October 7, 2020 -> Toni Morrison's Nobel Prize winning anniversary (1993) and what also happens to be Toni Braxton's birthday - a day I affectionately call **Toni Day**. It is therefore appropriate to do this with legendary wordsmiths in mind! :blue_heart:

Onward :muscle:

## Status

In refactor mode, `main_run` does not work as of 2.15.2022

As of 2.26.2022, [hosted on streamlit](https://share.streamlit.io/siawayforward/the-library-is-open/main/main_run.py)

## Data

The book information and ratings are compiled from the [New York Times Bestseller's Books API](https://developer.nytimes.com/docs/books-product/1/overview). Because of access key compliance, the file that loads the keys is not included as it is just for the data generation stage. Sometimes, a user will search for a title that was not in the Bestseller's list. For that, [Google's Books API](https://developers.google.com/books) is used to get the details of the title in order to still get the user a well-informed recommendation. That key is also read in from the file.

For replication, store your NYT Books and Google books in a `keys.txt` file in the same directory as the other files. The values should be stored on the two lines as follows (copy and paste the below, even with spaces, and just replace the API key strings):
> nyt, `<api-key-string>`
> google, `<api-key-string>`

- Open the `recommend_a_book.py` script and change line 38 to appear as follows so `update=True`:

```python
    BookRecommender(update=True).display_recommendations()
```

Note, this will take a good amount of time to run, so have dinner and watch an episode of Love is Blind or Twenties while waiting. My hope is that the next phase will include time optimizations as the main refactoring goal.

---

## Instructions *

To just run the recommender system with already retrieved data:

- Navigate to streamlit app page
- Enter book read, and click `Run Me`
- To start over, click `Can we start over?`
- If book is not found in corpus, message will appear to notify you.

### Known Issues

- Can only get good recommendations if the author's name and book title are entered correctly (it is OK if the entry is mixed case)
- The recommendations are currently only for English language books. The hope is to keep building and making it more inclusive
- The book selections are mainly from the NYT Bestsellers list in the new millenium. This is a scope issue. The list of books will grow with more improvements for time and space complexity efficiencies.
