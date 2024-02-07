#!/usr/bin/env python3
"""
function that chnages all topics of school doc based on:
    - the school name
mongo_collection: pymongo collection object
name: school name to update
topics: list of topics to update
"""
def update_topics(mongo_collection, name, topics):
    mongo_collection.update_one(
        {'name': name},
        {'$set': {'topics': topics}}
    )