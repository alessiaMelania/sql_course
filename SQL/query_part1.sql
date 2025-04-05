-- Create Students Table
CREATE TABLE Students (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      age INTEGER,
      email TEXT
    );

-- Version 2
CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT
      );

-- Insert a Record in Students Table
INSERT INTO Students (name, age, email) 
VALUES ('John Doe', 20, 'johndoe@example.com');

-- Insert Multiple Records inside Students Table
INSERT INTO Students (name, age, email) 
VALUES 
    ('Bahadurjit Sabharwal', 18, 'tristanupadhyay@example.net'),
    ('Zayyan Arya', 20, 'yashawinibhakta@example.org'),
    ('Hemani Shukla', 18, 'gaurikanarula@example.com');

-- Select data froma a Table
SELECT *
FROM Student

SELECT name
FROM Student
WHERE age > 18;

-- Update Data in a Table
UPDATE Student
SET email = 'johndoe@exampleupdate.com'
WHERE
    name LIKE 'John Doe';

-- Delete Data from a Table
DELETE FROM Student
WHERE name LIKE 'John Doe';

-- Drop a Table
DROP TABLE Student;

DROP TABLE IF EXISTS Student;
