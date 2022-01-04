#print("hello amani is typing")
"""
Amani is typing
Amani is typing
Amani is typing
Amani is typing
Amani is typing

"""

#my_new_fav_lang = "Python"
#print(my_new_fav_lang)


#for i in range (10,15,20):
#    print(i)

"""
num = 5
if num < 3:
    print('less than 3')
else:
    print('bigger than 3')
"""

"""
name_age = ('Amani', 'Sheena', 35, False) #Tuple - immutable( can't add or remove/modified) use parathesis
#print(name_age[2])
#print(name_age[3])
name_age[0] = "Mkamba"
"""

"""
name_age = ['Amani', 'Sheena', 35, True] #Lits - mmutable use brakcets
#print(name_age[0])
#name_age[0] = 'Mkamba'
#print(name_age)
#name_age.pop()
#print(name_age)
name_age.append('Imani')
print(name_age)
print(type(name_age))
"""
"""
#Dictionaries - key and values, use curly brces
new_person = { 'first_name': 'Amani', 'last_name': 'Mkamba', 'age': '31', 'weight': '69Kg' }
#print(new_person['first_name'])
#print(new_person['age'])
#print(type(new_person))
new_person['hobbies'] = ['photography', 'playing gitar']
#print(new_person)
#w = new_person.pop('weight')
#print(w)
#print(new_person)
"""

"""
num = 3.4
print(type(num))

name = "Amani"
print(type(name))
print(len(name))

num_one = 1
print(type(num_one))

name = {'first_name': 'Amani', 'last_name': 'Mkamba'}
print(type(name))
print(len(name))
"""

"""
import random
rand_num = random.randint(2,10)
print(rand_num)
"""

"""
print(type(24))
print(type(23.44))

int_float = float(24)
print(int_float)

float_int = int(23.44)
print(float_int)

"""

"""
num_one = 5
num_two = 5.5
sum = num_one + num_two


print(int(sum))
"""

"""
name = "Amani"
print("My name is", name)
print("My name is" + " " + name)

age = 42
print("My age is", age)
print("My age is" + " " + str(age))
"""

"""
#interpolation
first_name = "Amani"
last_name = 'Mkamba'
full_name = 'amani mkamba'
age = 31
#print(f"My name is {first_name} {last_name} and I am {age} years old!")
#print("My name is {} {} and I am {} years old!".format(first_name, last_name, age))
#print("My name is %s %s and I am %d years old!" % (first_name, last_name, age))

print(full_name.title())
print(full_name.upper())
"""

"""
num = [1,2,3]
name = ['Amani', ['Sheena', 'Imani']]
num_name = num + name
#print(num_name)

names = 3 * name
#print(names)

#print(name[1][0])

nums = [1,2,3,4,5]
#print(nums[:])
#print(nums[1:])
#print(nums[1:4])
nums.append(6)

print(nums)
print(nums.index(6))
print(len(nums))
"""
"""
names = ('Amani', 'Sheena')
print(names[0])
print(type(names))
#names[0] = 'Imani'
names = names + ('Imani',)
print(names)
names = names[1:2] + ('is a wife to',) + names[0:1]
print(names)
"""

"""
names = {}
names['first_name'] = 'Amani'
names['last_name'] = 'Mkamba'
#print(names)

cities = { 'first_city': 'Dar', 'second_city': 'Allentown'}
#print(cities['second_city'])
#city = cities.pop('first_city')
#print(cities)
#del cities['first_city']
#print(cities)
#print(cities.keys())
#print(cities.values())


num = 6
num = 11
if num < 5:
    print('less than 5')
elif num > 10:
    print('bigger than 10')
else:
    print('Is number', num)
"""

#for i in range(5):
    #print(i)

#for num in range (5,10):
    #print(num)

#for num in range (0,10,2):
    #print(num)

#for char in 'Amani':
    #print(char)

"""
my_list = ['abc', 123, 'False']
#for i in range(0,len(my_list)):
    #print(i)
    #print(i, my_list[i])

for v in my_list:
    print(v)
"""

names = ("Amani", "Imani", "Sheena")
#print(type(names))
#for i in names:
    #print(i)

"""
my_dict = {'first_name': 'Amani', 'last_name': 'Mkamba'}
#for i in my_dict:
    #print(my_dict[i])

#for key in my_dict.keys():
    #print(key)

#for val in my_dict.values():
    #print(val)

for key, val in my_dict.items():
    print(key, '=' , val)
"""

"""
for num in range(0,5):
    print("cointing is", num)

else:
    print("False Statement")

num = 0
while num < 5:
    print("counting is", num)
    num+=1

else:
    print("False Statement")
"""

"""
for val in 'string':
    if val == 'i':
        break
    print(val)

for val in 'string':
    if val == 'i':
        continue
    print(val)


num = 5
while num >= 1:
    print(num)
    num-=1
    if num == 1:
        break
    else:
        'False final statement'
"""

"""
def add(a,b):
    x = a + b
    return x

new_val = add(3,4)
sum2 = add(5,5)
print(new_val)
print(sum2)

def hello(name):
    return (f"Hi World {name} is coding!")
#greeting = hello("")
greeting_one = hello('Amani')
greeting_two = hello('Imani')
print(greeting_two)

"""
"""
def greeting(name="Imani", repeat=2):
    return (f" Good day!, {name}.\n" * repeat)

print(greeting("Amani"))
print(greeting())
print(greeting(name='Sheena', repeat=4))
"""

def multiply(num_list, num):
    #print(num_list, num)
    for x in range(len(num_list)):
        #print(x)
        num_list[x] *= num
        #print(x)
        #print(num_list)
    return num_list
a = [2,4,10,16]
b = multiply(a,5)

print(b)









