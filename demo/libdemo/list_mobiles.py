with open("mobiles.txt", "rt") as f:
    mobiles = set()
    for line in f:
        parts = line.strip().split(",")
        for mobile in parts:
            if len(mobile) == 10 and mobile.isdigit():
                mobiles.add(mobile)

for mobile in sorted(mobiles):
    print(mobile)
