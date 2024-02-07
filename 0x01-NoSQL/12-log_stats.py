#!/usr/bin/env python3
"""
script that provide stas about NGINX logs stored in mongoDB
DATABSE: logs
COLLECTION: nginx
display:
    first line: x logs where x is number of doc in collection
    last line: methods:
    5 line with number of doc 
    methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']
    one line with number of docs with:
    - method GET
    - path=/status
"""
from pymongo import MongoClient
def log_status():
    client = MongoClient('mongodb://localhost:27017/')
    logs_collection = client.logs.nginx

    total_logs = logs_collection.count_documents({})
    print(f'{total_logs} logs')

    methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']
    for method in methods:
        count = logs_collection.count_documents({'method': method})
        print(f"   method {method}: {count}")

    status_check_count = logs_collection.count_documents({"method": "GET", 'path': '/status'})
    print(f"{status_check_count} status check")


if __name__ == '__main__':
    log_status()