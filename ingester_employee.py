import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["employee_competencies_db"]
collection = db["employee_competencies_data"]


# Function to insert data into MongoDB
def insert_into_mongodb(data):
    collection.insert_one(data)


# Read CSV file and insert into MongoDB
csv_data = pd.read_csv("employee_competencies.csv", sep="|")
for _, row in csv_data.iterrows():
    data = {
        "employee": row["employee"],
        "payment_issue": row["payment_issue"],
        "create_account": row["create_account"],
        "contact_customer_service": row["contact_customer_service"],
        "get_invoice": row["get_invoice"],
        "track_order": row["track_order"],
        "get_refund": row["get_refund"],
        "contact_human_agent": row["contact_human_agent"],
        "recover_password": row["recover_password"],
        "change_order": row["change_order"],
        "delete_account": row["delete_account"],
        "complaint": row["complaint"],
        "check_invoices": row["check_invoices"],
        "review": row["review"],
        "check_refund_policy": row["check_refund_policy"],
        "delivery_options": row["delivery_options"],
        "check_cancellation_fee": row["check_cancellation_fee"],
        "track_refund": row["track_refund"],
        "check_payment_methods": row["check_payment_methods"],
        "change_shipping_address": row["change_shipping_address"],
        "newsletter_subscription": row["newsletter_subscription"],
        "delivery_period": row["delivery_period"],
        "edit_account": row["edit_account"],
        "registration_problems": row["registration_problems"],
        "switch_account": row["switch_account"],
        "set_up_shipping_address": row["set_up_shipping_address"],
        "place_order": row["place_order"],
        "cancel_order": row["cancel_order"],
        "check_invoice": row["check_invoice"]
    }
    insert_into_mongodb(data)
