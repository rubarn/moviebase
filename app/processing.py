from db_conn import connect_to_db

conn = connect_to_db()


if conn:
    try:
        cursor = conn.cursor()
        table_name = "[title.akas]"
        query = f"SELECT TOP 1 * FROM {table_name}"
        cursor.execute(query)

        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except Exception as e:
        print("Error processing data:", e)

    finally:
        # Lukk forbindelsen
        conn.close()
        print("Database connection closed.")
else:
    print("Could not establish a database connection.")