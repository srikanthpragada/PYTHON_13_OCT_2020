import sqlite3

con = sqlite3.connect(r"c:\classroom\oct13\hr.db")
cur = con.cursor()
title = input("Title    :")
minsalary = input("Min Salary : ")

cur.execute("insert into jobs(title,minsalary) values(?,?)", (title, minsalary))
print(f"Inserted {cur.rowcount} row(s)")
con.commit()
con.close()
