from pathlib import Path
import re
new_file = ""
path = Path("/Users/oshchyrskyi/Documents/Python_GO_IT/My_repo/First_repo/test.txt")
with open (path, "r") as file:
    for line in file:
        if line[-2].isdigit() and line[-1] == "\n":
            continue
        else:
            print(line)
            x = line.rfind("0")
            
            print (x)