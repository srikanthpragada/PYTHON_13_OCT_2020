def wish_all(*names, message='Hi'):
    for n in names:
        print(message, n)


wish_all("Jack", "Joe", )
wish_all("Larry", "George", "Mike")
wish_all("Bill", 'Steve', message="Hello")
