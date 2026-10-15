WITH segments AS (
    SELECT Contract, InternetService,
           COUNT(*) AS customers,
           ROUND(100.0 * AVG(CASE WHEN Churn='Yes' THEN 1.0 ELSE 0 END), 1) AS churn_rate_pct,
           ROUND(SUM(CASE WHEN Churn='Yes' THEN MonthlyCharges ELSE 0 END), 0) AS monthly_revenue_lost
    FROM customers
    GROUP BY Contract, InternetService
    HAVING COUNT(*) >= 50
)
SELECT *, RANK() OVER (ORDER BY churn_rate_pct DESC) AS risk_rank
FROM segments ORDER BY risk_rank;
