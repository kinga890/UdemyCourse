#                                   OBJECT ORIENTED PROGRAMMING
# #Given the below class:
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# # 1 Instantiate the Cat object with 3 cats
# cat1 = Cat('Maciej', 17)
# cat2 = Cat('Kacper', 91)
# cat3 = Cat('Bartek', 19)
#
#
# # 2 Create a function that finds the oldest cat
# def oldest(*args):
#     return (max(*args))
#
# g = oldest(cat1.age,cat3.age,cat2.age)
#
#
# # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
#
# print(f'The oldest cat is {g} years old')

# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# #1 Add another Cat
#
# class Maciej(Cat):
#     def activity(self):
#         return 'eating'
#
# #2 Create a list of all of the pets (create 3 cat instances from the above)
#
#
# cat1 = Maciej('Maciej', 19)
# cat2= Sally('Bartek', 17)
# cat3 = Simon('Kacper', 16)
#
# my_cats = [cat1, cat2, cat3]
#
# #3 Instantiate the Pet class with all your cats use variable my_pets
#
# my_pets = Pets(my_cats)
#
# #4 Output all of the cats walking using the my_pets instance
#
# print(my_pets.walk())
#
# my_pets.walk()
#
# class SuperList(list):
#     def __len__(self):
#         return 1000
#
# obj1 = SuperList()
#
# print(obj1.__len__())

# class PlayerCharacter:
#     membership = True
#     def __init__(self,name,age,lvl):         #self refers to the PlayerCharacter
#         if PlayerCharacter.membership:       # MEMBERSHIP jest globalne dla Class, więc można PlayerCharacter lub self
#           self.name=name        #ATTRIBUTES/PROPERTIES so no ()   (właściwości)
#           self.age=age
#           self.lvl=lvl
#     def run(self):      #METHOD so ()
#         print('run')
#         return ''
#     def shout(self):
#         print(f'My name is {self.name}')   # self.name bo NAME jest lokalne
#         return ''
#
# player1 = PlayerCharacter('Cindy', 29, 90)
# player2 = PlayerCharacter('Bart', 80, 19)
#
# print(player1.age)       #the dot notation allows us to access the attribute/property
# print(player2.run())
#
# player2.attack=50
#
# print(player2.attack)   #mogę to wyprintować ale to jest osobna cecha dla player2 i nie zadziała dla nikogo innego
#                         # (jest poza class)
#
# print(player2.shout())
# ---
# class PlayerCharacter:
#     membership = True
#     def __init__(self, name='anonymous', age=0):
#         if (age >= 18):
#             self.name = name #attributes
#             self.age = age
#     def shout(self):
#         print(f'my name is {self.name}')
#
# player1 = PlayerCharacter('Matt',10)
#
# print(player1.name)
# ---
#
# class PlayerCharacter:
#     membership = True
#     def __init__(self, name='anonymous', age=0):
#         if (age > 18):
#             self.name = name #attributes
#             self.age = age
#     def shout(self):
#         print(f'my name is {self.name}')
#     @classmethod      #WE CAN USE THIS WITHOUT INSTANTIATING A CLASS
#     def adding_things(cls, t1,t2):      #cls parameter for CLASS
#         return t1 + t2
#     @classmethod   #instantiating an object with classmethod
#     def adding_things2(cls,num1,num2):
#         return cls('Teddy', num1+num2)
#
# player1 = PlayerCharacter('Matt', 29)
#
# print(player1.adding_things('cobble ', 'dirt'))
#
# print(PlayerCharacter.adding_things('cobble ','dirt'))
# # CLASSMETHODS = METHODS ON THE ACTUAL CLASS
#
# player3 = PlayerCharacter.adding_things2(30,3)  #new object created by using CLASSMETHOD
# print(player3.name)
#
# ---
# class friend:
#     sex = 'male'
#     favgame = 'Dark Souls'
#     def __init__(self,name='anonymous', age=16):
#       self.name = name
#       self.age = age
#     @staticmethod
#     def adding_things(num1,num2):  #NO SELF OR CLS
#       return num1 + num2
# kacper = friend()
# print(kacper.adding_things(4,5))
# ---
# class NameOfClass():
#     class_attribute = 'value'
#     def __init__(self, param1,param2):
#         self.param1= param1
#         self.param2= param2
#     def method(self):
#       #code
#     @classmethod
#     def cls_method(cls, p1, p2):
#       #code
#     @staticmethod
#     def stc_method(pp1, pp2):
#      #code
# ---
# class User():       #parent class to Slenderman
#     def sign_in(self):
#         print('logged in')
#         return ''
#
# class Slenderman(User):     #children (subclass;derived) to User, parent to Skeleton
#     def __init__(self,item1,item2):
#         self.item1=item1
#         self.item2=item2
#
# class Skeleton(Slenderman):   #children to Slenderman
#     pass
#
# maciej = Skeleton('dirt', 'cobble')
#
# print(maciej.sign_in())
# ----
# class User():       #parent class to Slenderman
#     def sign_in(self):
#         print('logged in')
#         return ''
#     def attack(self):
#         print('do nothing')
#
# class Slenderman(User):     #children (subclass;derived) to User, parent to Skeleton
#     def __init__(self,item1,item2):
#         self.item1=item1
#         self.item2=item2
#     def attack(self):
#         User.attack(self)        #można z rodzica sobie brać
#         print(f'i attack with {self.item1}')        #można nadpisać to co było w rodzicu
#         return ''
# class Skeleton(User):   #children to Slenderman
#     def attack(self):
#         print(f'i like dogs')
#         return''
#
# player1 = Slenderman('dirt', 'cobblestone')
# player2= Skeleton()
#
# def attack(player1,player2):
#     print(player1.attack())
#     print(player2.attack())
#     return ''
#
# print(attack(player1,player2))
#
# for char in [player1,player2]:
#     print(char.attack())
# ---
# MULTIPLE INHERITANCE
# class User:
#     def log(self):
#         return 'logged in'
#
# class Steve(User):
#     def __init__(self,pants,armor):
#         self.pants=pants
#         self.armor=armor
#     def sound(self):
#         return 'AAAAAA'
# class Alex(User):
#     def __init__(self, helmet, sword):
#         self.helmet=helmet
#         self.sword=sword
#     def fightsound(self):
#         return f'i attack you with {self.sword} sword'
#
# class Wolf(Steve,Alex):
#     def __init__(self,pants,armor,helmet,sword):
#       Steve.__init__(self,pants,armor)
#       Alex.__init__(self, helmet,sword)
#
# obj1= Wolf('diamond','gold', 'iron','gummy' )
# print(obj1.fightsound())
# print(obj1.sound())
# print(obj1.log())
#

#                              FUNCTIONAL PROGRAMMING

# from functools import reduce

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5,4,3,2,1]
#
# g = ((sorted(list(zip(my_numbers,my_strings)))))
#
# print(g)

# or

# print(tuple(zip(sorted(my_numbers),my_strings)))  # tu jest lepiej bo sortuję faktycznie tylko listę numerów

# 3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]
#
#
# def func(x):
#   return x > 50
#
# print(list(filter(func,scores)))
#
# #4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
#
# def accumulator(acc,item):
#   return acc+item
#
# print(reduce(accumulator,my_numbers + scores,0))

# ----------
#
# my_list=[1,2,3,4,5,6,7,8,9]
#
# print(list(filter(lambda item: item % 2 == 0, my_list)))
#
# print(reduce(lambda item,acc: acc+item, my_list,0))
#
# -------
#
# my_list=[5,4,3]
#
# print(list(map(lambda x: x**2,my_list)))
#
# a = [(0,2), (4,3), (9,9), (10,-1)]
#
# y = (sorted(a, key= lambda x: x[1]))
#
# print(y)
#
# cars = ['Ford', 'BMW', 'Volvo']
#
# cars.sort(reverse=True)
# print(cars)
#
# -------
#
# my_dict = {key:key**2 for key in [1,2,3]}
#
# print(my_dict)
#
# ------
#
# some_list = ['a','b','b','c','d','m','n','n']
# duplicates = []
# for x in some_list:
#     if some_list.count(x) > 1 and x not in duplicates:
#         duplicates.append(x)
#
# print(duplicates)
#
# duplicates2 =  { x for x in some_list if some_list.count(x) > 1 }
#
# print(duplicates2)
#
# ---------
#
# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         func(*args, **kwargs)
#     return wrap_func
#
# --------
#                                   DECORATORS
# from time import time
#
# def performance(func):
#     def wrap_func():
#         t1=time()
#         result = func()
#         t2=time()
#         print(f'{t2-t1}')
#         return result
#     return wrap_func
#
# @performance
# def blahblahblah():
#     for i in range(100):
#         i*5
#
# blahblahblah()
#
# ---------
#
# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
# user2 = {
#     'name': 'Sorna',
#     'valid': True
# }
#
# def authenticated(fn):
#   def wrapper(*args,**kwargs):
#     if args[0]['valid'] is True:
#         return fn(*args, **kwargs)
#   return wrapper
#
#
# @authenticated
# def message_friends(user):
#     print('message has been sent')
#
# message_friends(user2)

# Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0]
# ]
#
# for value in picture:
#     for pixel in value:
#         if pixel == 0:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print('')
#
# print('Ala', end='@')
# print('Dominika')


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# prev = 0
# for value in my_list:
#     outcome = value + prev
#     prev = outcome
#     print(outcome)
#
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#
# my_list = []
# output_list = []
# for value in some_list:
#     if value not in my_list:
#         my_list.append(value)
#     else:
#         output_list.append(value)
#
# print(output_list)

#
# # 2 sposób:
# # .count
#
# def counter(n1, n2):
#     def counter2():
#         return n1 + n2
#
#     return counter2
#
#
# total = counter(10, 20)

# print(total())
#
#
# def checkDriverAge(age=0):
#     if int(age) < 18:
#         print("Sorry, you are too young to drive this car. Powering off")
#     elif int(age) > 18:
#         print("Powering On. Enjoy the ride!");
#     elif int(age) == 18:
#         print("Congratulations on your first year of driving. Enjoy the ride!")
#
#
# # checkDriverAge()
#
#
# def my_func(*args, **kwargs):
#     total = 0
#     for value in kwargs.values():
#         total += value
#     return sum(args) + total
#
#
# print(my_func(1, 2, 3, 4, 5, num1=10, num2=5))
#
# my_list = []
#
#
# def highest_even(args):
#     for value in args:
#         if value % 2 == 0:
#             my_list.append(value)
#     return (max(my_list))
#
#
# print((highest_even([2, 6, 8, 32, 11, 45, 17, 18])))
#
# total = 0
#
#
# def count(total):
#     total += 1
#     return total
#
#
# print(count(count(count(total))))  # =3
#
# print(total)  # =0
#
# class New:
#     pass
#
# obj1 = New()
#
# print(type(obj1))
#
# ERRORS HANDLING
#
# while True:
#     try:
#         age = int(input('What is your age? '))
#         print(5/age)
#     except ZeroDivisionError:
#         print('you can\'t be 0 years old')
#     except:
#         print('no specific error')
#     else:
#         break
#
# def generator_function(num):
#     for i in range(num):
#         yield i
#
# g = generator_function(100)
#
# next(g)
# print(next(g))
#
# from time import time
#
# def performance(func):
#     def wrap_func(*args,**kwargs):
#         time1 = time()
#         lol=func(*args,**kwargs)
#         time2 = time()
#         result = time2 - time1
#         print(result)
#         return lol
#
#     return wrap_func
#
# @performance
# def how_long():
#     for i in range(100):
#         print('i')
# @performance
# def how_long2():
#     for i in list(range(100)):
#         return i
#
# how_long()
# how_long2()

#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
#
# for value in picture:
#     for pixel in value:
#         if pixel == 0:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print('')

# with open('nonexistingfile.txt', mode ='w') as my_file:
#     text = my_file.write('DAMNNNN')
#     print(text)

# import re

# string = 'wassup my name is Kinga and i like dogs and cats '
#
# pattern = re.compile(r'([a-zA-Z]).([K])')
#
# a = pattern.search(string)
#
# print(a.group(2))

# def do_stuff(num):
#     try:
#             return num + 5
#     except TypeError as Err:
#         return Err


#
# def x():
#     raise ValueError
#
# def r():
#     return TypeError
#
#
# print(r())












