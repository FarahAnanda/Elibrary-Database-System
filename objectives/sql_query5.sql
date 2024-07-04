SELECT ROUND(AVG(return_date - loan_date)) AS average_loan_duration
FROM Loan
WHERE return_date IS NOT NULL;
