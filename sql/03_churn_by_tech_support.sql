SELECT TechSupport, COUNT(*) AS customers, ROUND(100.0 * SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) / COUNT(*), 1) AS churn_rate_pct
FROM customers WHERE InternetService <> 'No'
GROUP BY TechSupport ORDER BY churn_rate_pct DESC;
