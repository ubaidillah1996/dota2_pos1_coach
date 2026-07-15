import sqlite3


DATABASE_NAME = "dota_coach.db"


def create_connection():

    conn = sqlite3.connect(
        DATABASE_NAME
    )

    return conn



def create_table():

    conn = create_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS analyses (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            match_id INTEGER,

            hero TEXT,

            player_name TEXT,

            kda REAL,

            lh_per_min REAL,

            gpm INTEGER,

            status TEXT

        )
        """
    )


    conn.commit()

    conn.close()

def create_table():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS analyses (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            match_id INTEGER,

            hero TEXT,

            player_name TEXT,

            kda REAL,

            lh_per_min REAL,

            gpm INTEGER,

            status TEXT

        )
        """
    )

    conn.commit()
    conn.close()


create_table()

def save_analysis(
    match_id,
    hero,
    player_name,
    kda,
    lh_per_min,
    gpm,
    status
):

    conn = create_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO analyses
        (
            match_id,
            hero,
            player_name,
            kda,
            lh_per_min,
            gpm,
            status
        )

        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,

        (
            match_id,
            hero,
            player_name,
            kda,
            lh_per_min,
            gpm,
            status
        )
    )


    conn.commit()

    conn.close()

def view_history():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM analyses
        """
    )

    records = cursor.fetchall()

    conn.close()

    return records