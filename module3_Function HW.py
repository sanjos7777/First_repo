def factorial(n):
    print(n)
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

# 2
def invite_to_event(username):
    return f"Dear {username}, we have the honour to invite you to our event. Please calculate a taxi price next"
user_name = None
base_rate = 40
price_per_km = 10
total_trip = 0
while True:
    user_name = input("Enter you name: ")
    if user_name == "q":
        break
    else:
        print(invite_to_event(user_name))
#3
   
    print("total trip77777 ", total_trip)
    
    def calculate_trip_price(distance_km):
        global total_trip
        print("total trip ", total_trip)
        total_trip += 1
        print("total trip222 ", total_trip)
        return base_rate + price_per_km * distance_km

    distance = input (f"{user_name}, enter the distance, please: ")
    try:
        distance = float(distance)
    except ValueError:
        print ("Input correct distance")
    trip_price = calculate_trip_price(distance)
    print (f"Dear {user_name}, your price for trip is {trip_price} and it is your {total_trip} trip")


#4
price = 100
discount = 0.5
def discount_price(price, discount):
    
    def apply_discount():
        nonlocal price

        print ("nonlocal price - ", price )
        price = price - price * discount

    apply_discount()
        
    return price
print(discount_price(price, discount))


length=15
string='abaa'

def format_string(string, length):
    print(len(string))
    if len(string) >= length:
        return string
    else:
        add = (length - len(string)) // 2
        for l in range(1, add + 1):
            string = f" {string}"
        return string
        # add = (length - len(string)) // 2
        # string = " " * add + string
string = format_string(string, length)
print(444, len(string))

def first(size, *test ):
    sum = 0
    lenn = len(test)
    print ("lenn ", lenn)
    for i in range (1, lenn +1):
        print (i)
        sum  += i 
        print ("sum ", sum)
    return (test)
print(first(5, "first", "second", "third"))


def cost_delivery(qty, *product, discount = 0):
    """Функція повертає суму за доставлення замовлення.

    Перший параметр quantity кількість товарів в замовленні.
    Параметр знижки discount, який передається лише як ключовий, за замовчуванням має значення 0.
    Доступ до рядка документації функції можна отримати за допомогою атрибуту функції __doc__. Зверніть увагу на подвійне підкреслення."""
    
    
    result = (5 + 2 * (qty - 1)) * (1 - discount)
    return result

print (cost_delivery(2, 1, 2, 3, discount=0.3))
print (cost_delivery.__doc__)

"""
Ми проводимо розіграш призів серед перших 50 підписників ютуб-каналу. Ми маємо 7 призів для розіграшу. Може виникнути питання, скільки різних списків переможців ми можемо отримати під час розіграшу? Для цього ми будемо використовувати формулу сполучень без повторень

Cnk = n! / ((n - k)! · k!)

де n — це загальна кількість людей (випадків), а k — кількість людей, які отримали призи.

Напишіть функцію number_of_groups, яка приймає параметри n та k, і за допомогою функції factorial повертає нам скільки різних списків переможців ми можемо отримати при розіграші

Зверніть увагу на те, які великі значення ми отримуємо для факторіала. Рекурсивні висловлювання треба завжди застосовувати з обережністю при обчисленнях, щоб не отримати переповнення пам'яті.
"""
def factorial(n):
    if n == 1 or n == 0:
        return 1  # Базовий випадок
    else:
        return n * factorial(n - 1)
print ("factorial of 5 ", factorial(5))

def number_of_groups(n, k):
    C = factorial(n) / (factorial (n - k) * factorial(k))
    return int (C)
    
# Fibonacci

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print("Fib ", fibonacci (n - 1))
        print("pol ", fibonacci (n - 2))
        return fibonacci (n - 1) + fibonacci (n - 2)

print (fibonacci(2))
