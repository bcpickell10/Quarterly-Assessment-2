import sqlite3 as sql
conn=sql.connect('quarterly_assessment.db')
cr=conn.cursor()

cr.execute(
    """INSERT INTO Finance VALUES
    (1,'True/False: Net income is calculated by subtracting total expenses from total revenues on the balance sheet.','False'),
    (2,'Operating cash flow excludes cash flows from which of the following activities?
    a. Financing
    b. Investing
    c. Operating
    d. All of the above','d'),
    (3,"Operating cash flow represents the cash generated from a company's normal business ________.",'operations'),
    (4,"Which ratio measures a company's short-term liquidity?
    a. Debt-to-equity ratio
    b. Return on equity
    c. Current ratio
    d. Price-earnings ratio",'c'),
    (5,'True/False: A high debt-to-equity ratio indicates a low level of financial risk.','False')"""
    )

