import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def init_db():
    db = get_db_connection()
    print("======> db connected")
    cursor = db.cursor()

    # 1. Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        name VARCHAR(100),
        email VARCHAR(100) UNIQUE,
        password VARCHAR(100),
        dob DATE,
        salary DECIMAL(10, 2)
    );
    """)
    db.commit()
    print("======> Users table created")
    cursor.close()

    # 2. Transactions Table
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        category ENUM('Travel', 'Shopping', 'Grocery', 'Food', 'Personal', 'Education', 'Bills', 'Other') NOT NULL,
        type ENUM('expense', 'income') NOT NULL,
        mode ENUM('upi', 'cash', 'others', 'card') NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    db.commit()
    print("======> Transactions table created")
    cursor.close()

    # 3. Profile Build Table
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profile_build (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Food DECIMAL(10, 2) DEFAULT 0,
        Travel DECIMAL(10, 2) DEFAULT 0,
        Shopping DECIMAL(10, 2) DEFAULT 0,
        Grocery DECIMAL(10, 2) DEFAULT 0,
        Personal DECIMAL(10, 2) DEFAULT 0,
        Education DECIMAL(10, 2) DEFAULT 0,
        Bills DECIMAL(10, 2) DEFAULT 0,
        Other DECIMAL(10, 2) DEFAULT 0
    );
    """)
    db.commit()
    print("======> Profile Build table created")
    cursor.close()

    # 4. Goals Table
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS goals (
        id INT AUTO_INCREMENT PRIMARY KEY,
        amount DECIMAL(10, 2) NOT NULL,
        status ENUM('completed', 'incompleted', 'deleted') NOT NULL
    );
    """)
    db.commit()
    print("======> Goals table created")
    cursor.close()

    # 5. Available Badges Table
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS available_badges (
        badge_id INT AUTO_INCREMENT PRIMARY KEY,
        badge_image VARCHAR(255),
        badge_desc TEXT,
        badge_url VARCHAR(255),
        badge_criteria TEXT
    );
    """)
    db.commit()
    print("======> Available Badges table created")
    cursor.close()

    # 6. Issued Badges Table
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS issued_badges (
        badge_id INT,
        id INT,
        issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    db.commit()
    print("======> Issued Badges table created")
    cursor.close()

    # 7. Streaks Table
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS streaks (
        id INT PRIMARY KEY,
        count INT DEFAULT 0
    );
    """)
    db.commit()
    print("======> Streaks table created")
    cursor.close()

    db.close()
