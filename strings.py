text = """       This Is First Line   And Second Line   Last Third Line        """

song = '''Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one horse open sleigh'''
print ("is title", text.istitle()) # чи починаються слова в рядку з великої літери;
print ("is space", text.isspace()) # чи складається рядок з невідображуваних символів (пробіл, ознаки кінця сторінки '\f' і рядка '\n', переведення каретки '\r', горизонтальна табуляція '\t' і вертикальна табуляція '\v')

print (text)
print(text.count("line"))
print(text[:6:])
print(text[2:6:])
print(text[::-1]) # ззаду наперед
print ("is title", song.istitle()) # чи починаються слова в рядку з великої літери;


text = text.strip() # — видалення символів пробілів на початку і в кінці рядка;
                    # "лівий", lstrip, видаляє тільки пробіли на початку рядка;
                    # та "правий", rstrip, видаляє тільки пробіли в кінці рядка.
text = text.upper()
print(text)
text = text.title() # — першу букву кожного слова переводить в верхній регістр, а всі інші в нижній;
print(text)
print(text.swapcase()) #перекладає символи нижнього регістра в верхній, а верхнього — в нижній;

print("="*100)
print(song.startswith("Jingle")) # — чи починається рядок S з шаблону str;
print(song.endswith("sleigh")) # —чи закінчується рядок S шаблоном str;

print("split ", text.split("  ")) #— розбиття рядка за роздільником;
text_list = text.split("  ") # split  double-space  ['This Is First Line', ' And Second Line', ' Last Third Line']
text_str = " ".join(text_list)
print ("join ", text_str)

jingle_bells = "Jingle bells, jingle bells\nJingle all the way\nOh, what fun it is to ride\nIn a one horse open sleigh"
print (jingle_bells)

dogs_text = "All dogs bark like dogs."
cats_text = dogs_text.replace("dogs", "cats")
print("replace ", cats_text) # All cats bark like cats.

# Для видалення фіксованої послідовності на початку рядка є метод removeprefix:
print('TestHook'.removeprefix('Test'))   # Hook
print('TestHook'.removeprefix('Hook'))   # TestHook

# Є парний метод для видалення послідовності в кінці рядка, removesuffix:

print('TestHook'.removesuffix('Hook'))   # Test
print('TestHook'.removesuffix('Test'))   # TestHook

# В рядках є метод translate, цей метод дозволяє замінити символ в рядку на інший з мапи відповідності, яку можна задати.
map = {ord('з'): 'z', ord('ю'): 'u', ord('д'): 'd'}
translated = 'зю АБВГ д'.translate(map)
print(translated) # zu

#  Форматування рядків (метамова форматування)

# Наприклад, вивести числа від 1 до 5 в десятковому, шістнадцятковому, вісімковому і двійковому представленні:

for i in range(6):
    s = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i)
    print(s)
#width = 5
for num in range(12):
    print('{:^10} {:^10} {:^10}'.format(num, num**2, num**3))



