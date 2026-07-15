import sqlite3


conn = sqlite3.connect(
    "dota_coach.db"
)

cursor = conn.cursor()


cursor.execute(
    "SELECT * FROM analyses"
)


print(cursor.fetchall())


conn.close()