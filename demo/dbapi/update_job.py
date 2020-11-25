import sqlite3

con = sqlite3.connect(r"c:\classroom\oct13\hr.db")
cur = con.cursor()
id = input("Id :")
salary = input("New Min Salary : ")
try:
    cur.execute("update jobs set minsalary = ? where id = ?", (salary,id))
    if cur.rowcount == 1:
        print("Updated Successfully!")
        con.commit()
    else:
        print("Job id is not found!")
except Exception as ex:
    print(ex)
    print("Sorry! Could not update job due to error!")


con.close()
