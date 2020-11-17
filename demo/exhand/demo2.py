
v = input("Enter number :")
try:
    num = int(v)
    print(100 / num)
except ValueError:
    print("Invalid Number")
except ZeroDivisionError:
    print("Zero is a valid!")
except:
    print("Error!")

print("The End!")
