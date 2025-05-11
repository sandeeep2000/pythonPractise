# successful = True
# for number in range(3):
#     print("attempt")
#     if successful:
#         print("successful")
#         break

# else:
#     print("3 attempts already done")


# print(type(5))

# for x in "python":
#     print(x)

# command=""
# while command != "quit":
#     command = input(">")
#     print("Echo",command)

# count=0
# for number in range(1,10):
#     if number % 2 == 0:
#         print(number)
#         count=count+1

# print(f"we have {count} numbers")

# def greet(first_name,last_name):
#     print(f"Hi {first_name} how's it going")
#     print('welcome Aboard')

# greet("sandeep","charles")

# def increment(number=1,by=1):
#     return number + by

# print(increment(1))

# def multiply(*number):
#     total = 1
#     for i in number:
#         total = total * i
#     return total

# print(multiply(2, 3, 4, 5) ) # Output will be 120

# def save_user(**user):
#     print(user)

# save_user(id=1,name='john',age=22)

# message = "a"
# def greet(name):
#     message="b"

# greet("sandeep")
# print(message)

# def multiply(*number):
#     total = 1
#     for i in number:
#         total = total * i
#     return total


# print("start")
# print(multiply(1, 2, 3))


# def fizz_buzz(input):
#     if input%3==0 & input%5==0:
#         return "fizz_buzz"
#     elif input%5==0:
#         return "buzz"
#     elif input%3==0:
#         return "fizz_buzz"
#     else:
#         return input

# print(fizz_buzz(3))

# letters = ["a","b","c"]
# matrix = [[0,1],[2,3]]
# zeros = [0] * 100
# numbers = list(range(20))
# chars=list("Hello world")
# print(numbers)

# numbers = [1,2,3]
# # first = numbers[0]
# # second = numbers[1]
# # third = numbers[2]
# first,second,third=numbers
# print(first)

# numbers = [1,2,3,3,4,5,5,5,9]
# first,*other,last=numbers
# print(other)
# print(first,last)

# letters = ["a","b","c"]
# for letter in letters:
#  print(letter)

# adding and removing items in the list
# letters = ["a","b","c"]
# for letter in enumerate(letters):
#  print(letter)

# letters = ["a","b","c"]
# letters.append("d")
# letters.insert(0,"-")
# # print(letters)

# letters.pop()
# print(letters)

# letters=["a","b","c","d"]
# print(letters.index("d"))

# numbers = [1, 51, 2, 8, 6]
# sandeep = [1]
# numbers.sort()
# print(numbers)

# items = [
#     ("product1", 10),
#     ("product2", 9),
#     ("product3", 12)
# ]


# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item)
# print(items)

# items = [
#     ("product1", 10),
#     ("product2", 9),
#     ("product3", 12)
# ]

# prices = []
# for item in items:
#     prices.append(item[1])

# print(prices)

# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# print(list(zip(list1, list2)))

# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# print(browsing_session)
# last = browsing_session.pop()
# print(last)
# print(browsing_session)

# from collections import deque
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue)


# point = (1, 2) + (3, 4)
# print(point)

# point1 = (1, 2)*3
# print(point1)

# x = 10
# y = 11

# x, y = y, x

# print(x, y)

# numbers = [1, 1, 2, 3, 4]
# first = set(numbers)
# second = {1, 5}
# #  print(first | second)
# print(first ^ second)

# point = {"x": 1, "y": 2}
# point = dict(x=1, y=2)
# point["x"] = 10
# point["z"] = 20
# # print(point.get("a", 0))
# del point["x"]
# # print(point)

# for key in point:
#     print(key, point[key])


# values = []
# for x in range(5):
#     values.append(x*2)


# values = (x*2 for x in range(10))
# print(values)
# for x in values:
#     print(x)

# from pprint import pprint
# sentence = "This is a common interview question"
# char_frequency = {}
# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1
# pprint(char_frequency, width=1)
# try:
#     age = int(input("age:"))
# except (ValueError, ZeroDivisionError):
#     print("You did not enter a valid age")
# else:
#     print("No exceptions were thrown")

# from timeit import timeit
# code1 = """


# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("age cannot be zero")
#     return 10/age


# try:
#     calculate_xfactor(-1)

# except ValueError as error:
#     print(error)
# """

# print("first code=", timeit(code1, number=10000))

# class Point:
#     def draw(self):
#         print("draw")


# point = Point()
# print(type(point))
# print(isinstance(point, Point))


# class Robo:
#     def __init__(self):
#         self.x = 100
#         self.y = 200


# obj = Robo()
# print("addition=", (obj.x+obj.y))
# *************


# class Robo:
#     def __init__(self, x, y):
#         self.a = x
#         self.b = y


# obj = Robo(100, 200)
# print("addition =", obj.a+obj.b)


# class TagCloud:
#     def __init__(self):
#         self.tags = {}

#     def add(self, tag):


# class Product:
#     def __init__(self, price):
#         self.price = price


# product = Product()


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#          self.y = y

#     def __add__(self, other):
#         return Point(self.x+other.x, self.y+other.y)


# point = Point(10, 20)
# other = Point(1, 2)
# combined = point+other
# print(combined.x)


# class Product:
#     def __init__(self, price):
#         self.price = price


# class Animal:
#     def __init__(self):
#         print("animal constructor")
#         self.age = 1

#     def eat(self):
#         print("eat")


# class Mammal(Animal):
#     def __init__(self):
#         super().__init__()
#         print("mammal constructor")
#         self.weight = 2

#     def walk(self):
#         print("walk")


# m = Mammal()

# print(m.age)
# print(m.weight)


# class Employee:
#     def greet(self):
#         print("Employee Greet")


# class Person:
#     def greet(self):
#         print("person Greet")


# class Manager(Employee, Person):
#     pass


# manager = Manager()
# manager.greet()

# from abc import ABC, abstractmethod


# class InvalidOperationError(Exception):
#     pass


# class Stream(ABC):
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already Open")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already Close")
#         self.opened = False

#     @abstractmethod
#     def read(self):
#         pass


# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")


# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a network")


# stream = Stream()
# stream.open()

# class A:
#     def fun(self):
#         print("this is class A")


# class B:
#     def fun(self):
#         print("this is class B")


# class C:
#     def fun(self):
#         print("This is class C")


# obj1 = A()
# obj2 = B()
# obj3 = C()


# def poly(x):
#     x.fun()


# poly(obj2)

# import multipledispatch


# class A:
#     def add(self, a, b):
#         return a+b

#     def add(self, a, b, c):
#         return a+b+c

#     def add(self, a, b, c, d):
#         return a+b+c+d


# obj = A()
# print(obj.add(1, 2, 3))
# print(obj.add(1, 2))


# def sum(*args):
#     if args:
#         start = type(args[0])()
#         for i in args:
#             start += i
#         return start

# class A:
#     def fun(self):
#         print("this is class A")


# class B:
#     def fun(self):
#         print("This is class B")


# class C:
#     def fun(self):
#         print("this is class C")


# def poly(obj):
#     obj.fun()


# obj1 = A()
# obj2 = B()
# obj3 = C()


# poly(obj1)
# poly(obj2)


# from multipledispatch import dispatch


# class A:
#     @dispatch(int, int)
#     def add(self, a, b):
#         print(a+b)

#     @dispatch(int, int, int)
#     def add(self, a, b, c):
#         print(a+b+c)

#     @dispatch(str, str)
#     def add(self, a, b):
#         print(a+b)


# obj = A()

# obj.add('Hi', 'there')
# obj.add(1, 2)
# obj.add(1, 2, 3)

# class Text(str):
#     def duplicate(self):
#         return self+self
# text = Text("python")
# print(text.duplicate())

# from ecommerce.shopping.sales import calc_shipping, calc_tax

# import sys
# import ecommerce.shopping.sales


# calc_shipping()
# calc_tax()

# print("helo")


# from ecommerce.shopping import sales


# from pathlib import Path

# path = Path("ecommerce/__init__.py")
# path.exists()
# path.is_file()
# path.is_dir()
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)

# path.with_name("file.txt")


# from pathlib import Path
# from zipfile import ZipFile

# with ZipFile("files.zip", "w") as zip:
#     for path in Path("ecommerce").rglob("*.*"):
#         zip.write(path)

# import csv

# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1001, 2, 15])
#     writer.writerow([1002, 2, 10])

# with open("data.csv") as file:
#     reader = csv.reader(file)
#     # print(list(reader))
#     for row in reader:
#         print(row)

# import json
# from pathlib import Path

# # movies = [
# #     {"id": 1, "title": "Terminator", "year": 1989},
# #     {"id": 2, "title": "Kindergarten Cop", "year": 1993}
# # ]


# # data = json.dumps(movies)
# data = Path("movies.json").read_text()
# movies = json.loads(data)
# print(movies[0]["title"])


# import time
# import sqlite3
# import json
# from pathlib import Path

# # movies = json.loads(Path("movies.json").read_text())
# # print(movies)

# with sqlite3.connect("db.sqlite3") as conn:
#     # command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     # for movie in movies:
#     #     conn.execute(command, tuple(movie.values()))
#     # conn.commit()
#     command = "SELECT * FROM Movies"
#     cursor = conn.execute(command)
#     # for row in cursor:
#     #     print(row)
#     movies = cursor.fetchall()
#     print(movies)

# ***********


# def send_emails():
#     for i in range(10000):
#         pass

# import time
# start = time.time()

# send_emails()

# end = time.time()

# duration = end - start
# print(duration)


# from datetime import datetime
# import time
# dt = datetime(2018, 1, 1)
# dt = datetime.now()
# dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
# import string
# import random
# from datetime import datetime, timedelta
# dt = datetime.fromtimestamp(time.time())

# print(f"{dt.year}/{dt.month}")


# dt1 = datetime(2018, 1, 1)

# dt2 = datetime.now()

# duration = dt2-dt1
# print(duration)

# generating random values/numbers

# print(random.random())

# print(random.randint(1, 10))

# print(random.choice([1, 2, 3, 4]))
# print("".join(random.choices(string.ascii_letters+string.digits, k=4)))

# Opening a web browser


# import webbrowser

# print("deployment completed")
# webbrowser.open("https://google.com")


import smtplib
from string import Template
from pathlib import Path
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


template = Template(Path("template.html").read_text())


message = MIMEMultipart()
message["from"] = "Sandeep"
message["to"] = "charlessandeep1@gmail.com"
message["subject"] = "This is a test email"
body = template.substitute({"name": "john"})
# or body = template.substitute(name="john")
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path"mosh.png").read_bytes()))


    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("charlessandeep1.gmail.com", "Sandeep@2000")
    smtp.send_message(message)
    print("sent....")




# import subprocess

    completed = subprocess.run(["python3", "other.py"],
    capture_output = True, text = True)

   print("args", completed.returncode)
   print("returncode", completed.returncode)
   print("stderr", completed.stderr)
   print("stdout", completed.stdout)

   # pypi-python package index
    completed = property.deleter(-> none format )