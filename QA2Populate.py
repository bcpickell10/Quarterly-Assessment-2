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

cr.execute(
    """INSERT INTO Analytics VALUES
    (1,'True/False: In regression analysis, the dependent variable is the variable being predicted or explained by the independent variable.','True'),
    (2,'In simple linear regression, the equation of the regression line is represented as Y = a + βX + ε, where a is the ________ and β is the regression coefficient.','intercept'),
    (3,'True/False: A p-value less than the significance level indicates that the null hypothesis should be rejected.','True'),
    (4,'The regression coefficient represents the ________ in the dependent variable for a one-unit change in the independent variable.','change'),
    (5,' If the regression coefficient of a variable is negative, what does it indicate?
    a. There is no relationship between the variables
    b. An increase in the independent variable is associated with a decrease in the dependent variable
    c. An increase in the independent variable is associated with an increase in the dependent variable
    d. The coefficient is not interpretable','c')"""
)