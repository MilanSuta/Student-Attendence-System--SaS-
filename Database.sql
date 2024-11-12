CREATE DATABASE student_attendance_system;

USE student_attendance_system;

-- Students table
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(255),
    student_email VARCHAR(255),
    student_password VARCHAR(255)
);

-- Courses table
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(255),
    course_code VARCHAR(100)
);

-- Classes table
CREATE TABLE classes (
    class_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT,
    class_date DATE,
    class_time TIME,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Attendance table
CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    class_id INT,
    attendance_status VARCHAR(50),
    excuse_reason TEXT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (class_id) REFERENCES classes(class_id)
);
