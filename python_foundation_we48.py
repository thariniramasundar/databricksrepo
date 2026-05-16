#Refer python_theory/notes for understanding few basics of python...
'''
What we are going to learn in Python???
**1. Basic programming fundamentals -
A. Intent/Block based coding
B. Comments
C. Quotes
D. Variables & Values
E. Naming Conventions

F. Types and Casting
G. Input & Output operations
H. Datatypes (Simple/premetive or Complex/Collection (data structure))

I. Operators
J. Conditional Structure
K. Looping Constructs
L. Complex Types

#Specific to Python
2. Exception Handling

3. **FBP - Dataengineers (eg. leverage the spark functions writtern by somebody)

4. OOPS - Framework developers (eg. commiters/contributors of apache spark)
5. Building Apps/APIs/AI integration using Python Programming

'''

'''
Interpreter
line/line -> compiler -> object code -> vm -> execute
Compiler
entire line -> compiler -> object code -> vm -> execute

#execution example of both
Interpreter Example:
vi python_interpreter.py
name='Inceptez'
age=11
print(name)
#print(something)
print(age)
print("hello")
print("good morning")

#Interpret the line by line of code and execute
python python_interpreter.py

vi scala_compiler.scala
object obj1 extends App
{
var name="Inceptez"
var age=11
println(name)
printlnxyz(age)
println("hello")
println("good morning")
println("thank u")
}

#Compile the complete code and execute
scalac scala_compiler.scala
scala obj1

'''

print("************** 1. Basics of Python Programing*************")
print("How to run a python program")
#right click this module tab and run the program or go to run menu and run or click on the play button in the right top
#or type ctrl+shift+f10

#Fundamentals of Python Programming:
####################################
print("A. Python is an indent based programming language")
#Why Python uses indend based programing ->
#1. Managing the program more efficiently
#2. Better Readablility of the code
#3. For creating the hierarchy of programming.
#4. By default 4 spaces we will give for indends, but more/less spaces or tabs also can be used...

#Indendation is needed for (hierarchy of programming), because we are doing block operation (lines of code) with in the for loop


#Linux is not an intend based program, it is a block based rather:


#indendation has to be uniform within the block of code (not across the block of code)
#below prog doesnt work because we are using different number of spaces between lines of code in a given block


#below prog doesnt work because we are using different keys like spaces for one line and tab for another line


#optimal number of spaces has to be 4, but any numbers you can give


print("B. This is a commented line in Python")


print("C. Playing with Quotes: Python treats single quotes the same as double quotes as like triple quotes, but has some differences")
#Python treats single quotes the same as double quotes and triple quotes.



"""
>>> fruit='apple'
>>> type(fruit)
<class 'str'>
>>> fruit="apple"
>>> type(fruit)
<class 'str'>
>>> fruit='''apple'''
>>> type(fruit)
<class 'str'>
<class 'str'>
>>>

"""



#Double quotes is used for holding single quoted chars

company ="Inceptez tec's"

# value contains double quotes

company ='Inceptez tech"s'

##we can use escape sequence also

company='Inceptez tech\'s'

#Triple double quotes is used for muliline

sql_str=""" select * 
from emp
      where id=101
"""
#For handling paragraph/multilines text, we can use 3 single or doublequotes



#Any programming language learning has to be started first learning about variables


print("Let's learn all about VARIABLES")
'''1. Variable Properties - Dynamic Inference, Dynamic Typed, Strongly Typed'''

# variable -> holds the value in memory for reuse / name / identifier / label

tech="bigdata"

# tech -> variable
# bigdata -> value
# type -> str

# syntax : var_name=value (no need of dtype)

#Dynamic inference - based on the assigned value to a variable, it will automatically decides/infer/identify/refers the data type dynamically

#Dynamically typed: If a variable is created with a specific data type, can be changed later

msg ="program execution started ........"  # str - dynamic inference

print(msg)
print(type(msg))

msg =1000   # int    dynamic type

print(msg)
print(type(msg))



#below is possible, because python is dynamically typed language (Duck type language)


'''Scala is a statically typed language

#below is not possible - because of statically type feature

'''

#Strongly typed: Python allow us to operate between the variables of same datatype (of the same hierarchy) and doesn't allow to operate between different datatypes.


print("E. Naming Conventions")   # variable / module / packages / function / class

#A variable can have camel case or init upper or with underscores , snake case , pascal case

firstName="hadoop" # camel case
fullNameWithEmail="test"

Fullname="test user"    # initcase

full_name_with_email ="abc@gmail.com" # snake case

full_Name="iz tech"


# Variable name only have alpha / numbers / _


#A variable name must start with a letter or the underscore character

_price= 150



#A variable name cannot start with a number

# 2dept="csc" - not allowed in python


#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )

num1=150
num2=350
n3_num=500

res=num1+num2+n3_num

print(res)



#Variable names are case-sensitive

dept="CSC"

DEPT="civil"

print(dept,DEPT)


'''
>>> msg="hello"
>>> MSG="chennai"
>>> Msg="python"
>>>
>>>
>>>
>>> msg
'hello'
>>> MSG
'chennai'
>>> Msg
'python'
>>> mSG
Traceback (most recent call last):
  File "<python-input-40>", line 1, in <module>
    mSG
NameError: name 'mSG' is not defined. Did you mean: 'MSG'?
>>>
'''


#Multiple Variables can be assigned in a single line (Multi Assignment)

price , qty ,id = 100,5,"101a"

print(price)
print(qty)
print(id)

print("F. Types & Casting")

# numeric  -> int , float , complex number

# collection / complex types -> list , tuple , set , dict , str

# misc -> bool , bytes

# None - unknown / nothing / ( null in sql)
# int -
# we dont have any timy , small , byte , long in python , we have only onetype int

num =100

num :int=250 # mentioning type but that is a hint for our reference not for python

# type casting

# int() - python
# cast( '100' as int) - sql type casting

num = int("100") # string num to int

# how to check the data type of the variable

print(type(num))  # return type of the variable

# check the given var is int or not

print(isinstance(num,int))

msg="***************************************************"

msg



'''
>>> num=100
>>>
>>>
>>> isinstance(num,int)
True
>>> isinstance(num,str)
False
>>>
'''


'''
>>> int("100")
100
>>> int(125.50)
125
>>> int("125.0")
Traceback (most recent call last):
  File "<python-input-11>", line 1, in <module>
    int("125.0")
    ~~~^^^^^^^^^
ValueError: invalid literal for int() with base 10: '125.0'
>>> int(float("125.0"))
125
>>> int("hello")
Traceback (most recent call last):
  File "<python-input-13>", line 1, in <module>
    int("hello")
    ~~~^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'hello'
>>>

'''

# float - decimal

price=125.25

print(type(price))

print(isinstance(price,float))

# type casting

price =float(100)  # 100.0


# complex num

cnumber=100+10j

type(cnumber)

# exponential

amt=3e2

'''
>>> amt=3e2
>>> amt
300.0
>>> 3*(10*10)
300
>>> 125e3
125000.0
>>> amt
300.0
>>> amt=3e2
>>> type(amt)
<class 'float'>
>>> amt
300.0
>>>
'''


# str
# Sequence collection of characters / literals
# index based collection of char ( index start with 0)


fruit= "apple"

print(fruit[0])


for c in fruit:
      print(c)


# bool -> True or False

iselgbl=True
iselgbl:bool=True

'''
>>> bool("True")
True
>>> bool("False")
True
>>> bool(None)
False
>>> bool(0)
False
>>> bool(1)
True
>>> bool(100)
True
>>>
'''

print(iselgbl)

# type casting


# collection type / data struct

# list , tuple , set , dict, str

#3. How to check a given TYPE is of what datatype we expect  & type casting
#Functions we are learning in this topic ()
#What we are learning here is the usage of few functions like
#To understand the age is of what type

sal=5000

# get the type of the variable

print(type(sal))

#To check wheter the sal is of an expected type

# check sal is int or not

print(isinstance(sal,int))




#To convert the age to an expected type


#Check for a given type, if it is not as expected then cast it to the expected type programatically using if condition


print("G. Standard Input & output options")
#assigning value statically

#assigning value dynamically using input()

#print statement will be used as a std output function
#semi colon can be used to seperate a statment if we write multiple statements in one line

#below print function is taking only 1 argument (but print can take any number of arguments)

#below print function is taking multiple arguments and printing them individually

#Formatted string Print statements - positional args
#Positional arguments

#keyword/named arguments

#Formatted string Print statements other way (3x onwards) - named args

print("H. Datatypes, Mutability & Builtin Functions")
#Sequence Types
#string type -
# indexed sequenced collection of characters/literals
# can be assigned with single, double, triple single/double quotes

#Hints

#Numeric Types
#int type

#float type

#exponential


#Misc Types
#bool types: used for performing logical and conditional operations

# complex numbers:

#None -

#bytes - used for converting the values to byte/binary format before transfer across the network or for processing in a secured fashion

#Complex types - list, tuples, set, dict we learn later

print('G. Operators')

# symbol -> performing action

#Python supports operators -> assignment, arithmatic, comparison/relational, logical,
# unary (least priority), binary (least priority), ternary (least priority), bitwise (least priority)

#Assignment Operators ()- used to assign some values to a variable - return the value/reference as a result

# = , += , -= ,*=...

sal = 10000

# sal -> variable name
# = => assignment operator
# 10000 -> value / operant

sal =1000 +1000

# 1000 + 1000 -> expression , eval

counter =1

counter+=10 # counter = counter + 10 -> 11
counter+=10 # 21
counter+=10  # 31

print(counter)

'''
>>> num=5
>>>
>>> num*=2
>>> num
10
>>> num*=20
>>> num
200
>>> num=num*20
>>> num
4000
>>> num/=20
>>> num
200.0
>>>
'''

#Arithmatic Operators () - will return operated value as a result

#  + , - , * , / , %  , ** , //


num = 100

num2 = 25


# operators usage

print(f"addition of {num} and {num2}(+) :  {num + num2}")

print(f"multiplication of {num} and {num2}(*) :  {num * num2}")

print(f"subtraction of {num} and {num2}(-) :  {num - num2}")

print(f"division  of {num} and {num2}(/) :  {num / num2}")

# modulus

res = 10 %2 # 0 , reminder
'''
11%2 ->1
?%2 -> 0,1
?%3-> 0,1,2
'''

# partitioning / sharding / bucketing


# exponent (**)

print(2**3) # 8 -> 2 *2*2

print(5**3)


# floor division
'''
>>> 125//2
62
>>> 125/2
62.5
>>> 23//3
7
>>> 23/3
7.666666666666667
>>> 23//3
7
>>>
'''

# * -> multiply , ** -> exponent , / -> division , // - floor division

# REF - refer module : sal_bonus_arithmatic.py

print("*-"*30 , "Arithmatic operator ends here","*-"*30)

#Relational operators () - Used for comparing variables and values and returns boolean type as a result
# comparison operator
#  equal , not equal  , less than , greater than  , lte,gte

# conditional struct

# equal -> ==

num=150

num2=300


res=(num==num2)
print(res)  # False

num=num2
res=num==num2
print(res)  # True

# not equal ->   !=

# in sql <>

num=100

num2=300


print(num!=num2) # True

'''
>>> num=100
>>> num2=300
>>> num==num2
False
>>> num!=num2
True
>>>
'''

# lees than  (<)

# greater than (>)

'''
>>> sal=50000
>>> avg=25000
>>>
>>>
>>> sal<avg
False
>>> sal>avg
True
>>>
'''

# less than equal (<=)
# greater than equal(>=)


'''
>>> sal=15000
>>> avg=15000
>>> sal>avg
False
>>> sal<avg
False
>>> sal<=avg
True
>>> sal>=avg
True
>>>

'''

#Logical Operators () - apply logic between multiple output of the relational operators and Returns boolean

# combine multiple condition
#or -

# either True -> True
# everything F -> F

'''
>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> False or False
False
>>>

>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> False or False
False
>>>

'''

#and -

# anything False

# evrything True -> True

'''
>>> True and True
True
>>> False and False
False
>>> True and False
False
>>> False and True
False
>>>
'''
#not -

# reverse case

'''
>>> not True
False
>>> not False
True
>>>

'''

#Bitwise Operators (&, |) - same like logical operator (Costly to use) -

#Unary

num=5 # +

num=+5 #

num=-5


#Binary

#Ternary

# walrus

# membership

# identity

#One program covers almost all these operators

###########One Reallife usecase program to bring all types of operators in one Program###########
#Swiggy food purchase -> coupon max discount of 100 or 10% which ever is lesser


# operator precedence

# BODMAS
# B-> Brackets , O -> Orders(power,exponent) , D -> Division , M-> multiplication , A-> addition , S-Subtraction

# PEMDAS

# P -> parenthesis , E- exponent , ....


# control struct

# conditional struct
# if , switch (not available )
# match -> 3X

# looping construct

# for , while , do while (not available python)(workaround)

# block of statements we need to follow indentation


print('J. Conditional Structure')

# if
# if condition  should return bool value

# syntax - simple if

'''
# indentation  , block of statemtns 
if condition :
      body of the if
      second line
      third ....
      
# breaking if block 

'''


sal=1500
avg_sal=10000


if sal>avg_sal:
      print("higher than average")
      print(f"{sal-avg_sal} getting more" )

print("out side if")


# if -else

# syntax

'''
if condition:
    body of if 
    line2
else:
    body of else
    line2 ...

print("out side if else")

'''


# if alone
'''
if condition:
 print("if block") # this will only execute if the condition true 
 
-> 

>>> if False:
...     print("hi")
...
>>> if True:
...     print("hi")
...
hi
>>>
'''


# if - else

'''
if condition:
    print("if block") # this will only execute if the condition true 
else:
    print("else block") # this will only execute when if condition fails 
 
 
 >>> if True:
...     print("hi")
... else:
...     print("bye")
...
hi
>>> if False:
...     print("hi")
... else:
...     print("bye")
...
bye

'''


# if -elif(else if) -else


''' 
if condition:
    body of if
elif condition2:
    body of elif
else :(optional)
    else part
'''





# Refer ticket_booking_ifelse.py


# nested if

'''
if condition:
    bodyof if
    if condition:
        bodyof innerif
    else:
        body of inner else
else:
    body of outer else
    if condition:
        body of inner if
    else:
        body of inner else

print("out side if-else")

'''



#I can/must/minimum have if condition alone - yes
#I must have if condition with else statement - yes
#I can have only else if or else statement - no
#I can have if condition with else condition alone - yes
#I can have if condition with else if condition alone - yes
#I must have if condition with else if condition and else statement also - else is optional - no
#I should have my conditional structure started with if (if should be used only once), - if
# but can have multiple elif and should have only one else

#Minimal Conditional Structure

#Conditional Structure with multiple condition

#Nested conditional structure, which has to be used appropriately, needs lot of iterative testing


#Quick Usecases:
#Usecase1: Find the greatest of 2 and then 3 numbers using built in functions (max(list of values))

#Usecase2:
# "if" user clicked on the popup then provide the options available upcoming batch or ask anything
# "if" user choosen upcoming batch -> ask user to choose either de or ds or cloud or devops else inform course is not available
# "if" user choosen ask anything ->


# if alone
# if else

# if elif , elif

# if with multi conditions
# if elif, elif , else

# nested
# if
#   if
# else

print('J. Looping Constructs')
#Looping Construct concepts ->

# repeating , iterating
'''

for - un conditional ,  iteration -> fixed 

while , do while   - conditional looping , how many iteration -> its not fixed (based on the condtion)


Category -> 
Conditional looping (entry & exit) eg. while i<=j or while True (do while loop) 
Un Conditional looping - for loop
Types (for, while + do while - not available directly in python (rather we use while True (exit controlled)))
break -> break will terminate the iteration of a loop and come out of the loop 
& continue -> continue will skip the iteration of a loop and continue to the next iteration
'''
#Iteration or repetitive execution of the some tasks across data or programs is called loops
#Two way of Performing Looping - Conditional & UnConditional loopings

#for loop is an unconditional looping


# str - seq collection char
# iterating each char from 'apple' , we are converting into upper case and printing

# for loop syntax

'''
for var in items:
    action 
'''

for c in "apple":
    print(c.upper())


for i in range(5):
    print(i)


# range
# Range it will take three input , 1 requires (stop), 2 optional
# start=0, stop=?,step=1
# used to genarte seq num
# range(start,stop,step)
# range(0,50,1) -> 0,1,2,3,4.....49
# start -0 (include)
# stop=50 (exclude)
# step=1 -> increment by 1
# built in function





#A Realtime Example of for loop on a list of salary (Unconditional Looping)


#while loop is a conditional looping

# conditional looping , number of iteration is not fixed

# entry controlled loop

# syntax

'''
while condition:
    body of the while 
    
'''


print("Print the numbers from 0 to 10 using while")

num=0

while num<10:
    print(num)
    num+=1


# for - fixed iterations

# while  - number of  iteration unknown

# do while - not available in python

# with do while , the code block definitively / at least on time will execute

# do { code } while condition
# exit controlled loop


# we can create do while feature in python with the help of while


print("do while")
num=0

while True:
    print(num)
    if num<10:
        break







#Realtime example of a conditional looping


#Let's try to understand the looping concept in detail with some case studies including the other constructs like break and continue:
#First lets' learn For loop -
#For loop will run on an iterable type only
#For loop is a unconditional looping
#For loop - number of iterations are already known


#How to write a simple for loop


#Nested For loop
#I wanted to calculate bonus applied salary


#for empname,sal in emp_lst,sal_lst:#We can't iterate on more than one list using a single looping construct
#    print(f"bonus applied salary for {empname} is ",int(sal+(sal*(bonus_percent/100))))
#This below approach for finding empname and the salary of the given employee, will not work as we expected


#Let's try with Nested looping: The below nested looping will not work


#Let's try with Nested looping: Using an important function called "enumerate" we can get the index also with the element and apply in other list


#When Do we use Nested For loop
#An University wanted to provide the subjects to all affliated colleges



#For Loop with Break and Continue constructs/clauses:
#Break is used to break the execution of the loop by come out of the loop if a given condition matches
#Continue is used to skip the given iteration of the loop (and execute the next iteration) if a given condition matches


#Let's fine tune the above looping construct to only iterate the required number of times
# (3 times only rather than 5 times)
#The loop will run only 5+1 times


#Break is only effective if we sort the data?
#exists in sql's


#continue construct: continue will help skip the current iteration and continue with the next iteration


#Usecase1: Try create tables for your kids from 2 to how many tables (get as an input)?
# using simple or nested for loop, skip the 5 and 10 tables
#Table has to created upto 12 numbers


#While Loop

#Looping constructs available in Common Prog languages - for, while and do while
#Looping constructs available in Python language - for and while (no do while is available in python)
#Types of Looping - Entry Control & Exit Control loops


#All about While loop:
#
#
#


#How to create infinate loop using while to run some process/operation continuously
#In the other hand if we don't manage the conditions properly, it will leads to infinate looping


#Convert the for loop into while loop - conclude which is better to use for iterating list of values? FOR LOOP is considerable


#Realtime Example of using While loop: Entry controlled loop
#Login username/password used in our routine life
# username=input("User name\n")
# storedpasswd="hduser"
# attempts=1
# maxattempts=3


#Usecase2 related to exit controlled loop (do while loop) + break & continue:
#Create a scheduler program to run a code minimum once or continue to run multiple hours + skipping odd hours
#eg. sfm_insure.py (some print statement)

##############################################Condition Structure & Looping Constructs####################################

print('K. Collection Types')
#Application of using collection types in realtime world?
#Self served metadata driven Data movement automation (DMA) tool
#{"process":"ETL Process1","source":["hive","Bigquery"],"target":["HDFS","GCS"],"cols":["custid","upper(custname) as upper_custname"],"tablename":"customer","where":"(city='chennai')","gcs_uri":"gcs://abc/xyz_bucket/"}


#Hive -
#Python -

#What is a collection type?

#Examples of Collection Types:

#list


#dictionary


#tuple


#set


#Notataions:

#Example of all collection types used:
#{'process': 'ETL Process1', 'source': {'hive', 'Bigquery'}, 'target': ['HDFS', 'GCS'], 'cols': ['custid', 'upper(custname) as upper_custname'], 'tablename': 'customer', 'where': "(city='chennai')", 'uris': ('gcs://abc/xyz_bucket/', 100)}

#Different types of collection types? in the order of importance
#list, dict, tuple, set

#Why we need collection types?
#To manage/store/parse the complex dataset in a hirarchical/nested/complex structure stored or to process semi structure data, nested data,
# dynamic schema-ful data (avro), variable data/metadata, for a data or metadata driven approaches..

#Different characteristics of collection types?
#Iterable (looping), mutable (changable) - updatable (modifyable) & resizable (added/removed), accessible (select using index, position, value, key)

######What are the topics we have to learn in collection types#######
#Iterable? Yes, all collection types are iterable in python.

#Notation, access, resizable/mutable/immutable?  insert/update/delete, functions to apply
#All the above we are going to see in detail
#Notation:
#Accessed using ?
#Definition: Indexed, sequenced collection of homogeneous elements

print("list operations")
#List can be hetrogeneous too (but not suggested, why ? because while operate between the elements of the list, program fails because python is a strongly typed language)


#All the python collections are iterable -


#select/access


#insert/update/delete (list is mutable, hence updating and resizing (add/removing) is possible)

#append in the last (proves list is mutable/resizable/can be inserted)


#insert in the index position


#update the list elements (mutable)

#delete the elements of the list using value


#delete multiple same elements using the value


#pop (delete) the elements of the list using index


print("list after popping out a given index element")

#search for a value with in the given index (range) value and pop(remove) it




#Wanted to remove the duplicate in a given list?
#Convert to set and back to list

#certain builtin functions to try out on list




print("Dictionaries (mutable) - {k:v, k:v}")


#Access a dictionary - using key


#Adding Items - if the key is not found


#Updating Items - if the key is found


#Removing an Item (from the last)

#Delete(pop) the given key

#Delete all the elements of a dict
#dict1.clear()


#Iteration of Dictionary
#Iterate on the items of the Dict - will return what datatype???tuple


#Iterate on the keys of the Dict - will return what datatype???respective key's datatype


#Iterate on the values of the Dict - will return what datatype???respective value's datatype

#Some additional functions

#Setdefault will add the key and value provided if key is not present already, if already present consider the given value and not the default value

#create a dictionary with the keys from list and value from the second argument


print("Tuples (immutable?)")
#Definition of Tuple:Tuple is an indexed sequenced collection of hetrogeneous elements, tuples are immutable (non updatable and non resizable)
#Notation is ()


#select/access
#City where Anirudh present

#count of some element in the given tuple

#search for some element in the given tuple to identify the index


#Resizable? No (insert/delete)
#Try to Add some elements to the tuple, lets try to add age of Anirudh
#Insert/Append? No


#delete? No
#tup1.__delattr__(name="Chennai") #cannot delete the elements of tuple

#Modify (update) - Not possible


#I want to achieve Insert/update/Delete in a tuple? Not possible by default,
# but we can do some workaround to achieve it? convert to list , do insert update delete and convert back to tuple

#Do all operations/functions that list supports (#Other functions to apply)
#Insert


#Update

#Delete


#Convert the list back to tuple



print("Set (mutable) (least important)- Notation {} - "
      "Set is a sorted and distinct collection of iterable elements, cannot be accessed using index ?? Why?")

#how to access the element of a set (cant be access directly by using index/key/values)- Index can't be used why?
#The number of elements/items in the set is not fixed in the numbers or sort order
#set1[0] #not possible to access using index

#set is iterable?yes


#set is mutable?Yes
#add will help add/update an element not the set

#update will help add/update another set


#set is mutable (resizable) - Removing/popping/cleaning


#set is supported with set operation (If we use set, we use it for these purposes)
#Requirement of identifying the common department in the given lists

#intersect - combine both the sets


#difference (difference/subtract/minus) - find the difference between the sets

