#!/usr/bin/env python3
"""
function that inserts a new doc in a collection based on kwargs
mongo_collection: pymongo collection object
return the new _id
"""
def insert_school(mongo_collection, **kwargs):
    return mongo_collection.insert_one(kwargs).inserted_id