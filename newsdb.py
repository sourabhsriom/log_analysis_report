# "Database code" for the reporting tool

import datetime
import psycopg2
import bleach

# setting the database name
DBNAME = "news"


def get_top_authors():

    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()

    query = '''select * from best_authors;'''
    cursor.execute(query)

    return cursor.fetchall()
    db.close()


def get_top_articles():

    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()

    query = '''select * from best_articles;'''
    cursor.execute(query)
    return cursor.fetchall()
    db.close()


def get_fails():

    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    query = '''select visits.date as date,
        round(cast(cast(fails.count as float)
        /cast(visits.count as float) * 100 as numeric), 2)
        as errors
        from visits
        inner join fails
        on visits.date = fails.date
        where cast(fails.count as float)/cast(visits.count as float) > 0.01;'''

    cursor.execute(query)
    return cursor.fetchall()
    db.close()
