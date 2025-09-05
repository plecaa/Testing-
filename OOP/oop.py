class Dog:
    def __init__ (self,name, age):
        self.name = name
        self.age = age
        
m = Dog('Tommy', 9)
print(m.name)
print(m.age) 

          
class Arnold:
     def walk(self):
          print('ill be back...!')
          print('i am walking...!')
          print('hasta la vista baby...!')
     def talk(self):
          print('Oh check i can talk...!')
          print('hello there...!')
          print('get to the chopper...!')  
     def eat(self):
          print('i am eating...!')
          print('i love to eat...!')
          print('i can eat a lot...!')    

p = Arnold()
p.walk()
p.talk()
p.eat()
print(type(p))        