# Todo Project
# CRUD => Create, Read, Update, Delete
 
# Step
 
# python => python -V or python --version
# pip list => display all the dependency of python
# mysql => pip install mysql-connector-python
 
# connect => connection, method
# cursor => cursor => cursor object
# execute => execute the query
 
import mysql.connector as mysql
 
con = mysql.connect(host="localhost", user="root", passwd="Jyoti@0987")
 
cursor = con.cursor()
 
cursor.execute("CREATE DATABASE IF NOT EXISTS TODOAPP")
# Database => collection of tables
 
 
print("Database created...")
 
cursor.execute("USE TODOAPP")
 
# create the tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_todo (
        id INT AUTO_INCREMENT PRIMARY KEY,
        task VARCHAR(50) NOT NULL,
        status ENUM('pending', 'completed') DEFAULT 'pending'
    )
""")
 
print("Table created...")