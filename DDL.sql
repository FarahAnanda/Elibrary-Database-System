CREATE TABLE Library (
    library_id SERIAL PRIMARY KEY,
    library_name VARCHAR(255) NOT NULL,
    library_address VARCHAR(255) NOT NULL
);

CREATE TABLE Author (
    author_id SERIAL PRIMARY KEY,
    author_name VARCHAR(255) NOT NULL
);

CREATE TABLE Book (
    book_id SERIAL PRIMARY KEY,
    isbn VARCHAR(17) UNIQUE NOT NULL,
    title VARCHAR(255) NOT NULL,
    author_id INT NOT NULL,
    type VARCHAR(50) CHECK (type IN ('book', 'audiobook')),
    FOREIGN KEY (author_id) REFERENCES Author(author_id)
);

CREATE TABLE Genre (
    genre_id SERIAL PRIMARY KEY,
    genre_name VARCHAR(255) NOT NULL
);

CREATE TABLE LibraryBooks (
    library_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity >= 0),
    PRIMARY KEY (library_id, book_id),
    FOREIGN KEY (library_id) REFERENCES Library(library_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
);

CREATE TABLE BookGenre (
    book_id INT NOT NULL,
    genre_id INT NOT NULL,
    PRIMARY KEY (book_id, genre_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (genre_id) REFERENCES Genre(genre_id)
);

CREATE TABLE Member (
    member_id SERIAL PRIMARY KEY,
    member_name VARCHAR(255) NOT NULL
);

CREATE TABLE LibraryCard (
    card_id SERIAL PRIMARY KEY,
    member_id INT NOT NULL,
    library_id INT NOT NULL,
    card_number VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    FOREIGN KEY (member_id) REFERENCES Member(member_id),
    FOREIGN KEY (library_id) REFERENCES Library(library_id)
);

CREATE TABLE Loan (
    loan_id SERIAL PRIMARY KEY,
    library_id INT NOT NULL,
    book_id INT NOT NULL,
    card_id INT NOT NULL,
    loan_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE DEFAULT NULL CHECK (return_date IS NULL OR return_date <= due_date),
    FOREIGN KEY (library_id) REFERENCES Library(library_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (card_id) REFERENCES LibraryCard(card_id)
);

CREATE TABLE Hold (
    hold_id SERIAL PRIMARY KEY,
    library_id INT NOT NULL,
    book_id INT NOT NULL,
    card_id INT NOT NULL,
    hold_date DATE NOT NULL,
    available_date DATE DEFAULT NULL,
    expiry_date DATE DEFAULT NULL CHECK (expiry_date IS NULL OR available_date IS NOT NULL),
    FOREIGN KEY (library_id) REFERENCES Library(library_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (card_id) REFERENCES LibraryCard(card_id)
);
