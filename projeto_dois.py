#invertendo strings e listas
def inverter(s):
    return s[::-1]

cores_invertido = []

cores = ["Amarelo", "Vermelho", "Roxo", "Azul"]
for cor in cores:
    cores_invertido.append(inverter(cor.lower()))

print(inverter(cores_invertido))