SELECT Contract,
       COUNT(*) AS churned_customers,
       ROUND(SUM(MonthlyCharges), 0) AS monthly_revenue_lost
FROM customers WHERE Churn = 'Yes'
GROUP BY Contract ORDER BY monthly_revenue_lost DESC;
