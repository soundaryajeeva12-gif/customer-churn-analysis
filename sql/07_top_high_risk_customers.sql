SELECT p.customerID, ROUND(p.churn_probability, 3) AS churn_probability,
       c.Contract, c.TechSupport, c.MonthlyCharges
FROM predictions p JOIN customers c USING (customerID)
WHERE p.high_risk = 1
ORDER BY p.churn_probability DESC, c.MonthlyCharges DESC
LIMIT 10;
