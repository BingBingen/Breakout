''' Comments
for Comments. Multiline () and for single lines use '#'.  
'''

''' Print Statement
print("Hello", "end", 87, False, end = '|') #end can change the behavior of the print statement. Sort of like changing from block to inline 
print("bye")
'''

''' Variables
hello = 'tim'
world = 'world'
world = hello
hello = 'no'

print(hello, world);

#naming Conventions: In a variable, you cannot use special characters and you cannot start with a number.
#For multiple word, use camel [highLowerBig] or snake [high_Lower_Big]. 
'''

''' User Input
input('Name: '); 
age = input('Number: ');
print('Hello,', 'you are', age, 'years old');
'''

''' Arithmetic Operator 
# exponent: **, floor division: // [integer result] , mod: %, 
# Python follows BEDMAS [brackets, exponents, divison, multiple, addition, subtraction]
# integer division and mod are in the lowest order of operations

x = 9 
y = 3
result = int(x / y)
print(result)

num = input('Number: ') #inputs outputs str 
print(int(num) - 5)
'''

''' String Methods
hello = 'hello ll Bigll'
print(type(hello)) #here you will see that in Python, everything is an object. Thus, all instances have some method & attribute. 
print(hello.upper().count('LL'))
#Some useful methods [functions] include: upper(), lower(), Capitalize(), count()
'''

''' Condtionals Operators + String multiplication & addition
x = 'hello '
y = 3
z = 'big'
print(x * y, x + z);

#----------

# ==: equality.         != : inequality       <=.     >=    
x = 'hello'
y = 'hello'
print(x == y);

# string comparison exists. a > z. Every character is represented by some ASCII code. View this value using ord()
print(ord('a'))
print(ord('Z')) #Thus,
print('a' > 'Z') #True
'''

''' Chained Conditional [and, or, ]
x = 7
y = 8
z = 0

result1 = x == y
result2 = y > x 
result3 = z < x + 2

result4 = result1 or result2 or result3
print(result4)

#Order of priority: not, and, or. 
'''

''' If/Else/Elif
x = input('Name: ')

if x == 'Tim':
    print('You are great!')
elif x == 'Mark':
    print('Hi Markie')
else:
    print('No, you are not him')
'''

''' List [mutable]
x = [4, True, 'hi'] #can be multitype list
y = 'him'
z = x[:] #copy 

print(len(x), len(y)) #notice that len(y) == 3. each letter works like an element of a list
x.append('hello')
x.extend(['big', 'one'])
x.pop() #remove and return the last element of the list; however, you can specify
x.pop(0)
x[0] = 5. #lists are mutable because it stores a reference (pointer) not a copy

print(z, x)
'''

''' Tuples [inmutable]
x = (0,0,2,2)
print(x)

#cannot do anything like x[0] = 5 
'''

''' for loops
for i in range(10, -1, -1):
    print(i)

#range is a function which accepts the inputs (start, stop, step)

x = ['boom', 'boom', 'pow']
for i in range(len(x)):
    print(x[i])

print();

for i, element in enumerate(x): 
    print(i, element);
'''

''' while Loop
i = 0
while i < 10:
    print('run')
    i += 1 #i = i + 1

    if i == 9:
        break #only breaks inner while loop

'''

''' Slice operator
#Slice: takes a slice of a collection like a list or tuple
#sliced = [start:stop(non-inclusive):step]
x = [0,1,2,3,4,5,6,7,8]
y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
s = 'hello'

slice = x[0:4:2]; #start at index 0, stop at index 4, step by 2
print(slice)

slice = x[:4];  #start at index 0, stop at 4
print(slice)

slice = x[4:]; #start at index 4, go to the end
print(slice)

slice = x[::-1] #(reversing a list) start at index 0, go to the end, step by -1
print(slice)

slice = x[::2] 
print(slice)
'''

''' Sets
#Unordered unique collection of elements. There is no duplicates, we do not keep track of order. All we care is if something exist or does not. You only
#care about whether or not something exists. 

x = set()
s = {4,32,2,2} #set literal. Otherwise, if you use s = {}, this is a dictionary
ss = {1,9}
s2 = [4, 32, 2, 2] #list

s.add(5)
s.remove(5)
print(s)

print(2 in s2) #this method works for lists too? 
print(4 in s) #boolean Output : in constant time

#more methods of sets: s.union(s2), s.difference, intersection
'''

''' Dictionary
#Dictionaries are key|value pairs. Can hold multitype. Near constant time.
x = {'key' : 4}
print(x['key'])

x[False] = True
x[1] = 2

print(x)
print('key' in x) #checking for keys
print(x.values()) #print all values, most of the time you want to do list(x.values())

del x['key']

for key, value in x.items(): 
    print(key, ":", value) 

for key in x: #same as above
    print(key, x[key])
'''

''' Comprehension
# format : [Do this | for this collection | in this situation] 
# Example: [x + 1 for x in range(10) if x%2 == 2]
x = [i for i in range(101) if i % 5 == 0] 
print (x)

#This also works for dictionaries & set
x = {i:0 for i in range(100) if i % 5 == 0} #dictionary
x = {i for i in range(100) if i % 5 == 0} #set
'''

''' functions
def func():
    print('Run')
    def func():
        print('hi')
    func()

func()

#functions are actually objects which means you can technically return them  

def para(x,y):
    print('Run', x, y)

para(5,6)

def ret(x,y):
    print('Run', x, y)
    return x * y, x / y #if you return multiple things, it will return as a tuple

ans1, ans2 = ret(5,6)
print("multi ans: ", ans1 ,'\n',"div ans: ", ans2)
'''

''' Advanced functions
def func(x):
    def func2():
        print(x)

    return func2

print(func(3)) #call function with value 3. Just retuns func2

y = func(3) 
y() #this is also equivalent to func(3)()
'''

''' Astericks
x = [1,23,236363, 2727]
print(x)
print(*x) #unpack whatever we have in our collection of data



def func(x,y):
    print(x,y)

pairs = [(1,2), (3,4)]

#method 1
for pair in pairs: 
    func(pair[0], pair[1])

#method 2: instead we should use *. Unpacks them and separates
for pair in pairs: 
    func(*pair)

#unpacking for dictionaries requires two astericks
func(**{'x' : 2, 'y' : 5})
'''

''' *args & **kwargs
def func(*args, **kwargs): #arguments and keyword arguments
    print(*args, kwargs)

func(1,2,3,4,5,one=0,two=1)
'''

''' Scope and Global
x = 'tim' #global

def func(name):
    x = name #local

print(x)
func('changed')
print(x)
'''
 
''' Exception & Handle Exception
raise Exception('Bad')
raise FileExistsError('Strange')

--------
try: 
    x = 7 / 0
except Exception as e: #exception : general exception
    print(e)

finally: #runs no matter what
    print('finally')
'''

''' Lambda
#lambda: one line anonymous function 
x = lambda x, y: x + 5 + y
print(x(2, 32))
'''

''' Map and filter
#map : takes all the elemtns of a list and use a function to map them into a new list
x = [1,2,4,5,6,23,2,5]

mp = map(lambda i: i + 2, x) #first arg: function |  second arg: list 
print(list(mp))

#---------

#filter : returns true or false; whether or not we should include the item in our filtered list
fp = filter(lambda i: i % 2 == 0, x) #format filter(function, collection )

print(list(fp))
'''

''' F strings: creating and manipulating strings
name = 'Tim'
x = f'hello, my name is {name} and I am {67 + 9} years old'
print(x)
'''

#------------------------------- [OBJECT ORIENTED PROGRAMMING(OOP)]
''' Instantiating Objects and Creating classes
class Dog:
    def __init__(self, name, age): 
         self.name = name 
         self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

    def bark(self): 
        print("bark")

    def add_one(self, x):
        return x + 1
    
d = Dog("Tim", 19) #instantiation. #self is kind of like a pointer to the Instant. We always need to pass self because that's the location of the instant?
d2 = Dog("Bill", 20)

d.set_age(23)
print(d.name, d.age)
'''

''' Multi-Class
class Student: 
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100
    
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = [] #notice that this is an attribute that's not passed in.
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        pass

    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        
        return value / len(self.students)
s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 23, 75)
s3 = Student("Jill", 41, 85)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)

print(course.add_student(s3))
print(course.get_average_grade())

'''

''' Inheritance
#Child class gets priority. Similar to CSS in which ID > class
class Pet: #generalization. Parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')


    def speak(self):
        print("I don't know what I say")


class Cat(Pet):  #More specifc class. Inherits attribute from Pet class. This is called the CHILD CLASS
    def __init__(self, name, age, color):
        super().__init__(name, age) #The Super class is the class we inherit from aka Pet. 
        #Dont skip. Super is important for inheriting methods and attributes from the parent class.
        self.color = color

    def speak(self):
        print("Meow")
    

class Dog(Pet): #CHILD CLASS

    def speak(self):
        print("Bark")

p = Pet("Tim", 19)
p.show()

c = Cat("Bill", 34)
c.show()

d = Dog("Jill", 25)
d.show()
'''

''' Class Attributes & Class Methods
class Person: 
    number_of_people = 0 #Class attribute. Because it does not have
    #access to any methods or instants, it is defined for the entire class. Constant value: gravity, etc.  

    def __init__(self,name):
        self.name = name
        Person.add_person()

    @classmethod #not referencing to instances but to the class itself
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("tim")
p2 = Person("jill")

print(Person.number_of_people_())
'''

''' Static methods
class Math: #Creating your own methods 

    @staticmethod #these methods do not have access to the instances. They do something but they cannot change anything...  
    def add5(x):
        return x + 5

print(Math.add5(5))
'''


