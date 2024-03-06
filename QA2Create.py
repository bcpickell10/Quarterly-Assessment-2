import sqlite3 as sql
conn=sql.connect('quarterly_assessment.db')
cr=conn.cursor()

cr.execute(
    """CREATE TABLE IF NOT EXISTS Finance
    (id TEXT PRIMARY KEY, Question TEXT, Answer TEXT)""")

cr.execute(
    """CREATE TABLE IF NOT EXISTS Analytics
    (id TEXT PRIMARY KEY, Question TEXT, Answer TEXT)""")

cr.execute(
    """CREATE TABLE IF NOT EXISTS Business_Management
    (id TEXT PRIMARY KEY, Question TEXT, Answer TEXT)""")

cr.execute(
    """CREATE TABLE IF NOT EXISTS Analytical_Thinking
    (id TEXT PRIMARY KEY, Question TEXT, Answer TEXT)""")

cr.execute(
    """CREATE TABLE IF NOT EXISTS Apps_Development
    (id TEXT PRIMARY KEY, Question TEXT, Answer TEXT)""")