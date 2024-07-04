SELECT b.title, COUNT(h.hold_id) AS total_holds
FROM Hold h
JOIN Book b ON h.book_id = b.book_id
GROUP BY b.title
ORDER BY total_holds DESC
LIMIT 10;
