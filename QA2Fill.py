import sqlite3

def insert_values_into_tables(database_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_file)
    
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    
    try:
        # Insert values into Table 1
        cursor.execute("INSERT INTO Finance (Number, Question, Answer) VALUES (?, ?, ?)", (1, 'value2', 'value3'))
        cursor.execute("INSERT INTO Finance (Number, Question, Answer) VALUES (?, ?, ?)", (2, 'value2', 'value3'))
        cursor.execute("INSERT INTO Finance (Number, Question, Answer) VALUES (?, ?, ?)", (3, 'value2', 'value3'))
        cursor.execute("INSERT INTO Finance (Number, Question, Answer) VALUES (?, ?, ?)", (4, 'value2', 'value3'))
        cursor.execute("INSERT INTO Finance (Number, Question, Answer) VALUES (?, ?, ?)", (5, 'value2', 'value3'))
        
        # Insert values into Table 2
        cursor.execute("INSERT INTO Analytics (Number, Question, Answer) VALUES (?, ?, ?)", (1, 'value5','value6'))
        cursor.execute("INSERT INTO Analytics (Number, Question, Answer) VALUES (?, ?, ?)", (2, 'value5','value6'))
        cursor.execute("INSERT INTO Analytics (Number, Question, Answer) VALUES (?, ?, ?)", (3, 'value5','value6'))
        cursor.execute("INSERT INTO Analytics (Number, Question, Answer) VALUES (?, ?, ?)", (4, 'value5','value6'))
        cursor.execute("INSERT INTO Analytics (Number, Question, Answer) VALUES (?, ?, ?)", (5, 'value5','value6'))
        
        # Insert values into Table 3
        cursor.execute("INSERT INTO Business_Management (Number, Question, Answer) VALUES (?, ?, ?)", (1, 'value7', 'value8'))
        cursor.execute("INSERT INTO Business_Management (Number, Question, Answer) VALUES (?, ?, ?)", (2, 'value7', 'value8'))
        cursor.execute("INSERT INTO Business_Management (Number, Question, Answer) VALUES (?, ?, ?)", (3, 'value7', 'value8'))
        cursor.execute("INSERT INTO Business_Management (Number, Question, Answer) VALUES (?, ?, ?)", (4, 'value7', 'value8'))
        cursor.execute("INSERT INTO Business_Management (Number, Question, Answer) VALUES (?, ?, ?)", (5, 'value7', 'value8'))
        
        # Insert values into Table 4
        cursor.execute("INSERT INTO Analytical_Thinking (Number, Question, Answer) VALUES (?, ?, ?)", (1, 'value7', 'value8'))
        cursor.execute("INSERT INTO Analytical_Thinking (Number, Question, Answer) VALUES (?, ?, ?)", (2, 'value7', 'value8'))
        cursor.execute("INSERT INTO Analytical_Thinking (Number, Question, Answer) VALUES (?, ?, ?)", (3, 'value7', 'value8'))
        cursor.execute("INSERT INTO Analytical_Thinking (Number, Question, Answer) VALUES (?, ?, ?)", (4, 'value7', 'value8'))
        cursor.execute("INSERT INTO Analytical_Thinking (Number, Question, Answer) VALUES (?, ?, ?)", (5, 'value7', 'value8'))
        
        
        # Insert values into Table 5
        cursor.execute("INSERT INTO Apps_Development (Number, Question, Answer) VALUES (?, ?, ?)", ('value6', 'value7', 'value8'))
        cursor.execute("INSERT INTO Apps_Development (Number, Question, Answer) VALUES (?, ?, ?)", ('value6', 'value7', 'value8'))
        cursor.execute("INSERT INTO Apps_Development (Number, Question, Answer) VALUES (?, ?, ?)", ('value6', 'value7', 'value8'))
        cursor.execute("INSERT INTO Apps_Development (Number, Question, Answer) VALUES (?, ?, ?)", ('value6', 'value7', 'value8'))
        cursor.execute("INSERT INTO Apps_Development (Number, Question, Answer) VALUES (?, ?, ?)", ('value6', 'value7', 'value8'))
        
        # Commit the changes to the database
        conn.commit()
        
        print("Values inserted into tables successfully.")
    
    except sqlite3.Error as e:
        print("Error inserting values into tables:", e)
        
        # Rollback the transaction if an error occurs
        conn.rollback()
    
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

# Replace 'database_file_name.db' with the name of your SQL database file
database_file = 'quarterly_assessment.db'
insert_values_into_tables(database_file)
