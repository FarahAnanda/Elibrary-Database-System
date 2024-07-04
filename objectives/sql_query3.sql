SELECT l.library_id, l.library_name, COUNT(lo.loan_id) AS total_loans
FROM Loan lo
JOIN Library l ON lo.library_id = l.library_id
WHERE lo.return_date IS NULL
GROUP BY l.library_id, l.library_name;
