## Report on user data of our awesome library

This is a report that we have in order to get some information on the top authors, articles and access failures. This is a python based report, pulling data from our news database.

## Prerequisites

- Python 3.6 or higher
- GitHub account

## Preparation required

To minimize the sql queries we will be writing in our python program, we create a few views in our news database namely :

- visits
- fails
- articles_visited
- best_authors
- best_articles
  select title,counts from articles inner join articles_visited on regexp_replace(lower(articles.title), '''', '') like format('%%%s%%',lower( articles_visited.article)) order by counts desc

## Instructions

- Login to your GitHub account.
