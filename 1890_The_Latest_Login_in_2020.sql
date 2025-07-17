# Write your MySQL query statement below
select user_id, max(time_stamp) as last_stamp from
(select * from Logins where year(time_stamp) = 2020) l
group by user_id