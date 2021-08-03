#!/usr/bin/env python3

"""Defines a function that updates a document in a collection."""

def update_topics(mongo_collection, name, topics):
    """Updates a mongodb document"""
    mongo_collection.update_many({"name": name}, {"$set":{"topics":topics}})
