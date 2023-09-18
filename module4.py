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

odd_numbers = numbers[0:9:2] # odd_numbers = numbers[::2]
even_numbers = numbers[1:9:2] # even_numbers = numbers[1::2]
three_numbers = numbers[2:9:3]

# Ви можете не вказувати початковий, кінцевий індекс або крок, пропускаючи його. За замовчуванням Python візьме зріз з початку до останнього елемента з кроком 1. Перепишемо попередній приклад у скороченому синтаксисі:
odd_numbers = numbers[::2]
even_numbers = numbers[1::2]
three_numbers = numbers[2:9:3]

numbers_copy = numbers[:]
print(odd_numbers)
print(numbers_copy)

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
print(chars)  # {'a': 1, 'b': 2, "c": 8}

# clear() — очищає словник, не створюючи нового
chars = {'a': 1, 'b': 2}
chars.clear()
print(chars)