/* Method 1 - SQL Server*/
SELECT DISTINCT l1.Num AS ConsecutiveNums
FROM Logs l1, Logs l2, Logs l3
WHERE l1.Id =l2.Id-1 AND l2.Id = l3.Id-1 AND l1.Num = l2.Num AND l2.Num = l3.Num


/* Method 2 - MySQL*/
SELECT DISTINCT Num AS ConsecutiveNums
FROM (
    SELECT Id,Num,
        @count := IF(@predNum = Num, @count+1,1) AS Count,
        @predNum := Num AS predNum
    FROM Logs, (SELECT @predNum := NULL, @count:= 1)  var) temp
WHERE Count >= 3
