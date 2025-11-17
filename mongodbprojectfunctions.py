from pymongo import MongoClient
from pprint import pprint
from datetime import datetime
import sys
client = MongoClient("mongodb://localhost:27017/")
db = client["Arnab"]
carnival = db["carnival"]

def collect_data():
    #NAME
    while True:
        Name = input("Enter Family Name (e.g., 'SHARMA FAMILY'): ").strip()
        if Name.replace(" ", "").isalpha() and len(Name) > 0:
            break
        else:
            print("Enter valid data (letters and spaces only): ")
    #FAMILY_ID
    while True:
        Family_id = input("Enter 8 DIGIT Family ID(e.g., '12345678'): ")
        if Family_id.isdigit() and len(Family_id) > 0 and len(Family_id) < 9:
            break
        else:
            print("Enter a valid Data: ") 
    #FAMILTY MEMEBERS        
    while True:
        Family_Members = input("Enter no of Family Members(INTEGER VALUE ONLY): ")
        if Family_Members.isdigit():
            break
        else:
            print("Enter a valid Data: ") 
    #TIME ENTRY 
    while True:
        Time_Entry = input("Enter Entry date and time (YYYY-MM-DD HH:MM)(e.g., '2024-12-25 18:30'): ")
        try:
            Time_Entry_dt = datetime.strptime(Time_Entry, "%Y-%m-%d %H:%M")
            break
        except ValueError:
            print("Invalid format! Please use: YYYY-MM-DD HH:MM (e.g., '2024-12-25 18:30')")
    #TIME EXIT  
    while True:
        Time_Exit = input("Enter Exit time (YYYY-MM-DD HH:MM)(e.g., '2024-12-25 18:30'): ")
        try:
            Time_Exit_dt = datetime.strptime(Time_Exit, "%Y-%m-%d %H:%M")
            break
        except ValueError:
            print("Invalid format! Please use: YYYY-MM-DD HH:MM (e.g., '2024-12-25 18:30')")
    #MEALS  
    while True:
        meal_input = input("Enter Meals (comma separated)(e.g., 'Lunch,Dinner,Breakfast'): ")
        Meals = [meal.strip() for meal in meal_input.split(",") if meal.strip()]
        if Meals and all(meal.replace(" ", "").isalpha() for meal in Meals):
            break
        else:
            print("Enter valid meal names (letters only, e.g., 'Lunch,Dinner,Breakfast'): ")           
    #CARNIVAL ADDRESS
    while True:
        Carnival_address = input("Enter Address Block Barcode(e.g., '155-054'): ")
        if Carnival_address.replace("-", "").isdigit() and len(Carnival_address) > 0:
            break
        else:
            print("Enter valid data (letters and spaces only): ")
    #COORDINATES

    coord_x = float(input("Enter coordinate X(e.g., '78.12651'): "))
    coord_y = float(input("Enter coordinate Y(e.g., '78.12651'): "))
    #STREET
    while True:
        street = input("Enter the Street Name(eg '37 Aveneue'/'Gold Street'): ")
        if street.replace(" ", "").isalpha() and len(street) > 0:
            break
        else:
            print("Enter valid data (letters and spaces only): ")        
    #ZIPCODE
    while True:
        zipcode = input("Enter 5-10 Digit Zip Barcode: ")
        if zipcode.replace(" ", "").isdigit() and len(zipcode) > 0 and len(zipcode) < 11:
            break
        else:
            print("Enter valid data (letters and spaces only): ")
    #CARNIVAL NAME
    while True:
        Carnival_name = input("Enter Carnival Name: ")
        if Carnival_name.replace(" ", "").isalpha() and len(zipcode) > 0:
            break
        else:
            print("Enter valid data (letters and spaces only): ")                 
    #OCCASION
    # initialize empty lists so they always exist
    Occasion = []
    events = []
    # OCCASION
    Oc = ["rides", "occasion"]
    while True:
        Occasion = input("Enter Occasion(s) (e.g., 'Rides,Occasion'): ").lower().split(",")
        valid = True
        for item in Occasion:
            item = item.strip()
            if item not in Oc:
                valid = False
                break
        if valid:
            l = len(Occasion)
            for i in range(l):
                n = int(input(f"Enter number of events for {Occasion[i]} ({i+1} of {l}): "))
                for j in range(n):
                    name = input(f"Event {j+1} Name for {Occasion[i]}: ")
                    score = int(input(f"Enter the score of {name} event: "))
                    events.append({
                        "occasion": Occasion[i],
                        "name": name,
                        "score": score
                    })
            print("\nAll Events Recorded:")
            for e in events:
                print(e)
            break
        else:
            print("INVALID DATASET\nEnter Valid DATA.\n")




    return {
            "address": {
                "Carnival_address": Carnival_address,
                "coord": [coord_x, coord_y],
                "street": street,
                "zipcode": zipcode
            },
            "Carnival": Carnival_name,
            "Occasion": Occasion,
            "Concerts": events,
            "Name": Name,
            "Family_id": Family_id,
            "Family_Members": Family_Members,
            "Time_Entry": datetime.strptime(Time_Entry, "%Y-%m-%d %H:%M"),
            "Time_Exit": datetime.strptime(Time_Exit, "%Y-%m-%d %H:%M"),
            "Meals": Meals
    }

def Update_data(sid):
    doc = carnival.find_one({"Family_id": sid})
    if doc:
        print("Family ID found!\n")
        print("PRESS THE RESPECTIVE NUMBER FOR THE FIELD YOU WANT TO UPDATE (Ex: PRESS 1 FOR FAMILY NAME UPDATE)\n")
        print("1:Family Name\n2:SORRY FAMILY ID CANNOT BE CHANGED ONCE ASSIGNED")
        print("3:Family_Members\n4:TIME ENTRY\n5:Time EXIT\n6:MEALS\n7:CARNIVAL ADRRESSS\n8:Coordibate X & Coordibate Y")
        print("9:STreet\n10:ZIPCODE\n11:CARNIVAL NAME\n12:OCCASIONS\n")
        print("PRINT 0 to EXIT")
        cal(sid, doc)
    else: 
        print("Family ID not found!")
        return

def cal(sid, doc):
 while True:
        try:
            a = int(input("\nEnter the Field number to be updated: "))
            if a == 1:
                doc = carnival.find_one({"Family_id": sid})
                prev = doc.get("Name", "N/A")
                print(f"\nPrevious Family Name: {prev}")
                New_Name(sid)
                
            elif a == 3:
                doc = carnival.find_one({"Family_id": sid})
                prev = doc.get("Family_Members", "N/A")
                print(f"\nPrevious FAMILY_MEMBERS: {prev}")
                FAMILY_MEMBERS(sid)
                
            elif a == 4:
                doc = carnival.find_one({"Family_id": sid})
                prev = doc.get("Time_Entry", "N/A")
                print(f"\nPrevious TIME ENTRY: {prev}")
                TIME_ENTRY(sid)
                
            elif a == 5:
                doc = carnival.find_one({"Family_id": sid})
                prev = doc.get("Time_Exit", "N/A")
                print(f"\nPrevious TIME_EXIT: {prev}")
                TIME_EXIT(sid)
                
            elif a == 6:
                doc = carnival.find_one({"Family_id": sid})
                prev = doc.get("Meals", "N/A")
                print(f"\nPrevious MEALS(): {prev}")
                MEALS(sid)

            elif a == 7:
                doc = carnival.find_one({"Family_id": sid})
                prev = doc.get("Carnival_address", "N/A")
                print(f"\nPrevious CARNIVAL_ADDRESS: {prev}")
                CARNIVAL_ADDRESS(sid)
                
            elif a == 8:
                doc = carnival.find_one({"Family_id": sid})
                prev = doc.get("coord", "N/A")
                print(f"\nPrevious COORDINATE(): {prev}")
                COORDINATE(sid)
                
            elif a == 9:
                doc = carnival.find_one({"Family_id": sid})
                prev = doc.get("street", "N/A")
                print(f"\nPrevious New_Street(): {prev}")
                New_Street(sid)
           
            elif a == 10:
                doc = carnival.find_one({"Family_id": sid})
                prev = doc.get("zipcode", "N/A")
                print(f"\nPrevious ZIPCODE(): {prev}")                     
                ZIPCODE(sid)
                
            elif a == 11:
                doc = carnival.find_one({"Family_id": sid})
                prev = doc.get("Carnival", "N/A")
                print(f"\nPrevious CARNIVAL_NAME(): {prev}")                     
                CARNIVAL_NAME(sid)
                
            elif a == 12:
                doc = carnival.find_one({"Family_id": sid})
                prev = doc.get("Occasion", "N/A")
                print(f"\nPrevious Occasion(): {prev}")                     
                Occasion(sid)
                
            elif a == 0:
                print("Program terminated.")
                sys.exit()
            else:
                print("Invalid input! Please enter a valid number.")
        except ValueError:
            print("Please enter a valid numeric choice.")
        

    ####################### Name Update #######################        
def New_Name(sid):
    doc = carnival.find_one({"Family_id": sid})
    while True:
        New_Name = input("Enter Family Name: ")
        if isinstance(New_Name, str):
            carnival.update_one({"Family_id": sid}, {"$set": {"Name": New_Name}})
            print("Name updated successfully!")
            break
        else:
            print("Wrong input type! Please enter a valid string.")

    ####################### Family ID Update #######################    
#def FAMILY_ID():
    #while True:
        #New_Family_ID = input("Enter New Family ID: ")
        #if isinstance(New_Family_ID, str):
            #carnival.update_one({"Family_id": sid}, {"$set": {"Family_id": New_Family_ID}})
            #print("Family ID updated successfully!")
            #break
        #else:
            #print("Wrong input type! Please enter a valid string.")


    ####################### Family Members Update #######################
def FAMILY_MEMBERS(sid):
    doc = carnival.find_one({"Family_id": sid})
    while True:
        New_Family_Members = int(input("Enter New Family Members count: "))
        if isinstance (New_Family_Members, int):  # manual check for int
            New_Family_Members = int(New_Family_Members)
            carnival.update_one({"Family_id": sid}, {"$set": {"Family_Members": New_Family_Members}})
            print("Family Members updated successfully!")
            break
        else:
            print("Wrong input type! Please enter a valid number.")
            
    ####################### Time Entry #######################            
def TIME_ENTRY(sid):
    doc = carnival.find_one({"Family_id": sid})
    while True:
        New_Time_Entry = input("Enter Time_Entry (YYYY-MM-DD HH:MM): ")
        try:
            New_Time_Entry_dt = datetime.strptime(New_Time_Entry, "%Y-%m-%d %H:%M")
            carnival.update_one({"Family_id": sid}, {"$set": {"Time_Entry": New_Time_Entry_dt}})
            print("Time_Entry updated successfully!")
            break
        except ValueError:
            print("Wrong format! Please enter in YYYY-MM-DD HH:MM format.")
            
    ####################### Time Exit #######################
def TIME_EXIT(sid):
    doc = carnival.find_one({"Family_id": sid})
    while True:
        New_Time_Exit = input("Enter Time_Exit (YYYY-MM-DD HH:MM): ")
        try:
            New_Time_Exit_dt = datetime.strptime(New_Time_Exit, "%Y-%m-%d %H:%M")
            carnival.update_one({"Family_id": sid}, {"$set": {"Time_Exit": New_Time_Exit_dt}})
            print("Time_Exit updated successfully!")
            break
        except ValueError:
            print("Wrong format! Please enter in YYYY-MM-DD HH:MM format.")

    ####################### Meals Update #######################
def MEALS(sid):
    doc = carnival.find_one({"Family_id": sid})
    while True:
        New_Meals = input("Enter Meals (comma separated): ").split(",")
        if isinstance(New_Meals, list):
            carnival.update_one({"Family_id": sid}, {"$set": {"Meals": New_Meals}})
            print("Meals updated successfully!")
            break
        else:
            print("Wrong input type! Please enter comma-separated values.")


    ####################### Address Update #######################
def CARNIVAL_ADDRESS(sid):
    doc = carnival.find_one({"Family_id": sid})
    while True:
        New_Carnival_address = input("Enter New Address Block Barcode: ")
        if isinstance(New_Carnival_address, str):
            carnival.update_one({"Family_id": sid}, {"$set": {"address.Carnival_address": New_Carnival_address}})
            print("Carnival_address updated successfully!")
            break
        else:
            print("Wrong input type!")
            
    ####################### COORDINATE #######################
def COORDINATE(sid):
    doc = carnival.find_one({"Family_id": sid})
    while True:
        New_coord_x = input("Enter coordinate X: ")
        New_coord_y = input("Enter coordinate Y: ")
        try:
            New_coord_x = float(New_coord_x)
            New_coord_y = float(New_coord_y)
            carnival.update_one({"Family_id": sid}, {"$set": {"address.coord": [New_coord_x, New_coord_y]}})
            print("Coordinates updated successfully!")
            break
        except ValueError:
            print("Invalid coordinates! Enter numeric values.")

    ####################### STREET #######################
def New_Street(sid):
    doc = carnival.find_one({"Family_id": sid})
    while True:
        New_street = input("Enter Street Name: ")
        if isinstance(New_street, str):
            carnival.update_one({"Family_id": sid}, {"$set": {"address.street": New_street}})
            print("Street updated successfully!")
            break
        else:
            print("Wrong input type!")

    ####################### ZIPCODE #######################
def ZIPCODE(sid):
    doc = carnival.find_one({"Family_id": sid})
    while True:
        New_zipcode = input("Enter Zipcode: ")
        if isinstance(New_zipcode, str):
            carnival.update_one({"Family_id": sid}, {"$set": {"address.zipcode": New_zipcode}})
            print("Zipcode updated successfully!")
            break
        else:
            print("Wrong input type!")
            
    ####################### Carnival #######################
def CARNIVAL_NAME(sid):
    doc = carnival.find_one({"Family_id": sid})
    while True:
        New_Carnival_name = input("Enter Carnival Name: ")
        if isinstance(New_Carnival_name, str):
            carnival.update_one({"Family_id": sid}, {"$set": {"Carnival": New_Carnival_name}})
            print("Carnival Name updated successfully!")
            break
        else:
            print("Wrong input type!")

    ####################### Occasion #######################
def Occasion(sid):
    doc = carnival.find_one({"Family_id": sid})
    while True:
        New_Occasion = input("Enter Occasion: ")
        if isinstance(New_Occasion, str):
            carnival.update_one({"Family_id": sid}, {"$set": {"Occasion": New_Occasion}})
            print("Occasion updated successfully!")
            break
        else:
            print("Wrong input type!")

    ####################### Events / Concerts #######################
    events = []
    n = int(input("Enter the number of events: "))
    for i in range(n):
        New_event_name = input(f"Event {i+1} Name: ")
        while True:
            New_event_score = input(f"Score for {New_event_name}: ")
            if New_event_score.isdigit():
                New_event_score = int(New_event_score)
                break
            else:
                print("Score must be a number!")
        events.append({"name": New_event_name, "score": New_event_score})

    carnival.update_one({"Family_id": sid}, {"$set": {"Concerts": events}})
    print("Events updated successfully!")
    
def delete_data():
    def singledata_delete():
        print("You have chosen Single Data Deletion\nWARNING! THIS PROCESS IS IRREVERSIBLE AND WILL END IN DELETION OF THE ENTIRE DATASET")
        sid = input("Enter the Family ID: ")
        Queryresult = list(carnival.find({"Family_id": sid}))
        
        if Queryresult:
            print("\nData found!")
            pprint(Queryresult[0])
            while True:
                m = input("FINAL WARNING! PRESS 1 FOR DELETION\nPRESS Q FOR QUIT: ").strip().lower()
                
                if m == '1':
                    print("DATA DELETION IMMINENT\n")
                    carnival.delete_one({"Family_id": sid})
                    print("Data has been successfully deleted\n")
                    return True
                elif m == 'q':
                    print("You have chosen to quit program\nProgram terminated\n")
                    return False
                else:
                    print("INVALID INPUT! Please enter 1 or Q")
        else:
            print("Please enter a valid ID - no such ID exists")
            return False

    while True:
        n = input("Press 1 for Single Deletion\nPress 2 for Multiple Deletion\nPress Q to Quit program: ").strip().lower()
        
        if n == '1':
            singledata_delete()
            break
        elif n == '2':
            print("You have chosen multiple data deletion")
            try:
                l = int(input("Enter the number of DATASETS you want to delete: "))
                for i in range(l):
                    print(f"\nDeleting dataset {i+1} of {l}:")
                    singledata_delete()
                break
            except ValueError:
                print("Please enter a valid number!")
        elif n == 'q':
            print("You have chosen to quit program\nProgram terminated")
            break
        else:
            print("INVALID INPUT! Please enter 1, 2, or Q")


