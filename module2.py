# ///////////////////////////   Module 2 conditions_and_statements    /////////////////////////////
#2.1 if...elif...else
#a = input("Enter any number: ")
a = int(a)
if a > 0:
    print ("Число додатне")
elif a < 0:
    print ("Число відʼємне")
else: 
    print ("Число - 0")

if a: # все окрім 0 - буде True і навіть відʼємне число буде тру, тому на elif перевірку не потрапить. 0 - буде сприйнято як False, тому спрацює Else
    print ("Число додатне")
elif a < 0:
    print ("Число відʼємне")
else: 
    print ("Число - 0")

#2.2 AND OR
name = "Jonh"
age = 17 #change to 18 or bigger to get TRUE
has_driver_licence = True
if name and age >=18 and has_driver_licence: # резудьтат работи оператора AND буде TRUE, якщо всі умови TRUE. Як тільки буде хоч 1 FALSE - результат буде FALSE, подальша робота інтерпретатора припиняється, бо все одно результат буде False. Перевірка зліва направо Name==True->Age==True-> has_licence==True - Total - TRUE. якщо вік буде менше 18 то Age==False і весь if буде False
    print (f"Client {name} can rent a car")
else:
    print (f"Client {name} can't rent a car")

""">>> 1 and 2 and 3
3
>>> 1 and 0 and 3
0
>>> 1 and "rr" and ""
''
>>> 1 or 0
1
>>> 0 or ""
''
>>> 1 and 2 or 3
2
>>> 1 and 0 or 2
2
>>> 0 and 1 or 2
2
>>> 0 or 1 and 2
2
>>> not 2<0
True"""
# Тернанрні операції
is_nice = True
state = "Nice" if is_nice else "Not nice"
print(state)


some_data = None
msg = some_data or "Небуло отримано жодних даних"
print(msg)

# Блоки інструкцій, вкладеність
x = int(input("X: "))
y = int(input("Y: "))

if x == 0: # input 0 for X for run this part
    print("X can`t be equal to zero")
    x = int(input("X: "))
    if x == 0:
        print("X can`t be equal to zero")
        

    
#print(int(y / x))
# Приклад вкладеності для визначення чвертей для координатної площини.
x = -3
y = -2
if x >= 0:
    if y >= 0:               # x > 0, y > 0
        print("Перша чверть")
    else:                    # x > 0, y < 0
        print("Четверта чверть")
else:
    if y >= 0:               # x < 0, y > 0
        print("Друга чверть")
    else:                    # x < 0, y < 0
        print("Третя чверть")

#Цикли. 
# цикл for використовується для перебору усіх елементів контейнерів або ітерованих об'єктів, наприклад, списків. Інструкції, які знаходяться у тілі циклу, будуть виконані стільки разів, скільки елементів у списку. При цьому на кожній ітерації спеціальна змінна набуває значення одного з елементів списку.
"""Синтаксис циклу for:

цикл розпочинається з ключового слова for;
за яким обов'язково йде назва змінної, куди записуватиметься значення, що отримується з ітерованого об'єкту на кожній ітерації;
далі слідує ключове слово in;
за яким обов'язково йде вираз або об'єкт, по якому, власне, буде ітеруватися for;
далі ставиться :;
і з нового рядка з відступом йде набір виразів, які повторюватимуться на кожній ітерації"""
fruit = 'apple'
for char in fruit:
    print(char)

array = (1,2,3,4,5,6)
for num in array:
    print(num)

# WHILE дозволяє виконати інструкції, які знаходяться у тілі циклу до тих пір, доки виконується умова, вказана в циклі. Наприклад, цикл while, який виводить числа від 1 до 5
a = 1
while a <= 5:
    print(a)
    a = a + 1
#«Нескінченні цикли» та break. Можна використувувати як для WHILE так і IF
a = 0
while True:
    print(a)
    if a >= 20:
        print ("Loop is finished")
        break        
    a = a + 1
#Завершення ітерації за допомогою continue
a = 0
while a < 6:
    a = a + 1
    print("first", a)
    if not a % 2:
        print(f"in if a = {a} ")
        continue #ця директива повертає інтерпритатор на початок цикла
    print("last", a)
for i in range(10): #range - діапазон
    if i % 2 : # 0 % 2 -> 0 -False - виходимо з If і друкуємо i
                # 1 % 2 -> 1 - True - виконується Continue - пропускаємо і переходимо до наступної ітерації
                # 2 % 2 -> 0 -False - виходимо з If і друкуємо i
        continue
    print (i)

# 2.5 Винятки.
"""Основні типи виключень у Python
SyntaxError — синтаксична помилка.

IndentationError — помилка, яка виникає, якщо у виділенні блоків інструкцій пробілами припущена помилка.

TabError виникає, якщо в одному файлі використовувати пробіли і табуляції для виділення блоків інструкцій.

TypeError виникає, коли операція зі змінною цього типу неможлива."""

a = "a"
# int(a) тут буде виняток в обробці з типом ValueError

while True:
    user_input = input("Enter any numbers - ")
    try:
        x = int(user_input)
    except ValueError:
        print ("Should be a number. Try again!!")
        continue


val = 'a'
try:
    val = int(val)
except ValueError:
    print(f"val {val} is not a number")
else:
    print(val > 0)
finally:
    print("This will be printed anyway")

