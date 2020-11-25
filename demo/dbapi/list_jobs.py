import sqlite3

try:
    con = sqlite3.connect(r"c:\classroom\oct13\hr.db")
except Exception as ex:
    print("Could not connect to database! Error :", ex)
    exit(1)  # Terminate with error

try:
    cur = con.cursor()
    cur.execute("select * from jobs")
    for id, title, minsal in cur.fetchall():
        print(f"{id:5} {title:30}  {minsal:10}")
except Exception as ex:
    print(ex)
finally:
    con.close()
