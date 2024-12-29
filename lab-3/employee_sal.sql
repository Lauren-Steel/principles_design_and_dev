CREATE DEFINER=`root`@`localhost` PROCEDURE `emp_salary`(IN p_emp_no INT)
BEGIN
SELECT
employees.emp_no, employees.first_name, employees.last_name, salaries.salary
FROM employees JOIN salaries ON employees.emp_no=salaries.emp_no
WHERE employees.emp_no = p_emp_no;
END