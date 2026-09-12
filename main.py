# types of variables 1. Strings 

first_name = "kareem"
last_name = "Abu Ghalyoun"
food = "Manaf"

# 2. Integers 

age = 19 
num_of_students = 30

# 3. Float 

price = 3.5
gpa = 3.2 

# 4. Boolean 

is_student = True 
not_student = False
is_online = False 

# if is_student:

# else:    
            
# ***type casting*** the process of converting a variable from one data type to another 
#             str().. for String ,
#             int(), float(), bool(),
name = "Kareem"
age = 25 
gpa = 3.2
is_student = True

name = bool(name) # this is how we convert from string(str) to boolean 
age = int(age) # this is how we convert from float to int 


(type(name)) # by this statement we will Know what is the type of variable in the bracetes we can print it 

# *** User Input *** >>> Here we use input()

name = input("What is your name ? ")
age = int(input(f"Hello {name}! How old are you ? "))

age = int(age) # here the important of type casting show up or we can close the input statement with around bracetes ()
age = age + 1

print(f"Next year you will be {age} years old yeah ?")

print("The area cm²") # you can write this cm² by (keep the num lock on then alt + 0178)

''' and you can write the comment like this ''' 

# arithmetic operators / math functions 

friends = 10
'''  
friends = friends + 1 
friends += 1
friends -= 2
friends = friends - 2
friends = friends * 3
friends *= 3 
friends = friends / 2 
friends /= 2
'''
reminder = friends % 3 # By this statement you can determine  if it's even or odd number 

# some tricks in python : 
# 1. result = abs(x) Here we use abs(x) to calculate the x as a positive number -- you can use it to convert it into positive number 
# 2. result = max(x, y, z) here you convert the max number of these three numbers or howevew you need to compare 
# 3. result = pow(4, 3) that's mean 4 power of 3 
# 4. result = min(x, y, z) the minemum number of these numbers 

'''
import math

x = math.pi
y = math.e
z = 9
result = math.sqrt(z)

print(result)
'''






