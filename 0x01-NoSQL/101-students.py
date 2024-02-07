#!/usr/bin/env python3
"""
function that returns all students by average score
mongo_collection: pymongo collection object
top must be ordered
average score must be part of the each item return 
"""
def top_students(mongo_collection):
    students = list(mongo_collection.find())
    for student in students:
        scores = [topic['score'] for topic in student['topics']]
        student['averageScore'] = sum(scores) / len(scores)
    return sorted(students, key=lambda x: x['averageScore'], reverse=True)
