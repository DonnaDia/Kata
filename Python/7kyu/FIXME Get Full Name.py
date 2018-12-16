#Vers3
class Dinglemouse(object):
    def __init__(self, first, last):
        self.name = '{} {}'.format(first, last).strip()
    def get_full_name(self):
        return self.name


#Vers2
class Dinglemouse(object):
    def __init__(self, first_name = '', last_name = ''):
        self.first_name = first_name
        self.last_name = last_name
    def get_full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return('')



#Works-on-my-machine version
class Dinglemouse(object):
    def __init__(self, first_name = '', last_name = ''):
        self.first_name = first_name
        self.last_name = last_name
    def get_full_name(self):
        if self.first_name and self.last_name:
            print(self.first_name + ' ' + self.last_name)
        elif self.first_name:
            print(self.first_name)
        elif self.last_name:
            print(self.last_name)