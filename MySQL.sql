/*
This SQL file contains solutions for SQL LeetCode problems
*/

-- 1757. Recyclable and Low Fat Products
select product_id
from products
where low_fats = 'Y'
intersect
select product_id
from products
where recyclable = 'Y'

-- 584. Find Customer Referee
select name
from customer
where referee_id != 2 or referee_id is null

-- 595. Big Countries
select name, population, area
from world
where area >= 3000000
or population >= 25000000

-- 1148. Article Views 1
select distinct author_id as id
from views
where author_id = viewer_id
order by author_id

-- 1683. Invalid Tweets
select tweet_id
from tweets
where length(content) > 15

-- 1378. Replace Employee ID with the Unique Identifier
select unique_id, name
from employees e
left join employeeuni uni 
on e.id = uni.id

-- 1068. Product Sales Analysis 1
select product_name, year, price
from sales s
natural join product p