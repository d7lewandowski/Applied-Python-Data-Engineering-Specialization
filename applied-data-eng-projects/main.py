#!/usr/bin/env python3

"""
cli/app  extracting keywords and keyphrases by KeyBERT
source: https://github.com/MaartenGr/KeyBERT
"""

import yake
import click
from keybert import KeyBERT

# create funcation that reads a file
def read_file(filename: str):
    with open(filename, encoding='utf-8') as f:
        return f.read()

# def extract keywords
def extract_keywords(text):

    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(text)
    return keywords

# create a funcation that makes hash tags
def make_hashtags(keywords):

    hashtags = []
    for keyword in keywords:
        hashtags.append("#" + keyword[0])
    return hashtags

# create a function that make a limit for hashtags
def limits_keywords(keywords, max):
    keywords_limit = keywords[:max]
    return keywords_limit


@click.group()
def cli():
    """A cli for app"""

@cli.command("extract")
@click.argument("filename", default = "text.txt")
def extract(filename):
    """Extract keywords from file"""
    text = read_file(filename)
    keywords = extract_keywords(text)
    click.echo(keywords)

@cli.command("hashtags")
@click.argument("filename", default = "text.txt")
def hashtags(filename):
    """Extract hashtags from file"""
    text = read_file(filename)
    keywords = extract_keywords(text)
    hashtags = make_hashtags(keywords)
    click.echo(hashtags)


@cli.command("limits")
@click.argument("filename", default="text.txt")
@click.option('--max', '-l', default = 3)
def limitscli(filename, max):
    """Extract keywords from a file and make hashtags, limited by value"""
    text = read_file(filename)
    keywords = extract_keywords(text)
    hashtags = make_hashtags(keywords)
    limits = limits_keywords(hashtags, max)

    click.echo(limits)








if __name__ == "__main__":
    cli()

