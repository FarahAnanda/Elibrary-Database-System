-- Load data from CSV files into the corresponding tables

-- Library
COPY Library(library_id, library_name, library_address) 
FROM '/path/to/libraries.csv' 
DELIMITER ',' 
CSV HEADER;

-- Author
COPY Author(author_id, author_name) 
FROM '/path/to/authors.csv' 
DELIMITER ',' 
CSV HEADER;

-- Book
COPY Book(book_id, isbn, title, author_id, type) 
FROM '/path/to/books.csv' 
DELIMITER ',' 
CSV HEADER;

-- Genre
COPY Genre(genre_id, genre_name) 
FROM '/path/to/genres.csv' 
DELIMITER ',' 
CSV HEADER;

-- LibraryBooks
COPY LibraryBooks(library_id, book_id, quantity) 
FROM '/path/to/library_books.csv' 
DELIMITER ',' 
CSV HEADER;

-- BookGenre
COPY BookGenre(book_id, genre_id) 
FROM '/path/to/book_genres.csv' 
DELIMITER ',' 
CSV HEADER;

-- Member
COPY Member(member_id, member_name) 
FROM '/path/to/members.csv' 
DELIMITER ',' 
CSV HEADER;

-- LibraryCard
COPY LibraryCard(card_id, member_id, library_id, card_number, password) 
FROM '/path/to/library_cards.csv' 
DELIMITER ',' 
CSV HEADER;

-- Loan
COPY Loan(loan_id, library_id, book_id, card_id, loan_date, due_date, return_date) 
FROM '/path/to/loans.csv' 
DELIMITER ',' 
CSV HEADER;

-- Hold
COPY Hold(hold_id, library_id, book_id, card_id, hold_date, available_date, expiry_date) 
FROM '/path/to/holds.csv' 
DELIMITER ',' 
CSV HEADER;
