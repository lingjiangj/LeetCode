SELECT d.Name AS Department,e.Name AS Employee,e.Salary
FROM (
    SELECT DepartmentID,
        Name,Salary,
        DENSE_RANK() OVER(PARTITION BY DepartmentID ORDER BY Salary DESC) AS Rank
    FROM Employee) AS e
JOIN Department AS d
ON e.DepartmentId = d.Id
WHERE e.Rank <= 3
