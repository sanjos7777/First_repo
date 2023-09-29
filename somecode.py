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

res = "",
print("111   ",str_1[:-1])
print("222   ", str_1[-1])

res = ", ".join(str_1)
print("res  ", res)