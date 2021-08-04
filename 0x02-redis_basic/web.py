#!/usr/bin/env python3
"""Defines a method that implements an expiring web cache and tracker."""

import requests
import redis


def get_page(url: str) -> str:
    """ obtains the HTML content of a particular URL and returns it."""
    r = redis.Redis()
    count = 0
    r.set("cached:{}".format(url), count)
    response = requests.get(url)
    r.incr("count:{}".format(url))
    r.setex("cached:{}".format(url), 10, r.get("cached:{}".format(url)))
    return response.txt


if __name__ == "__main__":
    get_page("http://slowwly.robertomurray.co.uk")
