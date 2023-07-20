select area,min(score) from h_score where score >= '763' group by area

select area,max(score) from h_score group by area

select area from h_score where score >= '763' group by area

select temp.area,min(temp.score) from (select area,score,num,total_num from h_score where score >= '763') as temp  group by temp.area

select * from  h_score where score = '763'
select sum(total_num) from h_score where score = '763'
