# # # # import mysql.connector
# # # # from dotenv import load_dotenv
# # # # import os

# # # # load_dotenv()

# # # # def get_db_connection():
# # # #     return mysql.connector.connect(
# # # #         host=os.getenv("DB_HOST"),
# # # #         user=os.getenv("DB_USER"),
# # # #         port=int(os.getenv("DB_PORT")),
# # # #         password=os.getenv("DB_PASSWORD"),
# # # #         database=os.getenv("DB_NAME")
# # # #     )

# # # # def init_db():
# # # #     db = get_db_connection()
# # # #     print("======> db connected")
# # # #     cursor = db.cursor()
# # # #     cursor.execute("""
# # # #     CREATE TABLE IF NOT EXISTS users (
# # # #         id INT AUTO_INCREMENT PRIMARY KEY,
# # # #         username VARCHAR(100) NOT NULL,
# # # #         name VARCHAR(100),
# # # #         email VARCHAR(100) UNIQUE,
# # # #         password VARCHAR(100),
# # # #         dob DATE,
# # # #         salary DECIMAL(10, 2)
# # # #     );
# # # #     """)
# # # #     db.commit()
# # # #     print("======> User table created")
# # # #     cursor.close()
# # # #     cursor = db.cursor()
# # # #     cursor.execute("""
# # # #     CREATE TABLE IF NOT EXISTS transactions (
# # # #         id INT AUTO_INCREMENT PRIMARY KEY,
# # # #         user_id INT NOT NULL,
# # # #         amount DECIMAL(10, 2) NOT NULL,
# # # #         category VARCHAR(100) NOT NULL,
# # # #         mode VARCHAR(50) NOT NULL,
# # # #         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# # # #     );
# # # #     """)
# # # #     db.commit()
# # # #     print("======> Transactions table created")
# # # #     cursor.close()
# # # #     db.close()
# # # #     print("DB_PORT:", os.getenv("DB_PORT"))

        
# # # # if __name__ == "__main__":
# # # #     init_db()


# # # from dotenv import load_dotenv
# # # import os

# # # load_dotenv()  # This loads .env file

# # # print("DB_HOST:", os.getenv("DB_HOST"))
# # # print("DB_USER:", os.getenv("DB_USER"))
# # # print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
# # # print("DB_NAME:", os.getenv("DB_NAME"))
# # # print("DB_PORT:", os.getenv("DB_PORT"))


# # from dotenv import load_dotenv
# # import os

# # # Load .env file from the current directory
# # dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# # load_dotenv(dotenv_path=dotenv_path)

# # print("DB_HOST:", os.getenv("DB_HOST"))
# # print("DB_USER:", os.getenv("DB_USER"))
# # print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
# # print("DB_NAME:", os.getenv("DB_NAME"))
# # print("DB_PORT:", os.getenv("DB_PORT"))


# import mysql.connector
# from dotenv import load_dotenv
# import os

# # Load environment variables
# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# load_dotenv(dotenv_path=dotenv_path)

# def get_db_connection():
#     return mysql.connector.connect(
#         host=os.getenv("DB_HOST"),
#         port=os.getenv("DB_PORT"),
#         user=os.getenv("DB_USER"),
#         port=int(os.getenv("DB_PORT")),
#         password=os.getenv("DB_PASSWORD"),
#         database=os.getenv("DB_NAME")
#     )

# def init_db():
#     db = get_db_connection()
#     print("======> DB Connected Successfully")
#     cursor = db.cursor()
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         username VARCHAR(100) NOT NULL,
#         name VARCHAR(100),
#         email VARCHAR(100) UNIQUE,
#         password VARCHAR(100),
#         dob DATE,
#         salary DECIMAL(10, 2)
#     );
#     """)
#     db.commit()
#     print("======> User table created successfully")
#     cursor.close()
    
#     cursor = db.cursor()
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS transactions (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         user_id INT NOT NULL,
#         amount DECIMAL(10, 2) NOT NULL,
#         category VARCHAR(100) NOT NULL,
#         mode VARCHAR(50) NOT NULL,
#         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#     );
#     """)
#     db.commit()
#     print("======> Transactions table created successfully")
#     cursor.close()
#     db.close()
        
# <<<<<<< HEAD
# if __name__ == "__main__":
#     init_db()
# =======
# >>>>>>> dfb3d7280f2d4c1a5653d4d191440df8353c89ab




import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def init_db():
    db = get_db_connection()
    print("======> DB Connected Successfully")
    cursor = db.cursor()
    
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
    print("======> User table created successfully")
    cursor.close()
    
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        category VARCHAR(100) NOT NULL,
        mode VARCHAR(50) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    db.commit()
    print("======> Transactions table created successfully")
    cursor.close()
    db.close()
        
