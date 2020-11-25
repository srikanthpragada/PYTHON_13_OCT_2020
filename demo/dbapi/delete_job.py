import sqlite3

con = sqlite3.connect(r"c:\classroom\oct13\hr.db")
cur = con.cursor()
id = input("Job Id :")
cur.execute("delete from jobs where id = ?", (id,))
if cur.rowcount == 1:
    print("Deleted Successfully!")
    con.commit()
else:
    print("Job Id not found!")

con.close()
