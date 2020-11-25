import sqlite3

file = open("data.txt", "rt")
con = sqlite3.connect(r"c:\classroom\oct13\hr.db")
cur = con.cursor()
count = 0
for line in file.readlines():
    parts = line.split(",")
    if len(parts) != 2:
        continue

    try:
        cur.execute("insert into jobs(title,minsalary) values(?,?)", parts)
        print(f"{parts[0]} inserted successfully!")
        count += 1
    except:
        pass  # Ignore exception

con.commit()
con.close()
print(f"Loaded {count} rows!")
