import sqlite3

def get_table_names(database_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_file)
    
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    
    try:
        # Retrieve the names of all tables in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' LIMIT 5")
        
        # Fetch all rows from the cursor
        table_names = cursor.fetchall()
        
        # Print the names of the tables
        print("Names of tables in the database:")
        for table in table_names:
            print(table[0])
    
    except sqlite3.Error as e:
        print("Error retrieving table names:", e)
    
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

# Replace 'database_file_name.db' with the name of your SQL database file
database_file = 'quarterly_assessment.db'
get_table_names(database_file)
