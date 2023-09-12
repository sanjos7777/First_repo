# Хай є два початкових числа first та second.
# Виберемо менше з них та привласнимо значення змінній gcd.
# Поки first або second не діляться на gcd без залишку, треба виконувати цикл, в якому зменшуємо змінну gcd на одиницю.
# Коли цикл закінчиться в змінній gcd буде НСД для чисел first та second
# Напишіть програму, яка для двох додатних цілих чисел знаходить НСД.

# Примітка: Для умови циклу в пункті 3 необхідно пам'ятати, що цикл while виконується за умови True, а наш цикл повинен закінчитися, тільки якщо gcd поділив обидва числа без залишку.
#Змінна gcd має не вірне значення, 115 повинно бути: nod=25 first=375 second=575
#Код виконується


#HM 2.9 Найбвльший спільний дільник
first =   375 #int(input("Enter the first integer: "))
second =  575 #int(input("Enter the second integer: "))
gcd_first = None
gcd_second = None
gcd = first if first < second else second
print (range(1,gcd + 1))
for i in range(1, gcd+1):
    print (i)
    print("First ",first % i)
    print ("Second", second % i)
    if((first % i == 0) and (second % i == 0)):
        print(i)
        gcd = i
print("finally ",gcd)

# через while
gcd = first if first < second else second
while first % gcd != 0 or second % gcd != 0: #якщо first або second діляться без 
        gcd -= 1

# Or 
while True:
    if first % gcd == 0 and second % gcd == 0:
        break
    else:
        gcd -= 1



#HM 2.10
num = int(input("Enter integer (0 for output): "))
sum = 0
while num != 0:
    for i in range (1, num+1):
        print(i)
        sum = sum + i
        print(sum)
    num = int(input("Enter integer (0 for output): "))


#hm 2.11
sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
        
    for i in range(num + 1):
        sum = sum + i
    print(sum)

#hw 2.12 Ceasar code
message = "Hellow world!" #input("Enter a message: ")
offset = 37 #int(input("Enter the offset: "))

encoded_message = ""
for ch in message:
    print (ord (ch))
    if ch.isupper():
        pos = ord(ch) - ord ("A")
        new_pos = ((pos + offset) % 26)
        print ("pos", pos)
        print ("new pos", new_pos)
        new_char = chr ((new_pos) + ord("A"))
        print("new char", new_char)
        encoded_message = encoded_message + chr ((new_pos) + ord("A"))
    elif ch.islower():
        pos = ord(ch) - ord ("a")
        new_pos = ((pos + offset) % 26)
        print ("pos", pos)
        print ("new pos", new_pos)
        new_char = chr ((new_pos) + ord("a"))
        print("new char", new_char)
        encoded_message = encoded_message + chr ((new_pos) + ord("a"))
    elif ch in ("!","\"", "#", "$", "%", "&", "'", "(", ")", " "):
            encoded_message = encoded_message + ch
print ("encodede message", encoded_message)

#hw 2.13 Exception - Devide by zero
pool = 1000
quantity = 0# int(input("Enter the number of mailings: "))
try:
    chunk = chunk = pool // quantity
except ZeroDivisionError:
    print('Divide by zero completed!')

#hw 2.15 Calculator
result = None
operand = None
operator = None
wait_for_number = True

while True:
    char = input ("input value: ")
    print ("wait for number", wait_for_number)
    if char == "=":
        print(f"Result: {result}")
        break
   
    elif wait_for_number:
        try:
            operand = int(char)
            wait_for_number = False
            print ("Try...", wait_for_number)
            if operator:
                if operator == "+":
                    result += operand
                elif operator == "-":
                    result -= operand
                elif operator == "*":
                    result *= operand
                elif operator == "/":
                    try:
                        result /= operand
                    except ZeroDivisionError:
                        print ("Divide by zero")
                        continue

            else:
                result = operand
        except ValueError:
            print (f"{char} is not a number. Please input the number")
            continue
        wait_for_number = False

    elif char in ("+", "-", "*", "/"):
        operator = char
        wait_for_number = True
    
    else:
        print (f"{char} is not '+', '-', '*', '/'. Please input the correct operator: ")

