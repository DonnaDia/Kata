Basic subclasses---Adam-and-Eve
#1
def God():
    return [Man(), Woman()]
    
class Human():
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

#2
def God():
    return [Man("Adam"), Woman("Eve")]

class Human:
   def __init__(self, name):
      self.name = name

class Man(Human):
   def __init__(self, name):
      super().__init__(name)

class Woman(Human):
   def __init__(self, name):
      super().__init__(name)

#3
class Human():
    pass
class Man(Human):
    pass
class Woman(Human):
    pass
    
def God():
    Adam = Man()
    Eve  = Woman()
    return [Adam, Eve]