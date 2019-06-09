CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        /* Write your T-SQL query statement below. */
      SELECT DISTINCT Salary
      FROM (SELECT Salary, 
            dense_rank() over (order by Salary desc) as rank
           FROM Employee) r
      WHERE r.rank = @N 
    );
END
