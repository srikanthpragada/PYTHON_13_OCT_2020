import json


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


c = Contact("Abc", "39393933", "abc@gmail.com")
json_object = json.dumps(c.__dict__)
print(json_object)
dict_object = json.loads(json_object)
print(dict_object)


