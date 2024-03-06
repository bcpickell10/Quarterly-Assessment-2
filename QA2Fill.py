import sqlite3

def insert_values_into_tables(database_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_file)
    
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    
    try:
        # Insert values into Table 1
        cursor.execute("INSERT INTO Finance (id, Question, Answer) VALUES (?, ?, ?)", ('F1.', 'True/False: Net income is calculated by subtracting total expenses from total revenues on the balance sheet.', 'False'))
        cursor.execute("INSERT INTO Finance (idr, Question, Answer) VALUES (?, ?, ?)", ('F2.', 'Operating cash flow excludes cash flows from which of the following activities? a. Financing b. Investing c. Operating d. All of the above', 'd'))
        cursor.execute("INSERT INTO Finance (id, Question, Answer) VALUES (?, ?, ?)", ('F3.', 'Operating cash flow represents the cash generated from  normal business ________.', 'operations'))
        cursor.execute("INSERT INTO Finance (id, Question, Answer) VALUES (?, ?, ?)", ('F4.', 'Which ratio measures  short-term liquidity? a. Debt-to-equity ratio b. Return on equity c. Current ratio d. Price-earnings ratio', 'c'))
        cursor.execute("INSERT INTO Finance (id, Question, Answer) VALUES (?, ?, ?)", ('F5.', 'True/False: A high debt-to-equity ratio indicates a low level of financial risk.', 'False'))
        
        # Insert values into Table 2
        cursor.execute("INSERT INTO Analytics (id, Question, Answer) VALUES (?, ?, ?)", ('A1.', 'True/False: In regression analysis, the dependent variable is the variable being predicted or explained by the independent variable.', 'True'))
        cursor.execute("INSERT INTO Analytics (id, Question, Answer) VALUES (?, ?, ?)", ('A2.', 'In simple linear regression, the equation of the regression line is represented as Y = a + βX + ε, where a is the ________ and β is the regression coefficient.', 'intercept'))
        cursor.execute("INSERT INTO Analytics (id, Question, Answer) VALUES (?, ?, ?)", ('A3.', 'True/False: A p-value less than the significance level indicates that the null hypothesis should be rejected.', 'True'))
        cursor.execute("INSERT INTO Analytics (id, Question, Answer) VALUES (?, ?, ?)", ('A4.', 'The regression coefficient represents the ________ in the dependent variable for a one-unit change in the independent variable.', 'change'))
        cursor.execute("INSERT INTO Analytics (id, Question, Answer) VALUES (?, ?, ?)", ('A5.', ' If the regression coefficient of a variable is negative, what does it indicate? a. There is no relationship between the variables b. An increase in the independent variable is associated with a decrease in the dependent variable c. An increase in the independent variable is associated with an increase in the dependent variable d. The coefficient is not interpretable', 'c'))
        
        # Insert values into Table 3
        cursor.execute("INSERT INTO Business_Management (id, Question, Answer) VALUES (?, ?, ?)", ('BM1.', 'value7', 'value8'))
        cursor.execute("INSERT INTO Business_Management (id, Question, Answer) VALUES (?, ?, ?)", ('BM2.', 'value7', 'value8'))
        cursor.execute("INSERT INTO Business_Management (id, Question, Answer) VALUES (?, ?, ?)", ('BM3.', 'value7', 'value8'))
        cursor.execute("INSERT INTO Business_Management (id, Question, Answer) VALUES (?, ?, ?)", ('BM4.', 'value7', 'value8'))
        cursor.execute("INSERT INTO Business_Management (id, Question, Answer) VALUES (?, ?, ?)", ('BM5.', 'value7', 'value8'))
        
        # Insert values into Table 4
        cursor.execute("INSERT INTO Analytical_Thinking (id, Question, Answer) VALUES (?, ?, ?)", ('AT1.', 'value7', 'value8'))
        cursor.execute("INSERT INTO Analytical_Thinking (id, Question, Answer) VALUES (?, ?, ?)", ('AT2.', 'value7', 'value8'))
        cursor.execute("INSERT INTO Analytical_Thinking (id, Question, Answer) VALUES (?, ?, ?)", ('AT3.', 'value7', 'value8'))
        cursor.execute("INSERT INTO Analytical_Thinking (id, Question, Answer) VALUES (?, ?, ?)", ('AT4.', 'value7', 'value8'))
        cursor.execute("INSERT INTO Analytical_Thinking (id, Question, Answer) VALUES (?, ?, ?)", ('AT5.', 'value7', 'value8'))
        
        
        # Insert values into Table 5
        cursor.execute("INSERT INTO Apps_Development (id, Question, Answer) VALUES (?, ?, ?)", ('AD1.', 'value7', 'value8'))
        cursor.execute("INSERT INTO Apps_Development (id, Question, Answer) VALUES (?, ?, ?)", ('AD2.', 'value7', 'value8'))
        cursor.execute("INSERT INTO Apps_Development (id, Question, Answer) VALUES (?, ?, ?)", ('AD3.', 'value7', 'value8'))
        cursor.execute("INSERT INTO Apps_Development (id, Question, Answer) VALUES (?, ?, ?)", ('AD4.', 'value7', 'value8'))
        cursor.execute("INSERT INTO Apps_Development (id, Question, Answer) VALUES (?, ?, ?)", ('AD5.', 'value7', 'value8'))
        
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
