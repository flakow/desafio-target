string = "PREECISO DE UM EMPREGO NO MERCADO DE T.I"
inverter_string = ""

for i in range(len(string)-1, -1, -1):
    inverter_string  += string[i]

print(inverter_string)