CREATE DATABASE IF NOT EXISTS ans_data CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

USE ans_data;

CREATE TABLE financial_reports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    reference_date DATE NOT NULL,
    ans_code INT NOT NULL,
    account_code VARCHAR(20) NOT NULL,
    account_description VARCHAR(255),
    initial_balance NUMERIC(15,2),
    final_balance NUMERIC(15,2)
);

CREATE TABLE operators (
    ans_code INT PRIMARY KEY,
    cnpj VARCHAR(18) NOT NULL,
    corporate_name VARCHAR(255) NOT NULL,
    trade_name VARCHAR(255),
    modality VARCHAR(100),
    street VARCHAR(255),
    number VARCHAR(20),
    complement VARCHAR(100),
    district VARCHAR(100),
    city VARCHAR(100),
    state CHAR(2),
    zip_code VARCHAR(10),
    ddd VARCHAR(5),
    phone VARCHAR(20),
    fax VARCHAR(20),
    email VARCHAR(255),
    legal_representative VARCHAR(255),
    representative_role VARCHAR(100),
    commercial_region INT,
    ans_registration_date DATE
);

