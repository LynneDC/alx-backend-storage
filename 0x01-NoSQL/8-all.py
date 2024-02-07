#!/usr/bin/env python3
"""
function that list all docs in a collection
return an empty list if no docs
mongo_collection: pymongo collection object
"""
def list_all(mongo_collection):
    return list(mongo_collection.find())