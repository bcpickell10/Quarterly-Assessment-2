import sqlite3 as sql
conn=sql.connect('quarterly_assessment.db')
cr=conn.cursor()

cr.execute(
    """CREATE TABLE IF NOT EXISTS Finance
    (Number INTEGER PRIMARY KEY, Question TEXT, Answer TEXT)""")

cr.execute(
    """CREATE TABLE IF NOT EXISTS Analytics
    (Number INTEGER PRIMARY KEY, Question TEXT, Answer TEXT)""")

cr.execute(
    """CREATE TABLE IF NOT EXISTS Business_Management
    (Number INTEGER PRIMARY KEY, Question TEXT, Answer TEXT)""")

cr.execute(
    """CREATE TABLE IF NOT EXISTS Analytical_Thinking
    (Number INTEGER PRIMARY KEY, Question TEXT, Answer TEXT)""")

cr.execute(
    """CREATE TABLE IF NOT EXISTS Apps_Development
    (Number INTEGER PRIMARY KEY, Question TEXT, Answer TEXT)""")