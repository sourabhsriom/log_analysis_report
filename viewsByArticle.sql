select title,counts from articles inner join articles_visited on regexp_replace(lower(articles.title), '''', '') like format('%%%s%%',lower( articles_visited.article)) order by counts desc
/*query for most viewed articles*/
select title,counts from articles
 inner join articles_visited
 where lower(articles.title)
 like format('%%%s%%',lower( articles_visited.article))
 order by counts desc limit 3;

/*  query for most viewed authors */
select authors.name,  sum(counts) from articles inner join articles_visited on regexp_replace(lower(articles.title), '''', '') like format('%%%s%%',lower( articles_visited.article)) inner join authors on authors.id = articles.author group by authors.name order by sum(counts) desc limit 3;


/* query to find date for more than 1% fails */
select visits.date as date, round(cast(cast(fails.count as float)/cast(visits.count as float)  * 100 as numeric), 2) as errors from visits inner join fails on visits.date = fails.date where cast(fails.count as float)/cast(visits.count as float) > 0.01;


select cast(fails.count as float)/cast(visits.count as float) as errors from visits inner join fails on visits.date = fails.date limit 5;

select round(cast(cast(fails.count as float)/cast(visits.count as float) as numeric), 2) as errors from visits inner join fails on visits.date = fails.date limit 5;
