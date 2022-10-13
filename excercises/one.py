name = 'muhammed'
age = 15

print(f'my name is {name} and my age is: {age}')
print('my name is {} and my ade is: {} '.format(name,age))
print('my name is  %s  and my age is:  %d  '%(name ,age))
print( 'my name is ' + name + 'my age is=> '  + str(age) )

print(name.split())

d = 'hellow how are you'

t=d.split()
t.reverse()
print(' '.join(t))

# =================================================================================================================
import random

# name = input("What is your name? ")
# print("Good Luck! " + name)

# names = ['hadi', 'yara', 'hasan', 'sara', 'osama']

# word = random.choice(names)

# print("the name is:")

# guesses = ''                 # => if user press enter without write anything

# turns = 12

# while turns > 0:

#     failed = 0

#     for char in word:

#         if char in guesses:
#             print(char)

#         else:
#             print("_")
#             failed += 1

#     if failed == 0:
#         print("You Win")
#         print("The name is: ", word)
#         break

#     guess = input("guess a character:")

#     guesses += guess

#     if guess not in word:
#         turns -= 1
#         print("Wrong guess")
#         print("You have", + turns, 'more guesses')

#         if turns == 0:
#             print("You Loose")


#= ==============================================================================================================

# while True:
#     if name == '':                        # if user press entre
        
#         break


di = {
    'one':'muhammed','two':'ahmed','three':'hussain'
 }

print(di)
di.update({'one':'osama'})
print(di)

# ==============================================================================================================
import re

pattern = (r'\d{3}-\d{4}-\d{4}')
text = 'my phone number is 010-2949-1006 if you need to call me'

def fun():
    is_right = re.search(pattern , text)
    if is_right :
        print('identical')
        print(is_right)

    else:
        False
fun()

# ==============================================================================================================


# phone_number = input('entre your phone number: ')
# searsh_phone = re.findall(r'\d{3}-\d{4}-\d{4}',phone_number)
# p = []
# if searsh_phone == [] :
#     False
# else:
#     p.append(searsh_phone)
#     print(p)


#= ====================================================================================

date = '27-09-2022'
d = re.search(r'(\d{2})-(\d{2})-(\d{4})' ,date)
day = d.group(1)
month = d.group(2)
year = d.group(3)
print(f'the day is {day} and the month is {month} and the year is {year}')

#  =>>>>>        please Notice      =<<<<<<<<<<<<<<<<<<<<<
j , l , p = d.groups()
print(l)

from pathlib import Path
str(Path('Users','Public',))