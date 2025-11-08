# Write your MySQL query statement below
#we are asked to retreive the name, population, and area of countries that have at least 3 million square kilometers or 2.5 million people
#yeah thats it lol
select name,population,area 
from world 
where population >=25000000 or area >= 3000000