import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["user_requests_db"]
collection = db["user_requests_data"]


# Function to insert data into MongoDB
def insert_into_mongodb(data):
    collection.insert_one(data)


# Read CSV file and insert into MongoDB
csv_data = pd.read_csv("user_requests.csv", sep="|")
for _, row in csv_data.iterrows():
    data = {
        "content": row["content"],
        "competent": row["competent"],
        "priority": row["priority"]
    }
    insert_into_mongodb(data)

