'''str="orange","green","blue"
print(len(str))

age=10
if age >=10:
    print("you are adult")
else:
    print("you are minor")

score=85
if score>=90:
    print('A')
elif score>=80:
    print('B')
elif score>=70:
    print('C')
elif score>=60:
    print('D')
else:
    print('E')

is_raining=True
is_cold=False
if is_raining:
    print("Bring Umbrella")
    if is_cold:
        print("bring jacket")

num=0
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero") 

my_set={1,2,3}
my_set1={4,5}
my_set1.update({4,5})
my_set2=my_set.union(my_set1)
print(my_set2)
my_set.add(4)
print(my_set)
my_set.remove(2)
print(my_set)
my_set.discard(5)
print(my_set)
my_set.add(5)
print(my_set)

def find_intersection(set1,set2):
    intersection=set1.intersection(set2)
    return intersection
set1={'a','b','c'}
set2={'c','e','f'}
intersection=find_intersection(set1,set2)
print(intersection)

class Dog:
    def __init__(self,name):
       self.name = name
    
dog1=Dog("buddy")
print(dog1.name)
 
class car:
    def __init__(self,make,model):
        self.make=make
        self.model=model

car1=car("toyoto","camry")
car2=car("honda","civic")
print(car1.make,car1.model)
print(car2.make,car2.model)

class BankAccount:
    def __init__(self,account_number,balance):
        self._account_number=account_number
        self.__balance=balance
    def get_balance(self):
        return self.__balance
account1=BankAccount("12345",1000)
print(account1._account_number)
print(account1.get_balance())

class Animal:
    def __init__(self,name):
        self.name=name
    def speaks(self):
        pass

class Dog(Animal):
        def speak(self):
            return "woof"
        
class Cat(Animal):
        def speak(self):
            return "meww"
dog = Dog("buddy")
cat= Cat("whiskars")
print(dog.name,dog.speak())
print(cat.name,cat.speak())

s1={1,2,3}
s2={2,3,4}
s4=s2.symmetric_difference(s1)
print(s4)

s1={1,2,3}
s2={2,3,4}
s4=s2.difference(s1)
print(s4)

student={"name":"Sneha","Age":"18","Grade":"A"}
print(student)
student["Age"]=26
student["city"]="Hathras"
for key,value in student.items():
    print(f"{key}:{value}")
for key in student.keys():
    print(f"{key}")
for value in student.values():
    print(f"{value}")

squares={num:num**2 for num in range(1,6)}
print(squares)
squares={num:num*2 for num in range(1,6)}
print(squares)
student={"name":"Sneha","Age":"18","Grade":"A"}
print(student)
del student["Age"]
print(student)
Phone=student.get("Phone")
print(student)
dict={0:10,1:20}
print(dict)
dict[2]=30
print(dict)

dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

#1st program
d={'x':10,"y":20,"z":30}
for key,value in d.items():
    print(f"{key}:{value}")

#2nd program
n=int(input("enter a number"))
multiple={num:num*num for num in range(1,n)}
print(multiple)

#3rd program
n=16
squares={num:num**2 for num in range(1,n)}
print(squares)

#4th program
sum=0
my_dict={"data1":100,"data2":-54,"data3":247}
for value in my_dict.values():
     sum+=value
print(sum)

#5th program
color_dict={"Red":"#FF0000","Green":"#008000","Black":"#000000","White":"#FFFFF"}
print(sorted(color_dict.keys()))

#6th program
d={1:10,2:20,3:30,4:40,5:50,6:60}
print(d)
n=int(input("enter a key"))
if(n in d.keys()):
     print("true")

def my_fun():
    x=10     #x is local variable number
    print(x)
my_fun()

def even_num():
 score=85
 if score>=90:
    print('A')
 elif score>=80:
    print('B')
 elif score>=70:
    print('C')
 elif score>=60:
    print('D')
 else:
    print('E')

even_num()
     

z=10                   #x is global variable number
def my_function():
   print(z)

my_function()

z=10                   #z is global variable number
def my_function():
   global z            #using non-local variable number
   z=20
   
my_function()
print(z)

import random
def guess_number():
  attempt=0
while True:
  choose=int(input("enter any number between 1 to 100"))

target_number = guess_number()
attempts = 0

while True:
    user_guess = int(input("Enter number: "))
    attempts += 1

    if user_guess == target_number:
        print("Congratulation! You guessed the number in", attempts, "attempts.")
        break
    elif user_guess < target_number:
        print("Try a higher number.")
    else:
        print("Try a lower number.")'''

import random()
def num_game():
    random.randint(1,100)
target_number=num_game()
attempt=0
while True:
    guess=int(input("guess any number"))
    attempt += 1
    if (guess==target_number):
        print("congrats")

  











    























































