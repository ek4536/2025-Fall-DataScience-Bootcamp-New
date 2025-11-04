SELECT p.project_id, SUM(e.experience_years)/COUNT(e.name) AS average_years
FROM Project p
LEFT JOIN Employee e
USING(employee_id)
GROUP BY p.project_id;
