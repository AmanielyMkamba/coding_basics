"""

class User:
    bank_name = "First National Dojo"
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@dojo.com"
        self.account_balance = 0

#instances
michael = User()
anna = User()

User()
guido = User()
monty = User()

print(guido.name)
print(monty.name)

guido.name = "Guido"
monty.name = "Monty"
guido.bank_name = "Dojo Credit Union"

print(guido.name)
print(monty.name)

print(guido.bank_name)
print(monty.bank_name)

User.bank_name = "Bank Of Dojo"

print(monty.bank_name)
print(michael.bank_name)

#attributes -characteristics shared by instances class type
#methods - actionsions/funct an obect can perform eg deposit withdrawal or send
#self - is the represenattion of the instance

"""

class User:
    bank_name = "First National Dojo"
    def __init__ (self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
amani = User("Amani Mkamba", "amani@mkamba.com")
imani = User("Imani LAnia", "imani@lania.com")

print(amani.name)
print(imani.email)
print(imani.account_balance)