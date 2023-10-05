import re
def real_len(text):
    res = ""
    for char in text:
        print (char)
        if char in "\n, \f, \r, \t, \v":
            continue
        else:
            res+= char
    return print (len(res))

real_len('Al\nKdfe23\t\v.\r')

articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    res = []
    for article in articles_dict:
        title = article["title"]
        print ("title ", title)
        author = article["author"]
        print ("author ", author)
        year = article["year"]
        print ("year ", year)

        if letter_case:
            pair_author = key in author
            print (1, "pair_author " ,pair_author)
            pair_title = key in title
            print ("pair_title ", pair_title)
        else:
            pair_author = key.lower() in author.lower()
            print (2, "pair_author FALSE" ,pair_author)

            pair_title = key.lower() in title.lower()
            print ("pair_title FALSE" ,pair_title)

        if pair_author or pair_title:
            result = {
                "title" : title,
                "author" : author,
                "year" : year
            }
            res.append(result)
    print (res)
    return res
find_articles("ocean")

# ===========================================================
def sanitize_phone_number(phone):
    new_phone =[]
    print("phone ", phone)
    for char in phone:
        if char not in ("(", ")", " ", "+", "-"):
            new_phone.append(char)
    print (new_phone)
    new_phone = "".join(new_phone)
    print (new_phone)

    return new_phone

user_phone = "   +38 (050) 123-45-67  "
sanitize_phone_number(user_phone)


# ===========================================================

# У модулі роботи з функціями ми писали функцію get_fullname для складання повного імені користувача. Виконаємо невелике продовження для цього завдання та напишемо функцію is_check_name, яка приймає два параметри (fullname, first_name) і повертає логічне значення True або False. Це результат перевірки, чи є рядок first_name префіксом рядка fullname. Функція is_check_name чутлива до регістру літер, тобто "Sam" і "sam" для неї різні імена.\

def is_check_name(fullname, first_name):
    fullname.lower()
    first_name.lower()
    if first_name in fullname:
        return True
    return False

full_name = "Ivan Ivanov"
first_name = "Ivan"
print(is_check_name(full_name, first_name))

# ======================================================
import re
from re import search
regex_JP = r"^81"
regex_SG = r"^65"
regex_TW = r"^886"
regex_UA = r"^380|^0[1-9][1-9]" 
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone

def get_phone_numbers_for_countries(list_phones):
    phone_list = {
    "UA": [],
    "JP": [],
    "TW": [],
    "SG": []
    }
    for phone in list_phones:
        sanitize_phone = sanitize_phone_number(phone)
        if search(regex_UA, sanitize_phone):
            phone_list["UA"].append(sanitize_phone)
        elif search(regex_SG, sanitize_phone):
            phone_list["SG"].append(sanitize_phone)
        elif search(regex_TW, sanitize_phone):
            phone_list["TW"].append(sanitize_phone)
        else:
            phone_list["JP"].append(sanitize_phone)
    print(phone_list)       
    return phone_list
get_phone_numbers_for_countries(['0658759411', '818765347', '818765344', '8867658976', '657658976'])

# ==============================================================
from re import search, sub
def is_spam_words(text, spam_words, space_around=False):
    reg_exp = r"[^a-zA-Z0-9а-яА-Я ]"
    text = text.lower()
    text = sub(reg_exp, "", text)
    new_text_list = text.split()
    if space_around:
        for word in new_text_list:
            if word in spam_words:
                return True
    else:
        for  word in spam_words:
            if search(word, text):
                return True
    return False
# ================================================================
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
print (len(CYRILLIC_SYMBOLS))
print (len(TRANSLATION))
TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()  
print (TRANS)


def translate(name):
    return name.translate(TRANS)
print (translate("Олекса Івасюк"))

# ===========================================
grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}


def formatted_grades(students):
    new_list = []
    count = 1
    for stud in students:
        print(stud)
        print(students[stud])
        print (grades[students[stud]])
        new_list.append("{:>4}|{:<10}|{:^5}|{:^5}".format(count, stud, students[stud], grades[students[stud]]))
        count += 1
    print(99999, new_list)
    return new_list

for el in formatted_grades(students):
    print(el)
# =============================================================

def formatted_numbers():
    new_list = []
    header = "|{:^10}|{:^10}|{:^10}|".format("decimal", "hex", "binary")
    new_list.append(header)
    for num in range(16):
        new_list.append("|{0:<10d}|{0:^10x}|{0:>10b}|".format(num))
    return new_list

for el in formatted_numbers():
    print(el)
# header = "|{:^10}|{:^10}|{:^10}|".format("decimal", "hex", "binary")
# print(header)
# for i in range(16):
#     print ("|{0:<10d}|{0:^10x}|{0:>10b}|".format(i))
# ==============================================================

import re
def find_word(text, word):
    res = {
            'result': False,
            'first_index': None,
            'last_index': None,
            'search_string': word,
            'string': text
        }
    results = re.search(word, text)
    if results:
        res['result'] = True
        res['first_index'] = results.span()[0]
        res['last_index'] = results.span()[1]
        res['search_string'] = results.group()
        res['string']= text
        return res 
    else:
        return res 
        
text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
word = "Python"

print(find_word(
"Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
"Python"))

# ================================================================

import re
def find_all_words(text, word):
    regexp = re.compile(word, re.IGNORECASE)
    results = re.findall(regexp, text)
    return results

        
text = "Guido van Rossum began PyTHon working PYTHON on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
word = "Python"

print(find_all_words(text, "Python"))

# ================================================================

import re

def find_all_emails(text):
    result = re.findall(r"[A-Za-z]+[(A-Za-z)0-9_\.-]+@[A-Za-z0-9]+\.[A-Za-z0-9]{2,4}", text)
    return result

regex = r"[a-zA-Z]{1}[\w\.]+@[a-zA-z]+\.[a-zA-Z]{2,}"
test_str = "Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net"
matches = re.finditer(regex, test_str)

for match in matches:
    print(f"{match.group()} start: {match.start()} end: {match.end()}")
# ==================================================================

