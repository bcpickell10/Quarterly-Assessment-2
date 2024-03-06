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

cr.execute(
    """INSERT INTO Business_Management VALUES
    (1,'True/False: Ethical decision making involves considering only the short-term consequences of actions.','False'),
    (2,'Multiple Choice: Which of the following is NOT a step in the ethical decision-making process?
    a. Identifying the ethical dilemma
    b. Evaluating potential consequences
    c. Ignoring the consequences of actions
    d. Making a decision and taking action','c'),
    (3,'True/False: Ethical leaders prioritize personal gains over the well-being of their team and organization.','False'),
    (4,'Ethical leaders demonstrate ________ by holding themselves and others accountable for their actions.','accountability'),
    (5,'Upholding core ________ such as honesty and integrity contributes to fostering an ethical workplace culture.','values')"""
)

cr.execute(
    """INSERT INTO Analytical_Thinking VALUES
    (1,'True/False: Critical thinking involves accepting information at face value without questioning its validity.','False'),
    (2,'True/False: Professionalism in the workplace includes demonstrating integrity and ethical behavior.','True'),
    (3,'What does professionalism entail in a business setting?
    a. Dressing formally at all times
    b. Following ethical guidelines and standards
    c. Ignoring deadlines and commitments
    d. Avoiding collaboration with colleagues','b'),
    (4,'Effective problem-solving requires a ________ approach, considering various perspectives and potential solutions.','systematic'),
    (5,'Which of the following is NOT a step in effective problem-solving?
    a. Identifying the root cause of the problem
    b. Implementing the first solution that comes to mind
    c. Evaluating potential solutions
    d. Monitoring the outcomes of the chosen solution','b')"""
)

cr.execute(
    """INSERT INTO Apps_Development VALUES
    (1,'True/False: Python is a compiled programming language, meaning code is translated into machine language before execution.','False'),
    (2,'In Python, a ________ is a collection of items that are ordered and changeable.','list'),
    (3,' In Python, the ________ method is used to execute SQL queries on an SQLite database.','execute'),
    (4,'Which SQL statement is used to retrieve data from a database?
    a. SELECT
    b. UPDATE
    c. DELETE
    d. INSERT','b'),
    (5,'The ________ statement in SQL is used to add new records to a database table.','INSERT')"""
)