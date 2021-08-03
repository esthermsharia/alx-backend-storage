#!/usr/bin/env python3
"""Defines a function that inserts a new document in
   a collection based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs"""
    return mongo_collection.insert(kwargs)
