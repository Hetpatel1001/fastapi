from pydantic import BaseModel

class User:
    def __init__(self,username, firstname, lastname, pincode, email):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.pincode = pincode
        self.email = email