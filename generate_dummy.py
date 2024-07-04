import pandas as pd
import random
from faker import Faker

fake = Faker()

# Define constants
NUM_LIBRARIES = 5
NUM_AUTHORS = 20
NUM_BOOKS = 50
NUM_GENRES = 12
NUM_MEMBERS = 30
NUM_LIBRARY_CARDS = 60
NUM_LOANS = 100
NUM_HOLDS = 50

# Predefined genres
genres = ['fiction', 'nonfiction', 'historical', 'fantasy', 'self-help',
          'feminism', 'romance', 'YA', 'mystery', 'contemporary',
          'thriller', 'memoir']

fiction_genres = ['romance', 'mystery', 'YA', 'thriller', 'contemporary', 'fantasy', 'crime', 'historical']
nonfiction_genres = ['self-help', 'psychology', 'memoir', 'politics', 'crime', 'historical']

def generate_libraries(num_libraries):
    """
    Create a DataFrame for libraries.

    Parameters:
    - num_libraries (int): Number of libraries to generate.

    Returns:
    - pd.DataFrame: DataFrame containing library information such as library_id, library_name, and library_address.
    """
    libraries = []
    for _ in range(num_libraries):
        libraries.append({
            'library_id': fake.unique.random_int(min=1, max=9999),
            'library_name': fake.company(),
            'library_address': fake.address()
        })
    return pd.DataFrame(libraries)

def generate_authors(num_authors):
    """
    Create a DataFrame for authors.

    Parameters:
    - num_authors (int): Number of authors to generate.

    Returns:
    - pd.DataFrame: DataFrame containing author information such as author_id and author_name.
    """
    authors = []
    for _ in range(num_authors):
        authors.append({
            'author_id': fake.unique.random_int(min=1, max=9999),
            'author_name': fake.name()
        })
    return pd.DataFrame(authors)

def generate_books(num_books, authors):
    """
    Create a DataFrame for books.

    Parameters:
    - num_books (int): Number of books to generate.
    - authors (pd.DataFrame): DataFrame containing author information.

    Returns:
    - pd.DataFrame: DataFrame containing book information such as book_id, isbn, title, author_id, and type.
    """
    books = []
    for _ in range(num_books):
        article = random.choice(['The', 'A', 'An'])
        subject = fake.word().title()
        additional_word = fake.word().title()
        series_number = f" Book {random.randint(2, 5)}" if random.choice([True, False]) else ""
        title = f"{article} {subject} {additional_word}{series_number}".strip()

        books.append({
            'book_id': fake.unique.random_int(min=1, max=9999),
            'isbn': fake.isbn13(),
            'title': title,
            'author_id': random.choice(authors['author_id']),
            'type': random.choice(['book', 'audiobook'])
        })
    return pd.DataFrame(books)

def generate_genres():
    """
    Create a DataFrame for genres.

    Returns:
    - pd.DataFrame: DataFrame containing genre information such as genre_id and genre_name.
    """
    genres_list = []
    for genre in genres:
        genres_list.append({
            'genre_id': fake.unique.random_int(min=1, max=9999),
            'genre_name': genre
        })
    return pd.DataFrame(genres_list)

def generate_library_books(books, libraries):
    """
    Create a DataFrame linking books to libraries with quantity information.

    Parameters:
    - books (pd.DataFrame): DataFrame containing book information.
    - libraries (pd.DataFrame): DataFrame containing library information.

    Returns:
    - pd.DataFrame: DataFrame containing library book information such as library_id, book_id, and quantity.
    """
    library_books = []
    for _, book in books.iterrows():
        for _, library in libraries.iterrows():
            if random.random() < 0.5:
                library_books.append({
                    'library_id': library['library_id'],
                    'book_id': book['book_id'],
                    'quantity': random.randint(1, 10)
                })
    return pd.DataFrame(library_books)

def generate_book_genres(books, genres):
    """
    Create a DataFrame linking books to genres.

    Parameters:
    - books (pd.DataFrame): DataFrame containing book information.
    - genres (pd.DataFrame): DataFrame containing genre information.

    Returns:
    - pd.DataFrame: DataFrame containing book genre information such as book_id and genre_id.
    """
    book_genres = []
    book_genre_set = set()
    fiction_genre_ids = genres[genres['genre_name'].isin(fiction_genres)]['genre_id'].tolist()
    nonfiction_genre_ids = genres[genres['genre_name'].isin(nonfiction_genres)]['genre_id'].tolist()

    for _, book in books.iterrows():
        primary_genre = random.choice(['fiction', 'nonfiction'])
        primary_genre_id = genres[genres['genre_name'] == primary_genre]['genre_id'].values[0]
        book_genres.append({'book_id': book['book_id'], 'genre_id': primary_genre_id})
        book_genre_set.add((book['book_id'], primary_genre_id))

        while True:
            if primary_genre == 'fiction':
                additional_genre_id = random.choice(fiction_genre_ids)
            else:
                additional_genre_id = random.choice(nonfiction_genre_ids)
            if (book['book_id'], additional_genre_id) not in book_genre_set:
                book_genre_set.add((book['book_id'], additional_genre_id))
                book_genres.append({'book_id': book['book_id'], 'genre_id': additional_genre_id})
                break

    return pd.DataFrame(book_genres)

def generate_members(num_members):
    """
    Create a DataFrame for members.

    Parameters:
    - num_members (int): Number of members to generate.

    Returns:
    - pd.DataFrame: DataFrame containing member information such as member_id and member_name.
    """
    members = []
    for _ in range(num_members):
        members.append({
            'member_id': fake.unique.random_int(min=1, max=9999),
            'member_name': fake.name()
        })
    return pd.DataFrame(members)

def generate_library_cards(members, libraries):
    """
    Create a DataFrame for library cards associated with members and libraries.

    Parameters:
    - members (pd.DataFrame): DataFrame containing member information.
    - libraries (pd.DataFrame): DataFrame containing library information.

    Returns:
    - pd.DataFrame: DataFrame containing library card information such as card_id, member_id, library_id, card_number, and password.
    """
    library_cards = []
    for _ in range(NUM_LIBRARY_CARDS):
        library_cards.append({
            'card_id': fake.unique.random_int(min=1, max=9999),
            'member_id': random.choice(members['member_id']),
            'library_id': random.choice(libraries['library_id']),
            'card_number': fake.unique.random_int(min=10000000, max=99999999),
            'password': fake.password()
        })
    return pd.DataFrame(library_cards)

def generate_loans(num_loans, library_books, library_cards):
    """
    Create a DataFrame for book loans.

    Parameters:
    - num_loans (int): Number of loans to generate.
    - library_books (pd.DataFrame): DataFrame containing library book information.
    - library_cards (pd.DataFrame): DataFrame containing library card information.

    Returns:
    - pd.DataFrame: DataFrame containing loan information such as loan_id, library_id, book_id, card_id, loan_date, due_date, and return_date.
    """
    loans = []
    for _ in range(num_loans):
        loan_date = fake.date_between(start_date='-1y', end_date='today')
        due_date = loan_date + pd.Timedelta(days=14)
        return_date = loan_date + pd.Timedelta(days=random.randint(1, 14)) if random.random() > 0.5 else None
        loans.append({
            'loan_id': fake.unique.random_int(min=1, max=9999),
            'library_id': random.choice(library_books['library_id']),
            'book_id': random.choice(library_books['book_id']),
            'card_id': random.choice(library_cards['card_id']),
            'loan_date': loan_date,
            'due_date': due_date,
            'return_date': return_date
        })
    return pd.DataFrame(loans)

def generate_holds(num_holds, library_books, library_cards, loans):
    """
    Create a DataFrame for book holds.

    Parameters:
    - num_holds (int): Number of holds to generate.
    - library_books (pd.DataFrame): DataFrame containing library book information.
    - library_cards (pd.DataFrame): DataFrame containing library card information.
    - loans (pd.DataFrame): DataFrame containing loan information.

    Returns:
    - pd.DataFrame: DataFrame containing hold information such as hold_id, library_id, book_id, card_id, hold_date, available_date, and expiry_date.
    """
    holds = []
    for _ in range(num_holds):
        hold_date = fake.date_between(start_date='-1y', end_date='today')
        selected_loan = loans[loans['return_date'].notnull()].sample(n=1)
        available_date = selected_loan['return_date'].values[0] if not selected_loan.empty else None
        expiry_date = available_date + pd.Timedelta(days=7) if available_date else None
        holds.append({
            'hold_id': fake.unique.random_int(min=1, max=9999),
            'library_id': random.choice(library_books['library_id']),
            'book_id': random.choice(library_books['book_id']),
            'card_id': random.choice(library_cards['card_id']),
            'hold_date': hold_date,
            'available_date': available_date,
            'expiry_date': expiry_date
        })
    return pd.DataFrame(holds)

# Generate data
libraries_df = generate_libraries(NUM_LIBRARIES)
authors_df = generate_authors(NUM_AUTHORS)
books_df = generate_books(NUM_BOOKS, authors_df)
genres_df = generate_genres()
library_books_df = generate_library_books(books_df, libraries_df)
book_genres_df = generate_book_genres(books_df, genres_df)
members_df = generate_members(NUM_MEMBERS)
library_cards_df = generate_library_cards(members_df, libraries_df)
loans_df = generate_loans(NUM_LOANS, library_books_df, library_cards_df)
holds_df = generate_holds(NUM_HOLDS, library_books_df, library_cards_df, loans_df)

# Display data
print(libraries_df.head())
print(authors_df.head())
print(books_df.head())
print(genres_df.head())
print(library_books_df.head())
print(book_genres_df.head())
print(members_df.head())
print(library_cards_df.head())
print(loans_df.head())
print(holds_df.head())

# Save to CSV
libraries_df.to_csv('libraries.csv', index=False)
authors_df.to_csv('authors.csv', index=False)
books_df.to_csv('books.csv', index=False)
genres_df.to_csv('genres.csv', index=False)
library_books_df.to_csv('library_books.csv', index=False)
book_genres_df.to_csv('book_genres.csv', index=False)
members_df.to_csv('members.csv', index=False)
library_cards_df.to_csv('library_cards.csv', index=False)
loans_df.to_csv('loans.csv', index=False)
holds_df.to_csv('holds.csv', index=False)
