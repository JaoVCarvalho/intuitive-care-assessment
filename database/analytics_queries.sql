SELECT
    fr.ans_code,
    o.corporate_name AS health_operator,
    SUM(fr.final_balance) AS total_expense
FROM financial_reports fr
JOIN operators o ON fr.ans_code = o.ans_code
WHERE
    fr.reference_date = (SELECT MAX(reference_date) FROM financial_reports)
    AND fr.account_description = "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR "
GROUP BY fr.ans_code, o.corporate_name
ORDER BY total_expense DESC
LIMIT 10;

--

SELECT
    fr.ans_code,
    o.corporate_name AS health_operator,
    SUM(fr.final_balance) AS total_expense
FROM financial_reports fr
JOIN operators o ON fr.ans_code = o.ans_code
WHERE
    fr.reference_date BETWEEN '2024-01-01' AND '2024-12-31'
--    fr.reference_date BETWEEN
--		STR_TO_DATE(CONCAT(YEAR(CURDATE()) - 1, '-01-01'), '%Y-%m-%d')
--		AND
--		STR_TO_DATE(CONCAT(YEAR(CURDATE()) - 1, '-12-31'), '%Y-%m-%d')
    AND fr.account_description = "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR "
GROUP BY fr.ans_code, o.corporate_name
ORDER BY total_expense DESC
LIMIT 10;
