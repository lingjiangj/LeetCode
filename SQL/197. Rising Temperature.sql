/* Method 1 */
SELECT Id
FROM (SELECT Id,RecordDate,Temperature,
            @higher:= If(Temperature > @preTemp,"Yes","No") AS Higher,
            @NextDate := If(DATEDIFF(RecordDate,@preDate) = 1,"Yes","No") AS NextDate,
            @preTemp := Temperature AS preTemp,
            @preDate := RecordDate
      FROM Weather,
      (SELECT @preTemp := NULL,@preDate := NULL,@highter := NULL) AS var
     ORDER BY RecordDate) AS tmp
WHERE Higher = "Yes" AND NextDate = "Yes"


/* Method 2 */
SELECT w1.Id
FROM Weather AS w1
JOIN Weather AS w2
ON DATEDIFF(w1.RecordDate,w2.RecordDate) = 1  
WHERE w1.Temperature > w2.Temperature
