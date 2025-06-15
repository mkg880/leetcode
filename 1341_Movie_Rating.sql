-- Write your PostgreSQL query statement below
with usr_cnt as (select user_id, count(*) as cnt from MovieRating group by user_id),
avgs as (select movie_id, avg(rating) as a from movierating where extract(month from created_at) = 2 and extract(year from created_at) = 2020 group by movie_id)
(select name as results from usr_cnt natural join Users where cnt = (select MAX(cnt) from usr_cnt) order by name limit 1)
UNION ALL 
(select title from avgs natural join Movies where a = (select MAX(a) from avgs) order by title limit 1)
