import sqlite3

con = sqlite3.connect(r"c:\classroom\oct13\hr.db")

try:
    cur = con.cursor()
    cur.execute("select avg(minsalary) from jobs")
    avgsalary = cur.fetchone()[0]
    print(f"Average Min Salary :  {avgsalary:.0f}")
except Exception as ex:
    print(ex)
finally:
    con.close()
