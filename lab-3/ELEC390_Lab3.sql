-- Use employees database
USE employees;

-- Question 01: Retrieve all columns from both employees and salaries tables
SELECT * 
FROM employees, salaries;

-- Question 02: From the salaries table, find the records whose salary times 1.7 is greater than $100_000
SELECT emp_no, salary, salary * 1.7 AS salary_modified 
FROM salaries
WHERE (salary * 1.7) > 100000;

-- Question 03: From the salaries table, find the average of the salaries whose emp_no is greater than 1_510
SELECT AVG(salary) as average_salary
FROM salaries
WHERE emp_no > 1510;

-- Question 04: From the salaries table, find the unique emp_no and the average salary of each unique emp_no
SELECT emp_no, AVG(salary) as average_salary
FROM salaries
GROUP BY emp_no;

-- Question 05: From the ‘Employees’ database, find the first_name, last_name, and salary of all the employees
SELECT employees.emp_no, employees.first_name, employees.last_name, salaries.salary, salaries.from_date, salaries.to_date
FROM employees
INNER JOIN salaries
ON employees.emp_no = salaries.emp_no;

-- Question 06: Write a procedure named ‘emp_avg_salary’. This procedure must accept employee number as its input, and show the average salary associated with this employee number
DELIMITER $$
CREATE PROCEDURE `emp_avg_salary`(IN p_emp_no INT)
BEGIN
	SELECT employees.emp_no, employees.first_name, employees.last_name, AVG(salaries.salary) as average_salary
	FROM employees
	JOIN salaries ON employees.emp_no = salaries.emp_no
	WHERE employees.emp_no = p_emp_no
	GROUP BY employees.emp_no, employees.first_name, employees.last_name;
END $$
DELIMITER ;

CALL emp_avg_salary(11300);