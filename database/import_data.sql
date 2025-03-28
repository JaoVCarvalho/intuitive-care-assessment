LOAD DATA LOCAL INFILE 'database/files/operators/Relatorio_cadop.csv'
INTO TABLE operators
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
    ans_code,
    cnpj,
    corporate_name,
    trade_name,
    modality,
    street,
    number,
    complement,
    district,
    city,
    state,
    zip_code,
    ddd,
    phone,
    fax,
    email,
    legal_representative,
    representative_role,
    @commercial_region,
    ans_registration_date
)
SET commercial_region = NULLIF(@commercial_region, '');

--

LOAD DATA LOCAL INFILE 'database/files/financial/1T2023.csv'
INTO TABLE financial_reports
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
    reference_date,
    ans_code,
    account_code,
    account_description,
    @initial_balance,
    @final_balance
)
SET
    initial_balance = REPLACE(@initial_balance, ',', '.'),
    final_balance = REPLACE(@final_balance, ',', '.');

--

LOAD DATA LOCAL INFILE 'database/files/financial/2T2023.csv'
INTO TABLE financial_reports
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
    reference_date,
    ans_code,
    account_code,
    account_description,
    @initial_balance,
    @final_balance
)
SET
    initial_balance = REPLACE(@initial_balance, ',', '.'),
    final_balance = REPLACE(@final_balance, ',', '.');

--

LOAD DATA LOCAL INFILE 'database/files/financial/3T2023.csv'
INTO TABLE financial_reports
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
    reference_date,
    ans_code,
    account_code,
    account_description,
    @initial_balance,
    @final_balance
)
SET
    initial_balance = REPLACE(@initial_balance, ',', '.'),
    final_balance = REPLACE(@final_balance, ',', '.');

--

LOAD DATA LOCAL INFILE 'database/files/financial/4T2023.csv'
INTO TABLE financial_reports
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
    @reference_date,
    ans_code,
    account_code,
    account_description,
    @initial_balance,
    @final_balance
)
SET
    reference_date = STR_TO_DATE(@reference_date, '%d/%m/%Y'),
    initial_balance = REPLACE(@initial_balance, ',', '.'),
    final_balance = REPLACE(@final_balance, ',', '.');

--

LOAD DATA LOCAL INFILE 'database/files/financial/1T2024.csv'
INTO TABLE financial_reports
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
    reference_date,
    ans_code,
    account_code,
    account_description,
    @initial_balance,
    @final_balance
)
SET
    initial_balance = REPLACE(@initial_balance, ',', '.'),
    final_balance = REPLACE(@final_balance, ',', '.');

--

LOAD DATA LOCAL INFILE 'database/files/financial/2T2024.csv'
INTO TABLE financial_reports
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
    reference_date,
    ans_code,
    account_code,
    account_description,
    @initial_balance,
    @final_balance
)
SET
    initial_balance = REPLACE(@initial_balance, ',', '.'),
    final_balance = REPLACE(@final_balance, ',', '.');

--

LOAD DATA LOCAL INFILE 'database/files/financial/3T2024.csv'
INTO TABLE financial_reports
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
    reference_date,
    ans_code,
    account_code,
    account_description,
    @initial_balance,
    @final_balance
)
SET
    initial_balance = REPLACE(@initial_balance, ',', '.'),
    final_balance = REPLACE(@final_balance, ',', '.');

--

LOAD DATA LOCAL INFILE 'database/files/financial/4T2024.csv'
INTO TABLE financial_reports
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
    reference_date,
    ans_code,
    account_code,
    account_description,
    @initial_balance,
    @final_balance
)
SET
    initial_balance = REPLACE(@initial_balance, ',', '.'),
    final_balance = REPLACE(@final_balance, ',', '.');

