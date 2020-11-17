v = input("Enter number :")
try:
    num = int(v)
    print(100 / num)
except Exception as ex:
    print('Error :', ex)

print("The End!")
