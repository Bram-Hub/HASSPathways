import psycopg2
import json
import os
from datetime import datetime

engine = psycopg2.connect(
    database="d2kedqtund732q",
    user="jdlgewreuvgeqx",
    password="d81a731c4930221b6fed9df3271d8f6d88a387d58b15527ee4ec62732f64914e",
    host="ec2-54-163-254-204.compute-1.amazonaws.com",
    port='5432'
)

print("hi")

db_cursor = engine.cursor()
db_cursor.execute("SELECT * FROM database_course")
temp = db_cursor.fetchall()

for i in range(len(temp)):
    print(temp[i])
    print()
    print(type(temp[i]))
    print()
