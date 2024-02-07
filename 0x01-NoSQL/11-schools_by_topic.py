#!/usr/bin/env python3
"""
function that retrun a list od school with specif topics
mongo_collection: pymongo collection object
topics: topic searched
"""
def school_by_topic(mongo_collection, topics):
    return list(mongo_collection.find({'topics': {'$in': topics}}))