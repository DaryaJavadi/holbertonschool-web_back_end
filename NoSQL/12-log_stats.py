#!/usr/bin/env python3
"""Module for logging stats"""
from pymongo import MongoClient  

# Connect to MongoDB  
client = MongoClient()  
db = client['logs']  
collection = db['nginx']  

# Get total number of documents  
total_docs = collection.count_documents({})  

# Count documents by method  
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]  
method_counts = {m: collection.count_documents({"method": m}) for m in methods}  

# Count documents with method GET and path /status  
status_check = collection.count_documents({"method": "GET", "path": "/status"})  

# Print results  
print(f"{total_docs} logs")  
print("Methods:")  
for m in methods:  
    print(f"\tmethod {m}: {method_counts[m]}")  
print(f"{status_check} status check")
