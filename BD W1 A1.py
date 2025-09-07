from pymongo import MongoClient
import json

# Create a MongoDB client
client = MongoClient()

# to create the StudentDB database
db = client["StudentDB"]

# to create the students collection
students = db["students"]

# to clear existing records 
students.delete_many({})

# inserting data 
students_data = [
    {"Roll": 1, "Name": "Arjun Nair", "Course": "Math", "Marks": 85, "City": "Kochi", "EmailID": "arjun.nair@gmail.com"},
    {"Roll": 2, "Name": "Anjali Menon", "Course": "Physics", "Marks": 78, "City": "Trivandrum", "EmailID": "anjali.menon@gmail.com"},
    {"Roll": 3, "Name": "Rakesh Pillai", "Course": "Chemistry", "Marks": 92, "City": "Kozhikode", "EmailID": "rakesh.pillai@gmail.com"},
    {"Roll": 4, "Name": "Meera Nambiar", "Course": "Math", "Marks": 65, "City": "Thrissur", "EmailID": "meera.nambiar@gmail.com"},
    {"Roll": 5, "Name": "Gautham Kurup", "Course": "Biology", "Marks": 88, "City": "Alappuzha", "EmailID": "gautham.kurup@gmail.com"},
    {"Roll": 6, "Name": "Divya Warrier", "Course": "Math", "Marks": 72, "City": "Kollam", "EmailID": "divya.warrier@gmail.com"},
    {"Roll": 7, "Name": "Vishnu Panicker", "Course": "Physics", "Marks": 95, "City": "Kochi", "EmailID": "vishnu.panicker@gmail.com"},
    {"Roll": 8, "Name": "Lekshmi Nair", "Course": "Biology", "Marks": 56, "City": "Palakkad", "EmailID": "lekshmi.nair@gmail.com"},
    {"Roll": 9, "Name": "Sudeep Varma", "Course": "Chemistry", "Marks": 34, "City": "Kottayam", "EmailID": "sudeep.varma@gmail.com"},
    {"Roll": 10, "Name": "Arya Krishnan", "Course": "Physics", "Marks": 68, "City": "Kozhikode", "EmailID": "arya.krishnan@gmail.com"},
    {"Roll": 11, "Name": "Nikhil Ramesh", "Course": "Math", "Marks": 82, "City": "Kannur", "EmailID": "nikhil.ramesh@gmail.com"},
    {"Roll": 12, "Name": "Revathi Menon", "Course": "Biology", "Marks": 45, "City": "Trivandrum", "EmailID": "revathi.menon@gmail.com"},
    {"Roll": 13, "Name": "Ajay Kumar", "Course": "Chemistry", "Marks": 77, "City": "Thrissur", "EmailID": "ajay.kumar@gmail.com"},
    {"Roll": 14, "Name": "Sandhya Pillai", "Course": "Math", "Marks": 91, "City": "Alappuzha", "EmailID": "sandhya.pillai@gmail.com"},
    {"Roll": 15, "Name": "Rohit Nair", "Course": "Physics", "Marks": 39, "City": "Kollam", "EmailID": "rohit.nair@gmail.com"}
]

students.insert_many(students_data)
print("Inserted", len(students_data), "student records.")



# to display all records of students
for s in students.find({}):
    print(f"\nStudent details for roll number {s['Roll']}:")
    print(s)


# query to fetch all students enrolled in specific course
course = "Math"
print(f"\nStudents enrolled in {course}:")
for s in students.find({"Course": course}):
    print(s["Roll"], s["Name"], s["Course"])

# query to find and fetch students with marks greater than 75
print("\nStudents with marks > 75:")
for s in students.find({"Marks": {"$gt": 75}}):
    print(s["Roll"], s["Name"], s["Course"], s["Marks"])


# query to retrieve students from a specific city
city = "Kochi"
print(f"\nStudents from city = {city}:")
for s in students.find({"City": city}):
    print(s["Roll"], s["Name"], s["City"])



# updating email of a student with a specific roll number
students.update_one({"Roll": 11}, {"$set": {"EmailID": "nikhil.ramesh.new@gmail.com"}})
print("\nUpdated email for roll number 11.")

# displaying updated record of the student
for s in students.find({"Roll": 11}):
    print(f"\nStudent details for roll number {s['Roll']}:")
    print(s)


# displaying marks of students enrolled in a specific course
course = "Physics"
print("\nStudents marks before update:")
for s in students.find({"Course": course}):
    print(s["Roll"], s["Name"], s["Course"], s["Marks"])

# to increase the marks of all students in that specific course by 10
students.update_many({"Course": course}, {"$inc": {"Marks": 10}})
print(f"Added +10 marks to students in {course}.")

# displaying updated records of students in that course
print(f"\nUpdated student details in {course}:")
for s in students.find({"Course": course}):
    print(s["Roll"], s["Name"], s["Course"], s["Marks"])

# to display students with marks less than 40
print("\nStudents with marks < 40:")
for s in students.find({"Marks": {"$lt": 40}}):
    print(s["Roll"], s["Name"], s["Course"], s["Marks"])

# deleting students record with marks less than 40
students.delete_many({"Marks": {"$lt": 40}})
print("Deleted students with marks < 40.")

#  deleting of records
print("\nVerifying deletion of students with marks < 40:")
for s in students.find({"Marks": {"$lt": 40}}):
    print(s)



# aggregate to count the number of students per course while sorting in ascending order
print("\nNumber of students per course:")
count = [{"$group": {"_id": "$Course", "count": {"$sum": 1}}}, {"$sort": {"count": 1}}]
for r in students.aggregate(count):
    print(r)


# aggregate to calculate average marks per course while sorting in ascending order
print("\nStudents average marks per course:")
avg = [{"$group": {"_id": "$Course", "avg_marks": {"$avg": "$Marks"}}}, {"$sort": {"avg_marks": 1}}]
for s in students.aggregate(avg):
    print(s)


print("\nTop 3 students by marks:")
for s in students.find({}).sort("Marks", -1).limit(3):
    print(s["Roll"], s["Name"], s["Course"], s["Marks"])


# query to display all students sorted by marks in descending order
print("\nAll students sorted by marks in descending order:")
for s in students.find({}).sort("Marks", -1):
    print(f"\nStudent details for roll number {s['Roll']}:")
    print(s)



# fetching all records excluding the MongoDB generated _id field converting to a list of dictionaries
docs = list(students.find({}, {"_id": 0}))

with open("students.json", "w", encoding="utf-8") as f:
    json.dump(docs, f, ensure_ascii=False, indent=2)
print("Exported to students.json")

