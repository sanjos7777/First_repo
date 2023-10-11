# file = open('test.txt', 'w')
# file.write("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000")
# file.close()
file = open('test.txt', 'r' )
import re
res = 0
regex_sal = r"\d+"
while True:
    line = file.readline()
    if line:
        found = re.search(regex_sal, line)
        salary = float(int(found.group()))
        res += salary
    else:
        break
print ("res ", res)
file.close()

# =======================================

file = open("text.txt", "w+")
employee_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19'], ['sdnfns, 22', 'smflns sfjn, 99']]
res = str()
for employee in employee_list:
    print (1 , employee)
    if len(employee) > 1:
        for employ in employee:
            print (2 , employ)
            res = res + f"{employ}\n"
    else:
        res = res + f"{employee[0]}\n"

print ("res ", res)
file.write(res)
file.seek(0)
text = file.read()
print("fi",text)
file.close()

# ====================================

file = open("text.txt", "r")
res = list()
for line in file:
    norm_line = line.replace("\n", "")
    res.append(norm_line)
    print (line)
print(res)
file.close()

# ==============================
file = open("text.txt", "a")
text = "Drake Mikelsson,19"
file.write(f"{text}\n")
file.close()

# ================================

with open ("ex5.txt", "r") as file:
    list_cat  = []
    names = ["id", "name", "age"]
    for line in file:
        line = line.replace("\n", "")
        list_line = line.split(",")
        record = dict(zip(names, list_line))
        print ("record ", record)
        list_cat.append(record)
    print(1, list_cat)

#  ================================

def get_recipe(path, search_id):    
    import re
    all_data = []
    recipe = {"id":"",
            "name":"",
            "ingredients":[]
            }
    with open(path, "r") as file:
        for line in file:
            line = line.replace("\n", "")
            list_line = line.split(",")
            all_data.append(line)
            if re.search(search_id, line):
                list_line = line.split(",")
                recipe["id"] = list_line[0]
                recipe["name"] = list_line[1]
                recipe["ingredients"] = list_line[2:]
                print("re ", recipe)
                return recipe
            else:
                continue
            
        return None
print (get_recipe("recipe.txt", "60b90c3b13067a15887e1ae4"))

def get_recipe(path, search_id):
    result = None
    with open(path, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0] == search_id:
                result = {"id": parts[0], "name": parts[1], "ingredients": parts[2:]}
                break
    return result

# 7=======================================================

def sanitize_file(source, output):
    with open (source, "r") as file:
        content = file.read()
    from re import sub
    content = sub("\d", "", content)
    with open(output, "w") as file:
        file.write (content)

# 8=======================================================

def save_applicant_data(source, output):
    res = ""
    for each in source:
        new_str = list(each.values())
        for item in range(len (new_str)):
            if item == len(new_str) - 1:
                res += f"{new_str[item]}\n"
            else:    
                res += f"{new_str[item]}," 
    with open (output, "w") as file:
        file.write(res)
a = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]
save_applicant_data(a, "output.txt")

# 10=======================================

def is_equal_string(utf8_string, utf16_string):
    first = utf8_string.decode()
    second = utf16_string.decode('utf-16')
    if first == second :
        return True
    else:
        return False

# 11==================================
def get_credentials_users(path):
    res = []
    with open (path, "rb") as file:
        users = file.read().decode()
        print (users)
        res = users.split("\n")
        return res
    
# 12==================================
import base64


def encode_data_to_base64(data):
    users_base64 = []
    for each in data:
        each_bytes = each.encode("utf-8") # Змінну each конвертуємо в байтовий об'єкт, використовуючи рядковий метод encode, і зберігаємо його в each_bytes
        base64_bytes = base64.b64encode(each_bytes) # ми кодуємо each_bytes та зберігаємо результат в base64_bytes, використовуючи base64.b64encode метод
        base64_user = base64_bytes.decode("utf-8") # ми отримуємо представлення перетворення Base64 у вигляді рядка, декодуючи змінну base64_bytes
        users_base64.append(base64_user) #
    return users_base64

# 13 =========================================
import shutil
def create_backup(path, file_name, employee_residence):
    with open (f"{path}/{file_name}", "wb") as file:
        for key, value in employee_residence.items():
            single_user = f"{key} {value}\n"
            b_single_user = single_user.encode()
            file.write(b_single_user)
    return shutil.make_archive('backup_folder', "zip", path)

# 14 =======================================
