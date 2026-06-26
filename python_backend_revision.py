# ==========================================
# Python Backend Revision
# Author: Niharika
# Topics:
# - Lists
# - Dictionaries
# - Functions
# - Loops
# - Backend Logic
# ==========================================


# ==========================================
# USERS
# ==========================================

users = [
    {"name": "Rahul", "age": 20},
    {"name": "Niharika", "age": 19},
    {"name": "Aman", "age": 17}
]

print("\n===== USERS =====")

# Print all user names
print("\nAll Users:")
for user in users:
    print(user["name"])

# Print adult users
print("\nAdult Users:")
for user in users:
    if user["age"] >= 18:
        print(user["name"])

# Create uppercase user list
upper_users = []

for user in users:
    upper_users.append(user["name"].upper())

print("\nUppercase Users:")
print(upper_users)


# ==========================================
# STUDENT DICTIONARY
# ==========================================

student = {
    "name": "Niharika",
    "marks": 95,
    "city": "Delhi"
}

print("\n===== STUDENT =====")
print("Name :", student["name"])
print("Marks:", student["marks"])


# ==========================================
# STUDENTS
# ==========================================

students = [
    {"name": "Rahul", "marks": 78},
    {"name": "Niharika", "marks": 95},
    {"name": "Aman", "marks": 62},
    {"name": "Riya", "marks": 88}
]

print("\n===== STUDENTS =====")

print("\nStudent Names:")
for student in students:
    print(student["name"])

print("\nStudents with Marks >= 80")
for student in students:
    if student["marks"] >= 80:
        print(student["name"])

student_names = []

for student in students:
    student_names.append(student["name"])

print("\nStudent Name List:")
print(student_names)


# ==========================================
# PRODUCTS
# ==========================================

products = [
    {"name": "Laptop", "price": 60000},
    {"name": "Mouse", "price": 800},
    {"name": "Keyboard", "price": 1500},
    {"name": "Monitor", "price": 12000}
]

print("\n===== PRODUCTS =====")

print("\nProduct Names:")
for product in products:
    print(product["name"])

print("\nProducts Price > 5000")
for product in products:
    if product["price"] > 5000:
        print(product["name"])

product_prices = []

for product in products:
    product_prices.append(product["price"])

print("\nPrice List:")
print(product_prices)

total_price = 0

for product in products:
    total_price += product["price"]

print("\nTotal Price:", total_price)


# ==========================================
# ORDERS
# ==========================================

orders = [
    {"id": 1, "amount": 1200},
    {"id": 2, "amount": 800},
    {"id": 3, "amount": 2500}
]

print("\n===== ORDERS =====")

total = 0

for order in orders:
    total += order["amount"]

print("Total Amount:", total)

print("\nOrders Above 1000")

for order in orders:
    if order["amount"] > 1000:
        print(order["id"])


# ==========================================
# EMPLOYEES
# ==========================================

employees = [
    {"name": "Aman", "department": "HR", "salary": 30000},
    {"name": "Rahul", "department": "IT", "salary": 55000},
    {"name": "Niharika", "department": "IT", "salary": 70000},
    {"name": "Riya", "department": "HR", "salary": 45000}
]

print("\n===== EMPLOYEES =====")

print("\nIT Employees:")

for employee in employees:
    if employee["department"] == "IT":
        print(employee["name"])

highest_salary = employees[0]["salary"]

for employee in employees:
    if employee["salary"] > highest_salary:
        highest_salary = employee["salary"]

print("\nHighest Salary:", highest_salary)

total_salary = 0

for employee in employees:
    total_salary += employee["salary"]

average_salary = total_salary / len(employees)

print("Average Salary:", round(average_salary, 2))

it_employee_names = []

for employee in employees:
    if employee["department"] == "IT":
        it_employee_names.append(employee["name"])

print("IT Employee List:")
print(it_employee_names)


# ==========================================
# FUNCTIONS
# ==========================================

print("\n===== FUNCTIONS =====")


def greet(name):
    print("Hello,", name)


greet("Niharika")
greet("Rahul")


def square(num):
    return num * num


print("\nSquare of 5:", square(5))


def is_even(num):
    return num % 2 == 0


print("10 is Even:", is_even(10))
print("7 is Even :", is_even(7))


def full_name(first, last):
    return first + " " + last


print(full_name("Niharika", "Sharma"))


# ==========================================
# LIST PRACTICE
# ==========================================

numbers = [5, 12, 7, 18, 25, 30]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("\n===== LIST PRACTICE =====")
print(even_numbers)


names = ["rahul", "aman", "niharika", "rohit"]

capitalized_names = []

for name in names:
    capitalized_names.append(name.capitalize())

print(capitalized_names)


print("\n===== END OF PYTHON BACKEND REVISION =====")
