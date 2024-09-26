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
