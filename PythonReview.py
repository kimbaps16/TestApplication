# Challenge 1: JSON File Reader
# Write a Python program that reads a JSON file containing a list of student records (name, age, grades).
# Extract and print the names and average grade for each student.
import json
import mysql.connector
import matplotlib.pyplot as plt

data_json = '''
{
    "students": [
        {"name": "Mizi", "age": 22, "grades": [90, 70]},
        {"name": "Sua", "age": 23, "grades": [97, 95]},
        {"name": "Ivan", "age": 22, "grades": [98, 94], 
        {"name": "Till", "age": 21, "grades": [82, 75]}
        
    ]
}
'''
data = json.loads(data_json)

def challenge_json():
    print("\n(Challenge 1) JSON Student Averages:")
    for student in data['students']:
        avg = sum(student['grades']) / len(student['grades'])
        print(f"{student['name']}: {avg:.2f}")

# Challenge 2: Plotting with matplotlib
# Using matplotlib, plot a line chart of students' average grades from the JSON data.
# Label axes and add a title.

def challenge_plotting():
    print("\n(Challenge 2) Plotting Student Averages:")
    names = [student['name'] for student in data['students']]
    averages = [sum(student['grades'])/len(student['grades']) for student in data['students']]
    plt.title("Student Average Grades")
    plt.bar(names, averages, color='#000000')
    plt.xlabel("Name")
    plt.ylabel("Average Grade")
    plt.grid(True)
    plt.show()

# Challenge 3: Class and Inheritance
# Create a base class Shape with a method area().
# Create 2 subclasses: Rectangle and Circle, each overriding area() appropriately.
# Instantiate objects and print their areas.

def challenge_class_inheritance():
    print("\n(Challenge 3) Class & Inheritance:")
    class Shape:
        def area(self):
            return 0;
    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height
        def area(self):
            return self.width * self.height
    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius
        def area(self):
            return 3.14 * (self.radius ** 2)
    # Instantiate
    rect = Rectangle(5, 10)
    circ = Circle(8)
    print("Rectangle Area:", rect.area())
    print("Circle Area:", circ.area())
    return [rect, circ]


# Challenge 4: Demonstrate Polymorphism
# Write a function that accepts a list of Shape objects.
# Call the area() method on each and print the results (showing polymorphism).

def challenge_polymorphism(shapes):
    # This function demonstrates polymorphism.
    # It accepts a list of Shape objects (which may be instances of Rectangle, Circle, etc.)
    print("\n(Challenge 4) Polymorphism Example:")
    for shape in shapes:
        # For each shape, call the .area() method.
        # Due to polymorphism, Python will call the correct overridden 'area()'
        # depending on the actual object type (Rectangle or Circle).
        # The type() function shows the actual class name for demonstration.
        print(type(shape).__name__, "area:", shape.area())

# Challenge 5: Simple Database Partial (SQLite)
# Create a MySQL database storing student records.
# Write Python functions to add new students and retrieve all students.
# Display results.

def challenge_mysql():
    print("\n(Challenge 5) MySQL DB Example:")
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Pwd@1234',
        'database': 'mydb'
    }
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS student (name VARCHAR(100), age INT, avg_grade FLOAT)")
    for student in data['students']:
        avg = sum(student['grades']) / len(student['grades'])
        cursor.execute(
            "INSERT INTO student (name, age, avg_grade) VALUES (%s, %s, %s)",
            (student["name"], student["age"], avg)
        )
    conn.commit()
    cursor.execute("SELECT * FROM student")
    students_db = cursor.fetchall()
    for row in students_db:
        print(row)
    conn.close()

# Challenge 6: Integration Challenge
# Combine previous challenges:
# Read student data from JSON.
# Store it in the SQLite database.
# Create Student objects.
# Plot their average grades using matplotlib.

# def challenge_integration():
#     print("\n(Challenge 6) Integration Challenge:")
#     challenge_json()
#     challenge_mysql()
#     challenge_plotting()

if __name__ == "__main__":
    challenge_json()
    challenge_plotting()
    shapes = challenge_class_inheritance()
    challenge_polymorphism(shapes)
    challenge_mysql()
    # challenge_integration()