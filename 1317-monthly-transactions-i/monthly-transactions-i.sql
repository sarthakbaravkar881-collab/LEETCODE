SELECT 
    -- Convert date to string in YYYY-MM format
    TO_CHAR(trans_date, 'YYYY-MM') AS month,
    country,
    count(*) AS trans_count,
    sum(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
    sum(amount) AS trans_total_amount,
    sum(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY 
    month, 
    country;