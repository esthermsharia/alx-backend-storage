#!/usr/bin/env python3
"""Defines a function that lists all documents in a mongo_db."""

from typing import List


def list_all(mongo_collection) -> List:
    """Lists all the documents in a given collection"""
    if mongo_collection is not None:
        return list(mongo_collection.find())
    return []
