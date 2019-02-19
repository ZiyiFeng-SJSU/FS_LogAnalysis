# "Database code" for the DB Forum.

import psycopg2
import bleach

DBNAME = "news"
PORTNUM = 5433


def most_popular_articles():
    db = psycopg2.connect(database=DBNAME, port=PORTNUM)
    c = db.cursor()
    c.execute("SELECT articles.title, COUNT(SUBSTRING(log.path, 10)) AS rank FROM articles JOIN log ON SUBSTRING(log.path, 10) LIKE articles.slug GROUP BY articles.title ORDER BY rank DESC LIMIT 3;")
    top3views = c.fetchall()
    db.close()
    return(top3views)


def author_rank():
    db = psycopg2.connect(database=DBNAME, port=PORTNUM)
    c = db.cursor()
    c.execute("SELECT au.name, autop.acount FROM (SELECT articles.author, COUNT(articles.author) AS acount FROM articles JOIN log ON SUBSTRING(log.path, 10) LIKE articles.slug GROUP BY articles.author ORDER BY acount DESC )autop JOIN authors au ON au.id = autop.author")
    authorrank = c.fetchall()
    db.close()
    return(authorrank)


def error_rate():
    db = psycopg2.connect(database=DBNAME, port=PORTNUM)
    c = db.cursor()
    c.execute("SELECT good.date, cast((good.ok * 1.0 )/total.all as decimal(10,2))*100 as erate FROM (SELECT date(time) as date, COUNT(status) AS ok FROM log WHERE status LIKE '200 OK' GROUP BY date) good, (SELECT date(time) as date, COUNT(status) AS all FROM log GROUP BY date) total WHERE good.date = total.date AND (good.ok * 1.0 )/total.all < 0.99 ORDER BY good.date; ")
    errors = c.fetchall()
    db.close()
    return(errors)
