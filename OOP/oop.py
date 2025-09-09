class Dog:
    def __init__ (self,name, age):
        self.name = name
        self.age = age
        
m = Dog('Tommy', 9)
pf = Dog('Rex', 3)
print(m.name)
print(m.age) 
print(pf.name)

          
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

class Students:
     def __init__(self, name, age, grade):
          self.name = name
          self.age = age
          self.grade = grade   # 0 -100

     def get_grade(self):
          return self.grade    

class Course:
     def __init__(self, name, max_students):
          self.name = name
          self.max_students = max_students
          self.students = []

     def add_student(self, student):
          if len(self.students)< self.max_students:
               self.students.append(student)
               return True
          return False
     def get_avarage_grade(self):
          pass

s1 = Students('lunza', 20, 80)  
s2 = Students('Tiana', 10, 60) 
s3 = Students('Granet', 14, 76) 
s4 = Students('Tasha', 19, 90) 

course = Course('math', 3)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)

          
                

         
