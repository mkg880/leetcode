# Write your MySQL query statement below
with visit_wo_trans as
(select * from Visits where visit_id not in (select visit_id from Transactions))

select customer_id, count(*) as count_no_trans from visit_wo_trans group by customer_id