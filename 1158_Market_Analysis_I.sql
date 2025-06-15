# Write your MySQL query statement below
select user_id as buyer_id, join_date,
(select count(*) from Orders where buyer_id = user_id and YEAR(order_date) = '2019') as orders_in_2019
from Users