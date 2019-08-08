Classy-Classes
#1
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def message(self):
        print('{}s age is {}'.format(self.name,self.age))

user = Person('John', 34)

Person.message(user)

#2
class Person():
    def __init__(self,name,age):
        self.info = name + 's age is ' + str(age)

user = Person('John', 34)

print(user.info)

#3
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        return self.name + 's age is ' + str(self.age)

user = Person('John', 34)

print(user.info())

#4
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name + 's age is ' + str(self.age))

user = Person('John', 34)
user2 = Person('Bonny', 96)

user.info()
user2.info()

#5
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @property
    def info(self):
        return self.name + 's age is ' + str(self.age)