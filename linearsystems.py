import re
addEquation = True

print("Enter your equations below...")
print("Hint: Make sure to put spaces between varialbes!!!")
print("Type \"SOLVE\" to solve the equation")
equations = []
while addEquation:
    eqstring = input("Equation: ")
    if eqstring == "SOlVE":
        break
    else:
        matrix1 = []
        matrix2 = []
        spliteq = eqstring.split("=")
        matrix1 = re.findall(r"\d+", spliteq[0])
        matrix2 = re.findall(r"\d+", spliteq[1])
        print(f"{matrix1} {matrix2}")
    
