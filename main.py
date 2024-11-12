import mysql.connector
from mysql.connector import Error

# Connect to MySQL
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='student_attendance_system',
            user='root',  # Change to your MySQL username
            password='password'  # Change to your MySQL password
        )
        if connection.is_connected():
            print("Connected to MySQL")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to add a student
def add_student(connection, name, email, password):
    cursor = connection.cursor()
    query = "INSERT INTO students (student_name, student_email, student_password) VALUES (%s, %s, %s)"
    values = (name, email, password)
    cursor.execute(query, values)
    connection.commit()
    print(f"Student {name} added successfully!")

# Function to add a course
def add_course(connection, course_name, course_code):
    cursor = connection.cursor()
    query = "INSERT INTO courses (course_name, course_code) VALUES (%s, %s)"
    values = (course_name, course_code)
    cursor.execute(query, values)
    connection.commit()
    print(f"Course {course_name} added successfully!")

# Function to add a class
def add_class(connection, course_id, class_date, class_time):
    cursor = connection.cursor()
    query = "INSERT INTO classes (course_id, class_date, class_time) VALUES (%s, %s, %s)"
    values = (course_id, class_date, class_time)
    cursor.execute(query, values)
    connection.commit()
    print("Class added successfully!")

# Function to mark attendance
def mark_attendance(connection, student_id, class_id, status, reason=""):
    cursor = connection.cursor()
    query = "INSERT INTO attendance (student_id, class_id, attendance_status, excuse_reason) VALUES (%s, %s, %s, %s)"
    values = (student_id, class_id, status, reason)
    cursor.execute(query, values)
    connection.commit()
    print(f"Attendance marked for student {student_id} in class {class_id}.")

# Function to generate attendance report
def generate_report(connection, class_id):
    cursor = connection.cursor()
    query = "SELECT s.student_name, a.attendance_status, a.excuse_reason FROM attendance a JOIN students s ON a.student_id = s.student_id WHERE a.class_id = %s"
    cursor.execute(query, (class_id,))
    result = cursor.fetchall()
    for row in result:
        print(f"Student: {row[0]}, Status: {row[1]}, Excuse: {row[2]}")

# Main function to demonstrate basic functionalities
def main():
    connection = create_connection()
    if not connection:
        return
    
    # Example operations
    add_student(connection, 'John Doe', 'john@example.com', 'password123')
    add_course(connection, 'Python Programming', 'CS101')
    add_class(connection, 1, '2024-11-12', '10:00:00')
    mark_attendance(connection, 1, 1, 'Present')
    generate_report(connection, 1)

if __name__ == "__main__":
    main()
