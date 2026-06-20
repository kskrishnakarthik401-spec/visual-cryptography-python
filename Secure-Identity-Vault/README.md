### 🔑 Enterprise Identity Access Vault (Java Middleware & SQL Primitives)

A secure backend credential verification and identity management engine. This module bridges object-oriented **Java** middleware logic with relational **SQL** database schemas to execute production-ready, cryptographically secure user authentication workflows.

* * *

### ⚙️ Core Engineering Concepts

### 1\. Cryptographic Salting & Entropy Isolation

To protect user records against pre-computed data breaches, the engine utilizes Java's `SecureRandom` cryptosystem to generate a unique, high-entropy **16-byte random salt** string for every single user generation event. This block shifts static passwords into unique hashes, rendering standard pre-computed tracking metrics useless.

### 2\. SHA-256 Hashing Pipeline

The system chains the unique database salt directly to the raw password input stream before running it through the native `MessageDigest` engine:

**Database Hash = SHA-256 ( Salt + Plaintext Password )**

The resulting binary payload is then mapped using bitwise masking arrays into a clean, 64-character hexadecimal digest string engineered for low-overhead database indexing.

### 3\. Rainbow Table & Dictionary Attacks Immunity

By enforcing dynamic salt allocation, identical passwords typed by two different users generate completely distinct hash strings inside the data tables. This step mathematically guarantees perfect immunity against **Rainbow Table Attacks** and localized **Dictionary Attacks**.

* * *

### 📊 Pipeline Operations

When executed, the system safely processes credentials through a closed loop:

text

    [ Input Password String ] ──► [ Generate 16-Byte Random Salt ]
                                               │
                                               ▼
    [ Transmit Account Payload ] ◄── [ Compile 64-Chr Hex SHA-256 ]
    


* * *

### 🚀 Execution & Deployment

### 1\. SQL Schema Initialization

Run this script inside your relational database engine workspace to instantiate the data matrix parameters:

sql

    CREATE DATABASE EnterpriseIdentityVault;
    USE EnterpriseIdentityVault;
    
    CREATE TABLE SystemUsers (
        UserID INT AUTO_INCREMENT PRIMARY KEY,
        Username VARCHAR(50) UNIQUE NOT NULL,
        PasswordHash VARCHAR(64) NOT NULL,
        CryptographicSalt VARCHAR(32) NOT NULL
    );
    


### 2\. Compiling the Java Subsystem

Compile and initialize the application directly via your machine console terminal:

bash

    javac IdentityVault.java
    java IdentityVault
    ```