-- Create Database
CREATE DATABASE office_visitor_db;
USE office_visitor_db;

-- Create Employees Table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    department VARCHAR(100),
    phone VARCHAR(15)
);

-- Create Visitors Table
CREATE TABLE visitors (
    visitor_id INT AUTO_INCREMENT PRIMARY KEY,
    visitor_name VARCHAR(100),
    visit_date DATE,
    emp_id INT,
    entry_time DATETIME,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);

-- Insert Employees (15 records)
INSERT INTO employees VALUES
(101, 'Arun Kumar', 'HR', '9876543210'),
(102, 'Priya Sharma', 'Finance', '9876543211'),
(103, 'Karthik R', 'IT', '9876543212'),
(104, 'Divya S', 'Admin', '9876543213'),
(105, 'Rohit M', 'Marketing', '9876543214'),
(106, 'Sneha P', 'IT', '9876543215'),
(107, 'Vignesh K', 'HR', '9876543216'),
(108, 'Anitha L', 'Finance', '9876543217'),
(109, 'Suresh B', 'Admin', '9876543218'),
(110, 'Meena D', 'Marketing', '9876543219'),
(111, 'Rahul T', 'IT', '9876543220'),
(112, 'Keerthana V', 'HR', '9876543221'),
(113, 'Manoj C', 'Finance', '9876543222'),
(114, 'Lakshmi N', 'Admin', '9876543223'),
(115, 'Ajay P', 'Marketing', '9876543224');

-- Insert Visitors (Sample Visit Data)
INSERT INTO visitors (visitor_name, visit_date, entry_time, emp_id) VALUES
('Ravi Kumar', '2026-01-10', '2026-01-10 09:30:00', 101),
('Anu Priya', '2026-02-12', '2026-02-12 10:15:00', 103),
('Sathish K', '2026-03-15', '2026-03-15 11:00:00', 105),
('Deepa S', '2026-04-18', '2026-04-18 11:45:00', 110),
('Mani Raj', '2026-05-20', '2026-05-20 12:30:00', 102),
('Kavitha R', '2026-06-22', '2026-06-22 13:15:00', 104),
('Prakash M', '2026-07-25', '2026-07-25 14:00:00', 106),
('Nisha L', '2026-08-28', '2026-08-28 14:30:00', 108);

-- View Employees Table
SELECT * FROM employees;

-- View Visitors Table
SELECT * FROM visitors;

-- Final Tabular View (Visitors + Employee Details)
SELECT 
    v.visitor_id,
    v.visitor_name,
    v.visit_date,
    v.entry_time,
    e.emp_name,
    e.department,
    e.phone
FROM visitors v
JOIN employees e ON v.emp_id = e.emp_id;