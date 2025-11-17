from pymongo import MongoClient
from pprint import pprint
import sys
from datetime import datetime
from mongodbprojectfunctions import collect_data, Update_data, delete_data

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["Arnab"]
carnival = db["carnival"]

# Take Family_id from user
sid = input("Enter Family_id: ")

# Query for the document
Queryresult = list(carnival.find({"Family_id": sid}))

if Queryresult:
    print("\n Data found!")
    pprint(Queryresult[0])

    # ongoing loop until user quits
    while True:
        print("\nChoose among the options:")
        print("Press 1 to Insert Data")
        print("Press 2 to Update existing data")
        print("Press 3 to Delete existing Data")
        print("Press Q to Quit program\n")
        c1 = input("Enter Your Choice: ").strip().lower()

        if c1 == "1":
            print("You have chosen to Insert New Data")
            doc = collect_data()
            result = carnival.insert_one(doc)
            print("Inserted single document with _id:", result.inserted_id)

        elif c1 == "2":
            print("You have chosen to Update Existing Data")
            Update_data(sid)

        elif c1 == "3":
            print("You have chosen to Delete Existing Data")
            delete_data()

        elif c1 == "q":
            print("PROGRAM TERMINATED")
            sys.exit()

        else:
            print("INVALID CHOICE. Please try again.\n")

else:
    print(" Data not found / INVALID DATA.\n")
    c = input("Press\nY to Proceed:\nN to Terminate:\n").strip().lower()
    if c == "n":
        print("PROGRAM TERMINATED")
        sys.exit()
    elif c == "y":
        while True:
            print("\nChoose among the options:")
            print("Press 1 to Insert Data")
            print("Press 2 to Update existing data")
            print("Press 3 to Delete existing Data")
            print("Press Q to Quit program\n")
            c1 = input("Enter Your Choice: ").strip().lower()

            if c1 == "1":
                print("You have chosen to Insert New Data")
                doc = collect_data()
                result = carnival.insert_one(doc)
                print("Inserted single document with _id:", result.inserted_id)

            elif c1 == "2":
                print("You have chosen to Update Existing Data")
                sid = input("Enter the family ID: ")
                Update_data(sid)

            elif c1 == "3":
                print("You have chosen to Delete Existing Data")
                delete_data()

            elif c1 == "q":
                print("PROGRAM TERMINATED")
                sys.exit()

            else:
                print("INVALID CHOICE. Please try again.\n")
    else:
        print("INVALID INPUT. PROGRAM TERMINATED\n")
