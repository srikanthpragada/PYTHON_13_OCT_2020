def wish(name='Guest', message='Hi'):
    print(message, name)


wish("Larry", "Hello")  # Positional arguments 
wish("Bill")
wish()
wish(message='Hello')  # Keyword argument
wish(message='Hello', name='Jack')  # Keyword arguments
