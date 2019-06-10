DELETE FROM Person
WHERE Id NOT IN(
    SELECT minID 
    FROM (SELECT Min(Id) as minID,Email
        FROM Person
         GROUP BY Email) AS tmp)
