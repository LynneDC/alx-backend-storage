#!/usr/bin/env python3
"""
improv 12-log_stats.py by adding top 10 of the most IPs
in the collection nginx of db logs
IPs top must be sorted
"""
from pymongo import MongoClient


def log_stats_new_version(mongo_collection):
    total_logs, methods_counts, status_check_count = log_stats(mongo_collection)
    top_ips = list(mongo_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]))
    return total_logs, methods_counts, status_check_count, top_ips