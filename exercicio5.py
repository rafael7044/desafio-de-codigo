string = "capivara"

string_invertida = ""

for i in range(len(string) -1, -1, -1):
    string_invertida = string_invertida + string[i]


print(f"String invertida: {string_invertida}")