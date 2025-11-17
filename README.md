 MONGODB-with-PYTHON-Connectivity
A Python–MongoDB CLI app that performs full CRUD operations on carnival visitor data. Supports inserting new records, updating fields, deleting entries, and validating user input. Demonstrates MongoDB connectivity, nested document handling, and interactive terminal-based data management.
 🎡 Carnival Attendance Management System (MongoDB + Python)

A Python-based database management project that demonstrates full **CRUD operations** (Create, Read, Update, Delete) using **MongoDB** via `pymongo`.  
The system manages carnival visitor information including families, event participation, timings, meals, ride scores, and more.

This project is ideal for learning:
- MongoDB NoSQL database design  
- Python–MongoDB connectivity  
- CRUD operations  
- Input validation  
- Interactive CLI application development  

---

 Features

 1. **Create / Insert Data**
- Insert a new family record into the carnival collection  
- Captures:
  - Family name  
  - Family ID  
  - Member count  
  - Entry & exit timestamps  
  - Meals  
  - Address details (block ID, street, zipcode, coordinates)  
  - Carnival name  
  - Occasions (rides, concerts, etc.)  
  - Event names + scores  

All inputs include **validation** to prevent incorrect data entry.

---

 ✔ 2. **Read Data**
- Fetch and display a document by **Family_id**
- Outputs complete structured data using `pprint`

---

 ✔ 3. **Update Data**
You can update almost **every field** in an existing record:

- Family Name  
- Member Count  
- Entry / Exit Time  
- Meals  
- Address (street, zipcode, coordinates, barcode)  
- Carnival Name  
- Occasion list  
- Event list + scores  

Each option displays the **previous value** and confirms updates.

---

 ✔ 4. **Delete Data**
- Delete **one** document  
- Or delete **multiple** documents  
- Includes strong safety warnings before deletion  
- Designed to prevent accidental data loss

---

 🗂 Project Structure


---

 🛠 Technologies Used

- **Python 3.x**
- **MongoDB**
- **PyMongo**
- **Datetime library** (timestamp handling)
- **PrettyPrint (pprint)** for outputs

---

 Installation & Setup

Install Dependencies
```bash
pip install pymongo
