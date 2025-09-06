#  Student Database Management with MongoDB  

##  Overview  
This project demonstrates how **MongoDB** can be used to manage student records efficiently.  
It simulates a **Student Information System**, where details such as Roll Number, Name, Course, Marks, City, and Email are stored, queried, updated, and analyzed using **Python with PyMongo**.  

The project also showcases CRUD operations, aggregation pipelines, and JSON export, making it a complete learning module for database management with MongoDB.  

---

##  Features Implemented  

### **1. Database & Dataset Creation**  
- Created a database: `StudentDB`.  
- Created a collection: `students`.  
- Inserted **15 student records** with Indian Malayali names.  

### **2. Basic Queries (Read Operations)**  
- Displayed all student records.  
- Retrieved students enrolled in a **specific course**.  
- Filtered students with **marks greater than 75**.  
- Retrieved students from a **particular city**.  

### **3. Update & Delete Operations**  
- Updated the **email ID** of a student by Roll Number.  
- Increased marks by **+10** for all students in a specific course.  
- Deleted students who scored **below 40 marks**.  

### **4. Aggregation & Analysis**  
- Counted the number of students per course.  
- Calculated the **average marks** per course.  
- Retrieved the **top 3 students** with the highest marks.  
- Sorted all students by marks in **descending order**.  

### **5. Export to JSON**  
- Exported the `students` collection into a file named **`students.json`**.  
- This file can be reused for backups, sharing, or integration.  

---

##  How It Works  
The project uses **Python + PyMongo** to interact with MongoDB:  

- **MongoClient()** → connects Python with MongoDB running on `localhost:27017`.  
- **insert_many()** → inserts multiple student records into the collection.  
- **find()** → fetches records with conditions (`marks > 75`, `course = Math`, `city = Kochi`).  
- **update_one() / update_many()** → updates single or multiple student records.  
- **delete_many()** → removes students meeting specific conditions.  
- **aggregate()** → performs analytics like grouping and averaging.  
- **json.dump()** → exports MongoDB documents into `students.json`.  

---

##  Technologies Used  
- **MongoDB** (NoSQL database)  
- **Python**  
- **PyMongo** (MongoDB client for Python)  
- **JSON** (data export format)  

---

## Example Insights  
- **Top performer**: Identified using sorting queries.  
- **Best performing course**: Calculated via average marks per course.  
- **Failed students**: Filtered and deleted (marks < 40).  

---

## Exported File  
- The dataset is exported to **`students.json`** automatically after running the script.  
- The JSON file contains all student records (excluding MongoDB’s `_id` field).  

---

