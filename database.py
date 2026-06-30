import sqlite3

connection = sqlite3.connect("LoginData.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS VEHICLE_DATA(
    TaskID TEXT PRIMARY KEY,
    Duration INTEGER,
    Impact INTEGER
)
""")

cursor.execute("""
     INSERT OR IGNORE INTO VEHICLE_DATA(TaskID,Duration,Impact)
     VALUES(
        "264eh3d---4hg",
        1,
        5
)
""")

connection.commit()
connection.close()

print("Database Created Successfully")