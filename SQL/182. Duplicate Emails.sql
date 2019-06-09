SELECT Email
FROM Person
GROUP BY Email
HAVING count(Id) > 1
