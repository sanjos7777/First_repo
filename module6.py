# тут ми відкриваємо файл з флагом "w" - відкрити і перезаписати - тобто стерти те що було в файлі

file = open('test.txt', 'w')
file.write("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000")
file.close()

# Тут за допомогою аргумента "a" ми відкриваємо файл та додаємо інформацію у кінець файлу
file = open('test.txt', 'a')
file.write('what do you think about Python?')
file.close()

# Тут з модулем WITH та методом writelines ми дописуємо рядок

# with open ("test.txt", "w") as file:
#     file.writelines(["mmm, I like it", " I don't like it at all"])


file = open('test.txt', 'r')
# таким циклом ми можемо перебрати кожен символ якщо параметр буде 1 у read(1) або одразу весь read(), або по два read(2) і так далі.
while True:
    symbol = file.read(6)
    print(22, len(symbol))
    if len(symbol) == 0: # вихід з циклу відбувається коли після останнього символа в строці while візьме нічого, тобто 0
        break
    print(symbol)
file.close()

file = open('test.txt', 'r' )
# all_file = file.read() # read( ) приймає у параметр кількість символів для читання, якщо нічого не передати, то читатися буде весь файл
while True:
    line = file.readline()
    print(line)
    if not line:
        break
        
file.close()
# ==========================

file = open("text.txt", "w+")
file.write("0123456789sg;lkjsd7ffgl;jrl sfljghsflrgh rglpijrdsgl;d fgdefl;ghjrg ")
print(file.tell())
file.seek(2)
r = file.read()
print("111 ", r)
file.write ("212312 \n")
file.write("RHRHHRHRHRHRH")
file.seek(0)
print(333 , file.readline())
r = file.read()
print("222 ", r)
file.close()
#  ===============

