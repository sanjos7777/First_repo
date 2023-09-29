some_iterable = ["a", "b", "c", "d"]
first_letter = some_iterable[0]
middle_one = some_iterable[1]
last_letter = some_iterable[2]

#OR use negative index

first_letter = some_iterable[-3]
middle_one = some_iterable[-2]
last_letter = some_iterable[-1]
print (len(some_iterable))
forth_letter = some_iterable[-2]
print (forth_letter)
print (some_iterable)

# change value of any element in the massive
some_iterable[2] = 33
print (some_iterable)

# Зрізи у Python (Slice)
# Для впорядкованих контейнерів є спеціальний синтаксис, коли нам необхідно отримати деяку послідовність елементів з контейнера. Наприклад, якщо ми хочемо отримати перші 5 літер рядку:
some_str = "This12 is awesome string"
first_five = some_str[0:5] # з 0 та до якого - 5 (не включно) брати елементи в нову послідовність
print (first_five) # в данному випадку 4 індекс включно - і загалом 5 символів

# також є третій параметр - крок [0: 13: 2], тобто брати через 1 символ
random_str = some_str[0: 13: 2]
print(random_str)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
numbers.append(4) #додати в кінець списку
print ("count ", numbers.count(4)) # Порахувати кількість елементів
print ("index ", numbers.index(4)) #Знайти індекс першого елемента у списку, що дорівнює
print ("max ", max(numbers))
print ("min ", min(numbers))
numbers_copy = numbers[:]
new_numbers = numbers.copy()
print("new numbers ", new_numbers)
new_numbers.clear() # видалення списку
print("new numbers after clear", new_numbers)
new_numbers = numbers
other = ["e", "f", "d", "k", "g", "a", 4, 2, 9, 10]
print 
numbers_copy.reverse() # перебудовує список у зворотній послідовності
print("reverse ", numbers_copy)
numbers_copy.sort() # сортує у алфавітній або числовій послідовності за зростанням
numbers_copy.insert(0, 585858558) # вставляє елемент в список за індексом
print("sort ", numbers_copy)
print("origin list ", id(numbers))
print("list by = ",id(new_numbers))
print("copied list by COPY",id(numbers_copy))

new_numbers.extend(other) # обʼєднання списків
print("after extend ", new_numbers)



odd_numbers = numbers[0:9:2] # odd_numbers = numbers[::2]
even_numbers = numbers[1:9:2] # even_numbers = numbers[1::2]
three_numbers = numbers[2:9:3]

# Ви можете не вказувати початковий, кінцевий індекс або крок, пропускаючи його. За замовчуванням Python візьме зріз з початку до останнього елемента з кроком 1. Перепишемо попередній приклад у скороченому синтаксисі:
odd_numbers = numbers[::2]
even_numbers = numbers[1::2]
three_numbers = numbers[2:9:3]


# Словники (обʼєкти)
# pop(key) — повертає значення елементу і видаляє пару ключ-значення зі словника
chars = {'a': 1, 'b': 2}
b_num = chars.pop('b')
print(chars)  # {'a': 1}
print(b_num)  # 2

# update(another_dict) — розширює словник значеннями з іншого словника
chars = {'a': 1, 'b': 2}
chars.update({"c": 3})
chars.update({"c": 8})
new_chars = chars.copy()
print(" New chars", new_chars)
print(chars)  # {'a': 1, 'b': 2, "c": 8}
print ("get ", new_chars.get('b'))
print ("items ", new_chars.items() )
print ("from key ", new_chars.fromkeys("b"))
print ("keys ", new_chars.keys())
print ("values ", new_chars.values())

# clear() — очищає словник, не створюючи нового
chars = {'a': 1, 'b': 2}
chars.clear()
print("chars ", chars)
print ("new chars ", new_chars)
for key in new_chars.keys():
    print (key)

for value in new_chars.values():
    print (value)

for key, value in new_chars.items():
    print(key, value)
print ("HW4 ", new_chars["b"])

# Математичні операції над множинами

a = set('hello')
print(a)    # {'e', 'h', 'l', 'o'}

b = set('hi there!')
print(b)    # {'r', ' ', 'i', 'e', '!', 'h', 't'}
print (a & b) # знайти загальні елементи для двох множин, виконаємо над ними операцію & (AND)
print (a ^ b) # усі елементи з двох множин, окрім загальних, за допомогою оператора ^ (XOR)
print (a | b) # Об'єднання множин, або просто усі елементи з обох множин знаходяться за допомогою оператора | (OR)
string_set = set("My set")
print("string set", string_set)  # {'s', ' ', 'y', 'M', 't', 'e'}
list_set = set(["My", "set"])  # {'My', 'set'}
print("list set",list_set)

user_1 = {"name": "Jane", "age": 21}
user_2 = {"name": "Moris", "age": 23}
user_3 = {"name": "Steve", "age": 24}

persons = [user_1, user_2, user_3]

for id in persons:
    print ("user ", id.get("name"))
    for field in id.keys():
        print("wtf ", id.get(field))

from pathlib import Path

p = Path()    # p Вказує на папку /home/user/Downloads
for i in p.iterdir():
    print(i)
import sys
a = []
b= ""
for arg in sys.argv: # oshchyrskyi@C11069 First_repo % python3 test.py hello second test world 333
    a.append(arg)
    b = " ".join(a[1:])
print (a) # ['test.py', 'hello', 'second', 'test', 'world', '333']
print (a[1:]) # ['hello', 'second', 'test', 'world', '333']
print(b) # hello second test world 333