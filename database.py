import sqlite3


DATABASE_NAME = "dota_coach.db"

## CONNECTING TO DB ##

def create_connection():

    conn = sqlite3.connect(
        DATABASE_NAME
    )

    return conn

## CREATING TABLE : ##
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


## SAVING / ADD USER MATCHES FUNCTION ##

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

## READ / VIEW DATA FUNCTION ##

def view_history():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            match_id,
            hero,
            player_name,
            kda,
            lh_per_min,
            gpm,
            status,
            notes

        FROM analyses
        """
    )

    records = cursor.fetchall()

    conn.close()

    return records


## DELETING FUNCTION ##

def delete_analysis(record_id):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM analyses
        WHERE id = ?
        """,
        (record_id,)
    )

    conn.commit()

    conn.close()

## CREATING FUNCTION FOR NOTES ADD BY USER ##

def add_notes_column():

    conn = create_connection()

    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            ALTER TABLE analyses
            ADD COLUMN notes TEXT
            """
        )

        conn.commit()

        print("Notes column added.")

    except Exception as e:

        pass

    conn.close()

## CREATING FUNCTION FOR NOTES UPDATE BY USER ##

def update_note(record_id, note):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE analyses
        SET notes = ?
        WHERE id = ?
        """,
        (
            note,
            record_id
        )
    )

    conn.commit()
    conn.close()

## CHECKING IF DATA ALREADY EXISTED FUNCTION ##

def check_existing_analysis(match_id, hero):

    conn = sqlite3.connect("dota_coach.db")

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT *
        FROM analyses
        WHERE match_id = ?
        AND hero = ?
        """,
        (
            match_id,
            hero
        )
    )


    result = cursor.fetchone()


    conn.close()


    return result

add_notes_column()