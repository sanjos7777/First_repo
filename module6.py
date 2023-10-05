# тут ми відкриваємо файл з флагом "w" - відкрити і перезаписати - тобто стерти те що було в файлі

# file = open('test.txt', 'w')
# file.write("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000")
# file.close()

# Тут за допомогою аргумента "a" ми відкриваємо файл та додаємо інформацію у кінець файлу
# file = open('test.txt', 'a')
# file.write('what do you think about Python?')
# file.close()

# file = open('test.txt', 'r')
# таким циклом ми можемо перебрати кожен символ якщо параметр буде 1 у read(1) або одразу весь read(), або по два read(2) і так далі.
# while True:
#     symbol = file.read(6)
#     print(22, len(symbol))
#     if len(symbol) == 0: # вихід з циклу відбувається коли після останнього символа в строці while візьме нічого, тобто 0
#         break
#     print(symbol)
# file.close()

file = open('test.txt', 'r' )
# all_file = file.read() # read( ) приймає у параметр кількість символів для читання, якщо нічого не передати, то читатися буде весь файл
import re
res = []
regex_sal = r"\d+"
# sal = []
# print(all_file)
# print (type(all_file))
print(res)
while True:
    line = file.readline()
    print(line)
    catch_sal = re.search(regex_sal, line)
    print(catch_sal.span)
    # res.append(float(int(catch_sal.group)))
    print (res)
    
    if not line:
        break
        
file.close()
