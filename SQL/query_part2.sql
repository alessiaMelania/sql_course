-- Create Courses Table
CREATE TABLE Courses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  description TEXT
);

-- Create Enrollments Table
CREATE TABLE Enrollments (
  student_id INTEGER,
  course_id INTEGER,
  enrollment_date DATE,
  PRIMARY KEY (student_id, course_id),
  FOREIGN KEY (student_id) REFERENCES Students(id),
  FOREIGN KEY (course_id) REFERENCES Courses(id)
);

-- Insert some Data


-- Selecting data
SELECT * FROM Students;

SELECT name, email FROM Students;

-- Filtering Data with WHERE
SELECT * FROM Students
WHERE age > 18;

-- Join & Count & Goup by
-- Find all students who are enrolled in at least one course.
SELECT Students.name, Enrollments.enrollment_date
FROM Students
INNER JOIN Enrollments ON Students.id = Enrollments.student_id;

-- How Many Courses is Each Student Enrolled In?
SELECT Students.name, COUNT(Enrollments.course_id) AS course_count
FROM Students
INNER JOIN Enrollments ON Students.id = Enrollments.student_id
GROUP BY Students.name;

-- Shows only students who are enrolled in more than one course

SELECT Students.name, COUNT(Enrollments.course_id) AS course_count
FROM Students
INNER JOIN Enrollments ON Students.id = Enrollments.student_id
GROUP BY Students.name
HAVING COUNT(Enrollments.course_id) > 1;

-- Find all courses that have at least one student enrolled
SELECT Courses.title, Enrollments.enrollment_date
FROM Courses
INNER JOIN Enrollments ON Courses.id = Enrollments.course_id;

--  How Many Students per Course?
SELECT Courses.title, COUNT(Enrollments.student_id) AS student_count
FROM Courses
INNER JOIN Enrollments ON Courses.id = Enrollments.course_id
GROUP BY Courses.title;



-- Show each student, the course they're enrolled in, and when they enrolled.

SELECT Students.name, Courses.title, Enrollments.enrollment_date
FROM Enrollments
JOIN Students ON Enrollments.student_id = Students.id
JOIN Courses ON Enrollments.course_id = Courses.id;