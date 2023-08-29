#!/usr/bin/env python
# coding: utf-8

# Q-1 What is database ? Differentiate between SQL and NOSQL database.

# Ans-1 A database is an organized collection of structured information , or data , typically stored electronically in a computer system. A database is usually controlled by a database management system (DBMS).
# 
# Difference between SQL and NOSQL
# 
# 1-  SQL- It stand for structured query languge , and it is the standard language for interacting with relation database.
#   NOSQL- It stands for not only sql , and it is a term that covers a wide range of non- relation  database that store data in     different formats and structures.
#   
# 2-  SQL store the data in the table form.
#     NOSQL store the data in the document based ,graphic based or key-value pair.
#     
#   

# Q-2 What is DDL ? Expalain why CREATE ,DROP , ALTER and TRUNCATE are used with an example.

# Ans-2 DDL stands for data definition language. It simply deals with descriptions of the database schema and is used to create and modify the structure of database object in the database.DDL commands used to create , modify ,and delete database atructure but not data.
# 
# CREATE- This help create an object (database ,table).
# Examle- CREATE table test_tale.
# 
# DROP- This help delete an object.
# Example- DROP test_table.
# 
# ALTER- This help alter the existing database or its object structures.
# Example- ALTER TABLE test_table.
# 
# TRUNCATE- This help to remove all recods from a table, including all space allocated for the recods are removed. 
# Example- TRUNCATE TABLE test_table.

# Q-3 What is DML ? Explain INSERT,UPDATE,and DELETE with an example.

# Ans-3 DML stands for data manuplating language . It is a class of sql statement that are used to query ,edit ,add and delete row-level data from database tables or views.The main DML statements are SELECT, INSERT, DELETE ,and UPDATE.
# 
# INSERT-This help to insert data in database table.
# Example- INSERT into test_table values(A INT, B VARCHER(50))
# 
# UPDATE- This help to update or modify the existing data iin database tables
# Example UPDATE test_table
#         SET name ="Neha Rana"
#         where id =2
# 
# 
# DELETE- This help to remove single or multiple existing recods from the database table.
# Exapmple DELETE FROM test_table
# WHERE id=2.

# Q-4 What is DQL ? Explain SELECT with an exmple.
# 
# Ans-4 DQL is stands for data query language. It is a part of the grouping involved in sql  sub language.
# 
# SELECT- This help to retrieve data from database.
# Example SELECT * from test_table.

# Q-5 Explain primary key and foreign key.
# 
# Ans-5 
# 
# PRIMARY KEY
#                  The primary key is a unique or non_null key that uniquely identify every record in a table or relation. 
#                 
# FORIEGN KEY-
#                  The foriegn key is a group of one or more columns in a database to uniquely identify another database record in                  some other table to maintain the referenctial integrety.

# Q-6 Write a python code to connect MYSQL to PYTHON . Explain the curser() and execute() method.
# 
# 

# In[4]:


'''import mySQL.connector
mydb =mySQL.connector.connect(
hosts= "localhost",
user= "abc",
password ="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
    
cursor() it is used to point database and its object . it is an object to make connection for executing sql queries.
execute() it s method used to execute mycursor element or data stored inside cursor.'''


# Q-7 Give the order of execution of sql clauses in an sql query.

# Ans-7 order of execution defines order in which clauses of query are evaluated .
# 1. 
