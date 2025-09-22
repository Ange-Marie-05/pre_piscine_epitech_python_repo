import math

i, n, b = 1, 9, 0
while i < n:
    a = i*10**(n-i)
    b += a
    i += 1
print(b)

nbr = 5
if nbr % 2 == 0:
    print("even")
else:
    print("odd")

print("Addition de nombres")
liste_recu = input("Entrez les nombres succèssivement (espacer entre eux): ")
nbr_recu = liste_recu.split()
somme = 0
for terme1 in nbr_recu:
    somme += int(terme1)

print("somme des nombres saisies: ", somme)


print("Integer")
nombre_float = float(input("Enter the float number: "))
nombre_int = int(nombre_float)
print("Integer base on your input: ", nombre_int)


print("decimal part")
float_nbr = float(input("Enter the float number: "))
int_nbr = int(float_nbr)
print("Decimal part of your input: ", float_nbr-int_nbr)

chiffre = math.pi
print(round(chiffre, 6)) # to rounds a float number

