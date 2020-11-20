import os

files = os.walk(r"c:\classroom\oct13")

for dirname, folders, files in files:
    for f in files:
        if f.endswith(".py"):
            print(dirname + "\\" + f)
