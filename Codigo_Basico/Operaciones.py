# Operaciones basicas con enteros

print(44 + 3)
print(43 - 2)
print(23 * 3)
print(5 / 4)
print(102 % 3)
print(101 // 3)
print(21 ** 3)
print(2 ** 4 + 1 - 7 / 5 // 4)

#Con cadenas de texto
print("Hola " + "Mundo " + "Soy")
print("Hola " + str(5))

#Mixtas
print("Holaaa " * 3)
print("Hola! " * (3 ** 4))

floatv = 3.1 * 2
print("Hola! " * int(floatv))

# Operaciones de comparativos con enteros
print(2 > 4) 
print(2 < 4)
print(2 >= 4)
print(2 <= 4)
print(2 == 4)
print(2.3 != 4)

#Con cadenas de texto
print("Hola" > "Mundo") 
print("Hola" < "Mundo")
print("aaaa" >= "abcaa") # Ordenación alfabética ASCII
print(len("aaaa") >= len("abcd")) # Cuenta los caracteres
print("Hola" <= "Mundo")
print("Hola" == "Hola")
print("Hola" != "Mundo")

#Lógicos
print(2 > 4 and "Hola" > "Mundo")
print(2 > 4 or "Hola" > "Mundo")
print(2 < 4 and "Hola" < "Mundo")
print(2 < 4 or "Hola" > "Mundo")
print(2 < 4 or ("Hola" > "Mundo" and 4 == 4))
print(not(2 > 4))
