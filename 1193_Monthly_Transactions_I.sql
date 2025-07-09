# Write your MySQL query statement below
SELECT LEFT(trans_date, 7) AS month, country, count(*) as trans_count, sum(case state when 'approved' then 1 else 0 end) as approved_count, sum(amount) as trans_total_amount, sum(case state when 'approved' then amount else 0 end) as approved_total_amount FROM Transactions GROUP BY month, country
