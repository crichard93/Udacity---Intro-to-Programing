#!/usr/bin/env python2.7.14
"""
Creator: Cory Richard
Last Modified: 4/09/2018

"""
import psycopg2
dbname = "news"
error_threshold = 0.010


def more_than_percent_errors():
    """returns all days that produced more than
    the error_threshold in the news database"""
    db = psycopg2.connect(database=dbname)
    c = db.cursor()
    c.execute("""SELECT cast(errors.date AS date),
        cast(errors.error_count AS float)/cast(daily_log.daily_views AS float)
        AS percent_errors_logs
        FROM errors, daily_log
        WHERE errors.date=daily_log.date AND
        cast(errors.error_count AS float)/cast(daily_log.daily_views AS float)
        > (%s);""", (error_threshold, ))
    daysanderrors = c.fetchall()
    db.close()
    return daysanderrors


def top3populararticles():
    """Queries the top 3 popular articles based on views and returns it"""
    db = psycopg2.connect(database=dbname)
    c = db.cursor()
    c.execute("""SELECT articles.title AS "Article Title",
        count(articles.id) AS "Times Viewed"
        FROM articles,log
        WHERE log.path LIKE '%' || articles.slug || '%'
        GROUP BY articles.id
        ORDER BY "Times Viewed" DESC
        LIMIT 3;""")
    articles = c.fetchall()
    db.close()
    return articles


def most_popular_authors():
    """Returns a list containing most popular authors the times they were Viewed
    from the news database"""
    db = psycopg2.connect(database=dbname)
    c = db.cursor()
    c.execute("""SELECT authors.name, count(authors.id) AS "Times Viewed"
        FROM(SELECT articles.author AS authorid
        FROM articles,log
        WHERE log.path LIKE '%' || articles.slug || '%') AS views, authors
        WHERE views.authorid=authors.id
        GROUP BY authors.id
        ORDER BY "Times Viewed" DESC;""")
    authors = c.fetchall()
    db.close()
    return authors


def print_popular_authors():
    """prints the authors by sorted by number of views"""
    authors = 0
    views = 1
    authorsandviews = most_popular_authors()
    print "Authors Ordered By Popularity:"
    print "Author ------ Views"
    for result in authorsandviews:
        print result[authors] + " ------ " + str(result[views])


def print_days_percent_errors():
    """prints the days that resulted in an error greater than
    the error threshld, 1.0% by default"""
    days = 0
    error = 1
    daysanderrors = more_than_percent_errors()
    print "Days where % error logs/total > " + str(error_threshold*100) + "%: "
    print "Day ------ Percent Status Error"
    for result in daysanderrors:
        print str(result[days]) + " ------ " + str(round(result[error]*100, 2))


def print_popular_articles():
    """prints the 3 most popular articles and their views"""
    articles = 0
    views = 1
    articlesandviews = top3populararticles()
    print "Top 3 Popular Articles:"
    print "Article Title ------ Views"
    for result in articlesandviews:
        print result[articles] + " ------ " + str(result[views])


def print_report():
    """prints the 3 reports"""
    print_days_percent_errors()
    print ""
    print_popular_authors()
    print ""
    print_popular_articles()
    print ""


print_report()
