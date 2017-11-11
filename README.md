## Report on user data of our awesome library

This is a report that we have in order to get some information on the top authors, articles and access failures. This is a python based report, pulling data from our news database.

## Prerequisites

- Python 3.6 or higher
- GitHub account

## Preparation required

To minimize the sql queries we will be writing in our python program, we create a few views(with instructions how to create them) in our news database namely :

- visits
   ```
   create view visits as
  SELECT log."time"::date AS date,
    count(log.id) AS count
   FROM log
  GROUP BY (log."time"::date);
  ```
- fails
  ```
  create view fails as
  SELECT log."time"::date AS date,
    count(log.id) AS count
   FROM log
  WHERE log.status <> '200 OK'::text
  GROUP BY (log."time"::date);
  ```

- articles_visited
  ```
  create view articles_visited as
  SELECT replace(replace(log.path, '-'::text, ' '::text), '/article/'::text, ''::text) AS article,
    count(log.id) AS counts
   FROM log
  WHERE log.status = '200 OK'::text AND replace(replace(log.path, '-'::text, ' '::text),
   '/article/'::text, ''::text) <> '/'::text
  GROUP BY (replace(replace(log.path, '-'::text, ' '::text), '/article/'::text, ''::text));
  ```
- best_authors
  ```
  create view best_authors as
  SELECT authors.name,
    sum(articles_visited.counts) AS sum
   FROM articles
     JOIN articles_visited ON regexp_replace(lower(articles.title), ''''::text, ''::text) ~~ format('%%%s%%'::text, lower(articles_visited.article))
     JOIN authors ON authors.id = articles.author
  GROUP BY authors.name
  ORDER BY (sum(articles_visited.counts)) DESC;
  ```


- best_articles
  ```
  create view best_articles as
  SELECT articles.title,
    articles_visited.counts
   FROM articles
     JOIN articles_visited ON regexp_replace(lower(articles.title), ''''::text, ''::text) ~~ format('%%%s%%'::text, lower(articles_visited.article))
  ORDER BY articles_visited.counts DESC;
  ```

## Instructions

- Login to your GitHub account.
- Clone the repository at https://github.com/sourabhsriom/log_analysis_report
- Change directory to the location where the cloned repository resides.
- If the news database doesn't exist, unzip the newsdata.sql.zip file.
- Run the following command to populate the database: ```psql -d news -f newsdata.sql```
- If you already have access to the default news database, create the views as listed in the Preparation required section.
- Once all the views have been created run the report.py file with the command ```python3 report.py```
- You should see the results expected from the project.
