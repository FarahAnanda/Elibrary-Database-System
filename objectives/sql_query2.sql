SELECT g.genre_name, COUNT(lo.loan_id) AS total_loans
FROM Genre g
JOIN BookGenre bg ON g.genre_id = bg.genre_id
JOIN Loan lo ON bg.book_id = lo.book_id
GROUP BY g.genre_name
ORDER BY total_loans DESC;
