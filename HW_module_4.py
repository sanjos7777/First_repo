def prepare_data(data):
    new_data = sorted(data)
    new_data.pop(0)
    new_data.pop()
    print (new_data)
    return new_data

array = [193, 446, 93, 2,4,5,7,333,555,777,0.3]
prepare_data(array)

#================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = numbers[0:10:2]
even_numbers = numbers[1:10:2]
three_numbers = numbers[2:10:3]

print(even_numbers, odd_numbers)

#================================

def format_ingredients(items):
    print(len(items))
    str_1 = "" 
    if len(items) > 0:
        for value in items:
            print (items.index(value))
            if len(items) >= 2:
                if items.index(value) == 0:
                    str_1 = str_1 + f"{value}" 
                elif items.index(value) < len(items) - 2:
                    str_1 = str_1 + f", {value}" 
                elif items.index(value) == len(items) - 2:
                    str_1 = str_1 + f", {value}"
                elif items.index(value) == len(items) - 1:
                    str_1 = str_1 + f" and {value}"
            else:
                str_1 = str_1 + value
    else:    
        str_1 = "You miss all yours ingridients"
    print (str_1)
    return str_1
    
str_1 = ["2 eggs", "tomato", "1 liter sugar", "1 tsp salt", "vinegar", "vanilla"]
format_ingredients(str_1)
#================================

def get_grade(key):
    list  = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}
    print (list.keys())
    if key in list.keys():
        return list.get(key)
    return None
print(get_grade("F"))

def get_description(key):
    list  = {"F": "Unsatisfactorily", "FX": "Unsatisfactorily", "E": "Enough", "D": "Satisfactorily", "C": "Good", "B": "Very good", "A": "Perfectly"}
    if key in list.keys():
        return list[key]
    return None

print(get_description("Be"))
 #================================
def lookup_key(data, value):
    res = []
    print(value)
    for key, val in data.items():
        if val == value:
            res.append(key)
        else:
            continue
    print (res)
    return res

#==============================

def split_list(grade):
    group_1 = []
    group_2 = []
    if len(grade) != 0:
        avarage = round(sum(grade)/len(grade), 1)
        print(avarage)
        for mark in grade:
            if mark <= avarage:
                group_1.append(mark)
            else:
                group_2.append(mark)
        
    return group_1, group_2



marks = (3, 5, 2, 2, 5, 5, 3)

print(split_list(marks))

# ====================================


points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}
print (points.keys())
def calculate_distance(coordinates):
    distance = 0
    if  len(coordinates) < 1:
        return distance
    else:
        for coord in range(len(coordinates)-1):
            current = [coordinates[coord], coordinates[coord+1]]
            print([min(current), max(current)])
            distance += points[min(current), max(current)]
        return distance

print (calculate_distance([0, 1, 3, 2, 0, 2]))

#  ==================================

def game(terra, power):
    for list in range (len(terra)):
        for list1_1 in terra[list]:
            if power >= list1_1:
                power += list1_1
            else: 
                break
    return power
    
game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1)

# ==================================
def is_valid_pin_codes(pin_codes):
    if len(pin_codes) > 0:
        for char in pin_codes:
            if isinstance(char, str) and len(char) == 4:
                try:
                    char_to_int = int(char)
                except ValueError:
                    print ("not a number")
                    return False
                pin_codes.remove(char)
                if char not in pin_codes:
                    print (100 )
                else:
                    print ("duplicates ", char)
                    return False               
            else:
                print ("invalid pin ", char)
                return False
    else:
        print (444)
        return False  
    print (777)
    return True
# print (is_valid_pin_codes ([]))
print (is_valid_pin_codes (['1101', '9034', '00r1', '1102']))

# =======================================

def is_valid_password(password):
    l, u, p, d = 0, 0, 0, 0
    symbols = "()*+,-./:;<=>?@#[\]^_`{|}~"
    print (len(password))
    if (len(password) >= 8):
        for i in password:
    
            # counting lowercase alphabets
            if (i.islower()):
                l+=1
                print(i, " L")           
    
            # counting uppercase alphabets
            if (i.isupper()):
                u+=1           
                print(i, " U")           

            # counting digits
            if (i.isdigit()):
                d+=1           
                print(i, " D")           

            # counting the mentioned special characters
            if i in symbols:
                p+=1
                print(i, " P")           
          
    if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password)):
        print("Valid Password")
        return True
    else:
        print("Invalid Password")
        return False

print( is_valid_password("9Nml|1V0"))

def is_valid_password(password):
    has_upper = False  #
    has_lower = False  #
    has_num = False  #
    for ch in password:  #
        if "A" <= ch <= "Z":  #
            has_upper = True  #
        elif "a" <= ch <= "z":  #
            has_lower = True  #
        elif "0" <= ch <= "9":  #
            has_num = True  #
    if len(password) == 8 and has_upper and has_lower and has_num:  #
        return True  #
    return False  #

# ========= complex solution for generator password
from random import randint


def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    has_upper = False  #
    has_lower = False  #
    has_num = False  #
    has_symb = False
    symbols = "()*+,-./:;<=>?@#[\]^_`{|}~"

    for ch in password:  #
        if "A" <= ch <= "Z":  #
            has_upper = True  #
        elif "a" <= ch <= "z":  #
            has_lower = True  #
        elif "0" <= ch <= "9":  #
            has_num = True  #
    if len(password) == 8 and has_upper and has_lower and has_num:  #
        return True  #
    return False  

def get_password():
    count = 0
    while count <=100:
        password = get_random_password()
        if is_valid_password(password):
            print(password)
            break
        else: 
            count += 1
    return password

#==============================================
from pathlib import Path
def parse_folder(path):
    p = Path(path)
    files = []
    folders = []
    for i in p.iterdir():
        print("items ", i)
        if i.is_file():
            print("+")
            files.append(i.name)
        else:
            print("-")
            if i.is_dir():
                folders.append(i.name)
    return print(files, folders)
parse_folder('/Users/oshchyrskyi/Documents/Python_GO_IT/My_repo/First_repo')

# ===================================================

import sys
a = []
b= ""
for arg in sys.argv: # oshchyrskyi@C11069 First_repo % python3 test.py hello second test world 333
    a.append(arg)
    b = " ".join(a[1:])
print (a) # ['test.py', 'hello', 'second', 'test', 'world', '333']
print (a[1:]) # ['hello', 'second', 'test', 'world', '333']
print(b) # hello second test world 333