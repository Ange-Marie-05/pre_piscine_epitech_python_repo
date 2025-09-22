import datetime
import os
import re
start = datetime.datetime.now()
from typing import TypeVar, Sequence
B = TypeVar('B')
I = TypeVar('I')
S = TypeVar('S')

"""
# task 1.1
def f1():
    return 42
def f2(x):
    return 2 * x
print(f1())
print(f2(5) + f1())


# task 1.2
def bread():
    print("<//////////>")
    return ''
def lettuce():
    print(" ~~~~~~~~~~~~ ")
    return ''
def tomato():
    print(" O O O O O")
    return ''
def ham():
    print(" ============ ")
    return ''
print(bread(), lettuce(), tomato(), ham(), ham(), bread())


# task 1.3
for i in range(1, 5):
    print(bread(), lettuce(), tomato(), ham(), ham(), bread())

# task 1.4
def numberOfSandwiche(number = input("How many swandwiche(s) would you like : ")):
    while number.isdigit() != True or int(number) <= 0:
        number = input("How many swandwiche(s) would you like (We need a positive number) : ")
    return int(number)
        
for i in range(0, numberOfSandwiche()):
    print(bread(), lettuce(), tomato(), ham(), ham(), bread())


# task 1.5(4.3)
def numberOfSandwiche(number = input("How many swandwich(es) would you like : "), *veg):
    veg = input("yes or no, do you want veg sandwich ?").strip()
    while number.isdigit() != True or int(number) <= 0:
        number = input("How many swandwiche(s) would you like (We need a positive number) : ")
    return [int(number), veg]
param = numberOfSandwiche()
for i in range(0, param[0]):
    if param[1] == "yes":
        print(bread(), lettuce(), lettuce(), tomato(), tomato(), bread())
    else:
        print(bread(), lettuce(), tomato(), ham(), ham(), bread())

# CHALLENGE
def power_function (nombre, puissance):
    if puissance > 0:
        resultat = nombre * power_function(nombre, puissance-1)
    else:
        resultat = 1
    return resultat
print(power_function(42, 84))
print(datetime.datetime.now() - start)

# task 2.1
def sum_function (number):
    if number > 0:
        resultat = number + sum_function(number-1)
    else:
        resultat = 0
    return resultat
print(sum_function(42))

# task 2.2
def palindrome_function (string1 = input("Enter a string of characters : ").strip("!?.").lower().split()):
    return True


# task 2.3
list = os.scandir() # If the path is not specified then the current working directory is used as a path.
# The os.scandir() method is used to get an iterator of os.DirEntry objects 
# corresponding to the entries in the directory given by specified path.
for entry in list:
    if entry.is_dir or entry.is_file:
        print(entry.name)
list.close()
# to close the iterator and free acquired resources use scandire.close() method
"""

# task 3.1
def funA(s, n):
    if len(s.strip(" ")) >= n:
        return True
    else:
        return False
    
regex = r"[$.,?*+\-\/!]"
def funB(s, n):
    x = re.findall(regex, s)
    if len(x) >= n:
        return True
    else:
        return False
    
regex2 = r"[0123456789]"
def funC(s, n):
    x = re.findall(regex2, s)
    if len(x) >= n:
        return True
    else:
        return False

#x = funA(input("Enter a string : "), int(input("Enter an integer : ")))
#y = funB(input("Enter a string : "), int(input("Enter an integer : ")))
#z = funC(input("Enter a string : "), int(input("Enter an integer : ")))
#print(z)

# task 3.2
def passcheck(func, valeur : I, password : S):
    x = func(password, valeur)
    if x == True:
        print("Good password")
        #return True
    else:
        print("Bad password")
        #return False

nbr: int = int(input("Enter a number : "))
string: str = input("Enter a password : ")
passcheck(funA, nbr, string)


"""
if x == y == z == True:
    print("Verdict: Very strong password")
elif x != y or y != z or z != x:
    print("Verdict: Not bad...")
elif x == y == z == False:
    print("Verdict: Dumb")
"""

# task 3.3




