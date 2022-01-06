class User:
    def __init__ (self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self,amount):
        self.account_balance -= amount

amani = User("Amani Mkamba", "amani@gmail.com")
imani = User("Imani Lania", "imani@gmail.com")

amani.make_deposit(500)
amani.make_withdrawal(400)
imani.make_deposit(200)
imani.make_withdrawal(300)

print(amani.account_balance)
print(imani.account_balance)

#.......................................

class User:
    def __init__ (self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def greeting(self):
        print(f"Hello my name is {self.first_name} {self.last_name} and I am {self.age} years old!")

amani = User("Amani", "Mkamba", 31)
amani.greeting()
