# Read all non-blank lines into list
with open("names.txt", "rt") as f:
    lines = [line for line in f if len(line.strip()) > 0]

# Write all non-blank lines back to file
with open("names.txt", "wt") as f:
    for line in lines:
        f.write(line)
