import pyodbc as odbc #pip install pyobcd
import keys

DRIVER_NAME=keys.DRIVER_NAME
SERVER_NAME=keys.SERVER_NAME
DATABASE_NAME=keys.DATABASE_NAME

def connect_to_db():
    #Create a connection string variable
    connectionString = f"""
        DRIVER={{{DRIVER_NAME}}};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trusted_Connection=yes;
        """

    # connect to database
    try:
        conn = odbc.connect(connectionString)
        print("Conn success: ", conn)

    except Exception as e:
        print("Conn failed:", e)
    finally:
        if 'conn' in locals():
            conn.close()

connect_to_db()