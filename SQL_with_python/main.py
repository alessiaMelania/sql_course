import sqlite3
import yaml

sqliteConnection = sqlite3.connect('myNew_db.db')

cursor = sqliteConnection.cursor()
print('DB Init')

# Creating table
table = """
    CREATE TABLE STUDENT(
        NAME VARCHAR(255), 
        CLASS VARCHAR(255), 
        SECTION VARCHAR(255));
"""

cursor.execute(table)

print("Table is created")

# Queries to INSERT records.
cursor.execute('''INSERT INTO STUDENT VALUES ('Raju', '7th', 'A')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Shyam', '8th', 'B')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Baburao', '9th', 'C')''')

# Display data inserted
print("Data Inserted in the table: ")
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

# Commit your changes in the database
sqliteConnection.commit()

# Closing the connection
sqliteConnection.close()
