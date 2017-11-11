# "Database code" for the reporting tool

import datetime
import psycopg2
import bleach

# setting the database name
DBNAME = "news"


def sqlFetch(query):

    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    return results


def get_top_authors():

    query = '''select * from best_authors limit 3;'''
    authors = sqlFetch(query)
    return authors


def get_top_articles():

    query = '''select * from best_articles limit 3;'''
    articles = sqlFetch(query)
    return articles


def get_fails():

    query = '''select visits.date as date,
        round(cast(cast(fails.count as float)
        /cast(visits.count as float) * 100 as numeric), 2)
        as errors
        from visits
        inner join fails
        on visits.date = fails.date
        where cast(fails.count as float)/cast(visits.count as float) > 0.01;'''

    fails = sqlFetch(query)
    return fails
