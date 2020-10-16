
# Calculate net amount by using 20% discount and 15% tax

sprice = input("Enter price :")
price = float(sprice)
discount = price * 0.20
gross_price = price - discount
tax = gross_price * 0.15
net_price = gross_price + tax

print("Net Price : ", net_price)








