#!/usr/bin/env python3

"""
Extract keywords from a text file and load them into a db
"""

from main import extract_keywords, make_hashtags, read_file
import click
import sqlite3
import os
from os import path 

DATABASE = "keywords.db"

def load_keywords(keywords, score, hashtags):
    """
    Load keywords, scores and their hashtags into a db 
    """
    db_exists = False

    if path.exists(DATABASE):
        db_exists = True

    # Creating a cursor object using the cursor() method
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    c.execute(
        "CREATE TABLE IF NOT EXISTS keywords (keyword TEXT, score REAL, hashtags TEXT)"
    )

    for keyword, score, hashtag in zip(keywords, score, hashtags):
        c.execute("INSERT INTO keywords VALUES (?, ?, ?)", (keyword, score, hashtag))
    conn.commit()
    conn.close()

    return db_exists


def collect_extract(filename):
    """Collect keywords, scores, hashtags from a file and extract them into a db"""
    keywords = []
    scores = []
    text = read_file(filename)
    extracted_keywords_with_score = extract_keywords(text)
    for key_score in extracted_keywords_with_score:
        keywords.append(key_score[0])
        scores.append(key_score[1])
    
    hashtags = make_hashtags(extracted_keywords_with_score)

    return keywords, scores, hashtags

# collected_extract = collect_extract("text.txt")
# print(collected_extract)

def extract_and_load(filename):
    """Extract keywords from a file and load them inot a db"""
    keywords, scores, hashtags = collect_extract(filename)
    load = load_keywords(keywords, scores, hashtags)
    return load

test = extract_and_load("text.txt")


def query_db(order_by = "score", limit = 10):
    """Query the db and return keywords, hashtags and scores"""

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute(f"SELECT * FROM keywords ORDER BY {order_by} DESC LIMIT {limit}")
    results = c.fetchall()
    conn.close()
    return results


@click.group()
def cli():
    """An ETL cli-app"""


@cli.command('etl')
@click.argument("filename", default = 'text.txt')
def etl(filename):
    """Extract keywords from a file and load them into a database

    Example etl.py etl text.txt
    """

    path_to_db = path.abspath(DATABASE)

    click.echo(
        click.style(
            f"Running ETL to extract keywords from {filename} and load them into a database: {path_to_db}",
            fg='green'
        )
    )
    result = extract_and_load(filename)
    if result:
        click.echo(click.style("Database already exists", fg='yellow'))
    else:
        click.echo(click.style("Database created", fg="green"))

print(etl("text.txt"))