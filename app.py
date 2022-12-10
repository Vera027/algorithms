import converter
from converter import lbs_to_kgs
import utils
import ecommerce.shipping
from ecommerce.shipping import calc_shipping
import random

ecommerce.shipping.calc_shipping()

course = "'Python's Course for Beginners"
# define a string with multi-lines
course1 = '''
Hi

Nice to meet you!
'''
print(course)
print(course1)

# format
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] ' + 'is a coder'
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)

# methods for string
course2 = 'Python for Beginners'
print(len(course2))
print(course2.upper())
print(course2.lower())
print(course2.find('n'))
print(course2.replace('Beginners', 'Absolute Beginners'))
# title() make the first letter in each word upper case
print('python' in course2)

# conditions
is_hot = True
is_cold = True

if is_hot:
    print("It's a hot day")
elif is_cold:
    print("It's a cold day")
else:
    print("It's a lovely day")
print("Enjoy your day")

# practice 1
price = 1000000
is_goodCredit = True
down_payment = 0
if is_goodCredit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print(f"Down payment: ${down_payment}")

has_high_income = True
has_high_credit = True

if has_high_income and has_high_credit:
    print("Eligible for loan")

# practice 2
'''
weight = int(input('Weight: '))
ask = input('(L)bs or (K)g: ')
if 'l' in ask or 'L' in ask:
    weight = round(weight*0.45359)
    msg1 = f'You are {weight} pounds'
    print(msg1)
else:
    weight = round(weight*2.20462)
    msg2 = f'You are {weight} kilograms'
    print(msg2)
'''

# while
i = 1
while i <= 5:
    print(i)
    i += 1
print('Done')

# guess a number
'''
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Sorry, you failed')
'''

# practice 3
'''
count_input = 0
while count_input < 10000000:
    user_input = input('>')
    count_input += 1
    if user_input == 'help':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
        while count_input < 1000000:
            user_input = input('>')
            count_input += 1
            if user_input == 'start':
                print('Car started... Ready to go!')
            elif user_input == 'stop':
                print('Car stopped.')
            elif user_input == 'quit':
                break
        break
    else:
        print("I don't understand that...")
'''

# for loop
for item in 'Python':
    print(item)

for item in [1, 2, 3, 4]:
    print(item)

for item in range(5, 10, 2):
    print(item)

prices = [10, 20, 30]
total_value = 0
for i in prices:
    total_value = i + total_value
print(f'Total: {total_value} dollars')

# nest loop
for x in range(4):
    for y in range(3):
        print(f' ({x}, {y})')

# practice 4
number = [5, 2, 5, 2, 2]
for i in number:
    i = 'x' * i
    print(i)

# list
name = ['John', 'bob', 'Sarah', 'Mary']
name[0] = 'Jon'
print(name)
print(name[1:3])

# find the max number in list a
a = [3, 5, 7, 9, 10, 4]
max_value = a[0]
for i in a:
    if i > max_value:
        max_value = i
print(max_value)

# 2D
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][2])

# list - mutable
number1 = [5, 2, 1, 7, 4]
number1.insert(0, 4)   # position 0 number 4
print(number1)
number1.remove(2)
print(number1)
number1.clear()   # remove all the list

number2 = [2, 4, 6, 7, 2, 3, 4]
uniques = []
for number in number2:
    if number not in uniques:
        uniques.append(number)
print(uniques)

# tuple - immutable
number3 = (1, 2, 3)
print(number3[0])

# unpacking
coordinates = (1, 2, 3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

x, y, z = coordinates

# dictionary
customer = {
    'name': 'John',
    'age': 30,
    'is_verified': True
}
print(customer['name'])
print(customer.get('birthdate', 'Jan 1 1980'))

# practice 5
phone = input('Phone: ')
phone_d = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four'
}
output = ''
for ch in phone:
    output += phone_d.get(ch, '!') + ' '
print(output)

msg = input('>')
word3 = msg.split(' ')
emojis = {
    ":)": "😀",
    ":(": "😞"
}
output1 = ' '
for w in word3:
    output1 += emojis.get(w, w) + ' '
print(output1)


# function
def greet_user(first_name, last_mame):
    print(f'Hi {first_name} {last_mame} there!')
    print('Welcome aboard!')


print('Start')
greet_user('John', 'Smith')
greet_user('Mary', 'Ng')
# calc_cost(total=50, shipping=5, discount=0.1)
print('Finish')


# return
def square(number):
    return number * number


result = square(3)
print(result)


def emojis_converter(user_input):
    msg1 = user_input.split(' ')
    emojis2 = {
        ':)': '😀',
        ':(': '😞'
    }
    output2 = ''
    for m in msg1:
        output2 += emojis2.get(m, m) + ' '
    return output2


user_input = input('>')
print(emojis_converter(user_input))

try:
    age = int(input('Age:'))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('Age can not be 0.')
except ValueError:
    print('Invalid value')


class Point:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point(10, 20)
point1.x = 10
point1.draw()
print(point1.x)


class Person:
    def __init__(self, name2):
        self.name2 = name2

    def talk(self):
        print(f"Hi, I am {self.name2}.")


person = Person('Mary')
person.talk()


# inheritance
class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


print(converter.kgs_to_lbs(70))
lbs_to_kgs(100)

print(utils.find_max([10, 4, 5, 3, 2]))

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))  # include 10 and 20

members = ['John', 'Bob', 'Mary']
leader = random.choice(members)
print(leader)


class Dice:
    def roll(self):
        x1 = random.randint(1, 6)
        y1 = random.randint(1, 6)
        result1 = (x1, y1)
        return result1


dice = Dice()
roll1 = dice.roll()
print(roll1)

















