# Write your MySQL query statement below
select signups.user_id, ROUND(COALESCE(COUNT(CASE WHEN action='confirmed' THEN 1 END) / NULLIF(COUNT(*), 0), 0), 2) as confirmation_rate
from signups left outer join confirmations
on signups.user_id = confirmations.user_id
group by signups.user_id;