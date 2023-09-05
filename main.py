# ///////////////////////////   Module 1 types_of_data    /////////////////////////////


# Python print() with end Parameter
print ("hello world!!!", end= " ")
print("Hello Git")

#Example 3: Python print() with sep parameter
print('New Year', 2023, 'See you soon!', sep= '. ')

#Sometimes we would like to format our output to make it look attractive. This can be done by using the str.format() method. For example,
x = 5
y = 10

print('The value of x is {} and y is {}'.format(y,x))


#print("Hello") # at the beggining - meaning that this string commented and doesn't work like a code

# nmbers
y = 8**3+4*(2+2)
x = 3.3 + 2j
print (x, y)

# complex number
complex = 3.14 + 1J # У Python вбудовані також комплексні числа. Запис таких чисел відбувається у вигляді пари значень: дійсної та уявної частини, які поділяються символом операції додавання. На кінці уявної складової частини комплексного числа обов'язково ставлять букву j.
# Щоб отримати дійсну та уявну частину чисел, окремо необхідно використовувати властивості real та imag:

print(complex.real)  # 3.14
print(complex.imag)  # 1.0

a = -2 + 3j
b = 4 + 2.1j
result = a + b
print ("result ", result) #(2+5.1j)

# f- string
a = "hello "
b = "world"
c= a+b
print(c)
name = "Jonh"
hello_string = f"Hello, {name}"
print (hello_string)

''' багаторядковий кометар - три одинарних або три подвійні кавички на початку та на прикінці  
 boolean
# Для приведення інших типів даних до булевого типу використовується функція bool() Функція bool() поверне False у наступних випадках
# -порожній рядок
# -нульове число
# -порожній список/кортеж
# В інших випадках функція поверне True
'''
e = True
d = False
age = 18
adult1 = age >= 18 
print(adult1) # true
print ("should be false", a == b) # false


"""
 input in Console
# e = input ("введдіть своє імʼя: ")
# age1 = input ("введдіть свій вік: ")
#num = int(input('Enter a number: ')) # at once convert to integer
#input_output = f"Hello, how is it going, {e}. You are {age1} years old and you are allowed to visite this site"
# print(input_output)
"""

pi = float(age)
print (pi)
print (type (pi))

#Для роботи з числами в Python існує один з найважливіших модулів math (для комплексних чисел існує окремий модуль cmath). Цей модуль надає великий функціонал для роботи з числовими даними. Щоб додати модуль до своєї програми, необхідно виконати імпорт цього модуля за допомогою ключового слова import => import math
import math
a = math.sqrt(100)  # корінь квадратний 10.0

a = -2
b = 7
c = -6
D = pow(b, 2) - 4 * a * c
x1 = (-b + math.pow(D, 0.5)) / (2 * a)
x2 = (-b - D**0.5) / (2 * a)
print("MATH", D, x1, x2)

f = 11
h = f
print (h)
f = 33
print (22222, h)
num_1 = 1.8
num_2 = int(float(str(num_1)))
print(num_1, num_2, type(num_2))

w = 3
q = 4
print(w, id(w))
print (q, id(q))

# ///////////////////////////   Module 2 conditions_and_statements    /////////////////////////////

