SELECT l.library_id, l.library_name, COUNT(lb.book_id) AS total_books
FROM LibraryBooks lb
JOIN Library l ON lb.library_id = l.library_id
GROUP BY l.library_id, l.library_name;
