CREATE DATABASE EnterpriseIdentityVault;
USE EnterpriseIdentityVault;

CREATE TABLE SystemUsers (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(50) UNIQUE NOT NULL,
    PasswordHash VARCHAR(64) NOT NULL,
    CryptographicSalt VARCHAR(32) NOT NULL
);
