#!/usr/bin/env python3

class UserData(object):
    def __init__(self,ID,Name):
        self.ID = ID
        self.Name = Name

class NewUser(UserData):
    group = 'shiyanlou-louplus'
    def __init__(self,ID,Name):
        self.ID = ID
        self._Name = Name

    def __call__(self,*args):
        print("{}'s id is {}".format(self.Name,self.ID))
    @property
    def Name(self):
        return self._Name
    @Name.setter
    def Name(self,value):
        if len(value) > 3:
            self._Name = value
        else:
            print('ERROR')
        
    def __repr__(self):
        return "ID:{} Name:{}".format(self.ID,self._Name)
    
    @classmethod
    def get_group(cls):
        return cls.group

    @staticmethod
    def format_userdata(ID,Name):
        print("{}'s id is {}".format(Name,ID))

if __name__ == '__main__':
    user = NewUser(101,'Jack')
    user()
  #  user1 = NewUser(101,'Jack')
  #  user1.Name = 'Lou'
   # user1.Name = 'Jackie'
   # user2 = NewUser(102,'Louplus')
   # print(user1.Name)
   # print(user2.Name)
