SELECT a.Name AS 'Employee'
FROM Employee AS a
JOIN Employee AS b
ON a.ManagerId = b.Id
WHERE a.Salary > b.Salary
