import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create the python_programming table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS python_programming (
        id INTEGER PRIMARY KEY,
        name TEXT,
        grade INTEGER
    )
''')

# Insert new rows into the table
students = [
    (55, 'Carl Davis', 61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'Jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99)
]
cursor.executemany('INSERT OR REPLACE INTO python_programming (id, name, grade) VALUES (?, ?, ?)', students)

# Select all records with a grade between 60 and 80
cursor.execute('SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80')
print("Students with grades between 60 and 80:")
for row in cursor.fetchall():
    print(row)

# Change Carl Davis's grade to 65
cursor.execute('UPDATE python_programming SET grade = 65 WHERE name = "Carl Davis"')

# Delete Dennis Fredrickson's row
cursor.execute('DELETE FROM python_programming WHERE name = "Dennis Fredrickson"')

# Change the grade of all students with an id greater than 55 to 80
cursor.execute('UPDATE python_programming SET grade = 80 WHERE id > 55')

# Verify the final state of the table
cursor.execute('SELECT * FROM python_programming')
print("\nFinal state of the python_programming table:")
for row in cursor.fetchall():
    print(row)

# Commit changes and close the connection
conn.commit()
conn.close()
