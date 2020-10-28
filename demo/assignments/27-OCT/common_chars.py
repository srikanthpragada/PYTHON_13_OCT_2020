names = ['scott', 'stoves', "tyson", "robers"]

common_chars = set(names[0])

for name in names[1:]:
    common_chars = common_chars & set(name)
    #print(common_chars)

print(common_chars)
