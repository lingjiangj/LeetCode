SELECT Request_at AS 'Day',
     ROUND(SUM(CASE WHEN Status LIKE 'cancelled%' THEN 1 ELSE 0 END)/COUNT(*),2) AS 'Cancellation Rate'
FROM Trips AS T
JOIN Users AS U
ON T.Client_ID = U.Users_Id
WHERE U.Banned = 'No' AND U.Role = 'client' AND Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY Request_at
ORDER BY Request_at
