nombres = ['Harry Houdini', 'Newton', 'David Blaine',
           'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']

# Separar los nombres en tres grupos: magos, científicos y otros
magos = []
cientificos = []
otros = []

for nombre in nombres:
    if nombre in ['Harry Houdini', 'David Blaine', 'Teller']:
        magos.append(nombre)
    elif nombre in ['Newton', 'Hawking', 'Einstein']:
        cientificos.append(nombre)
    else:
        otros.append(nombre)

# Función para modificar la lista de magos


def hacer_grandioso():
    for i in range(len(magos)):
        magos[i] = 'El gran ' + magos[i]

# Función para imprimir los nombres


def imprimir_nombres():
    print("--------------------------")
    print("Magos:")
    print("--------------------------")

    for mago in magos:
        print(mago)
        print("--------------------------")

        print("--------------------------")
    print("Científicos:")
    print("--------------------------")
    for cientifico in cientificos:
        print(cientifico)


# Imprimir la lista completa de nombres antes de ser modificados
print("--------------------------")
print("Lista completa de nombres:")
print("--------------------------")
for nombre in nombres:
    print(nombre)


# Modificar la lista de magos
hacer_grandioso()

# Imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes
imprimir_nombres()
print("--------------------------")

print("--------------------------")
print("Otros:")
print("--------------------------")
for otro in otros:
    print(otro)
