#!/usr/bin/env python3
"""Defines a function that returns
   the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """Finds and returns a list of schools in a document, that contain
    specific topics.
    """
    return mongo_collection.find({"topics": topic})
