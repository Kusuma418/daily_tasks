#How do you fetch duplicate records (same name, same email) from a users table
SELECT name, email, COUNT(*)
FROM users
GROUP BY name, email
HAVING COUNT(*) > 1;


#Find the second highest salary without limit
select max(salary) 
from emp 
where salary < (select max(salary) 
                from emp);

#order of execution
from
where
group by
having
select
distinct
order by
limit


#Find employees who logged in on 3 consecutive days.
SELECT DISTINCT e1.employee_id
FROM employee_logins e1
JOIN employee_logins e2 
  ON e1.employee_id = e2.employee_id AND e2.login_date = DATE_ADD(e1.login_date, INTERVAL 1 DAY)
JOIN employee_logins e3 
  ON e1.employee_id = e3.employee_id AND e3.login_date = DATE_ADD(e1.login_date, INTERVAL 2 DAY)
ORDER BY e1.employee_id;


 