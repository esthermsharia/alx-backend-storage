#!/usr/bin/env python3
"""Defines a class that stores an instance of redis client
   as a private variable and stores data in redis.
"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    def __init__(self):
        """Instanciates a redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores the data in redis"""
        r_key = str(uuid4())
        self._redis.set(r_key, data)
        return r_key
