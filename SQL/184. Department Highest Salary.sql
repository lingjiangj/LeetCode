SELECT d.Name AS Department,e.Name AS Employee, e.Salary AS Salary
From Employee AS e
JOIN Department AS d
ON e.DepartmentID = d.Id
WHERE (e.Salary,e.DepartmentID) IN
(SELECT MAX(Salary),DepartmentID
From Employee
GROUP BY DepartmentID)
