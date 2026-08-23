# Write your MySQL query statement below
select Temp.person_name from (
    select * ,sum(weight) over(order by turn asc) as elligible_weight  from Queue
) as Temp
where Temp.elligible_weight<=1000
order by Temp.turn desc
limit 1;
