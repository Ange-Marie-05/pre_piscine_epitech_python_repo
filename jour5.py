import random
import math
import datetime
start = datetime.datetime.now()
"""

# task 1.1
mylist = ["1", "2", "3", "4", "5"]
print(mylist[0])

# task 1.2
print(mylist[-1])

#task 1.3
mylist.append(42)
mylist.append("forty-two")

# task 1.4
print(mylist)
for x in mylist:
    print(x)

# task 1.5
mylist.pop()
print(mylist)

# task 1.6
mylist.insert(0, "0")
print(mylist)

# task 1.7
print(mylist[2:5])

# task 1.8
mylist.reverse()
print(mylist)

# task 1.9
print(mylist[::2])

# task 1.10
ten_integers = 11
while ten_integers <= 21:
    mylist.append(ten_integers)
    ten_integers += 1
print(mylist)

# task 1.11
my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
# my_first_list.extend(my_second_list) # same as the next line
my_first_list = [*my_first_list, *my_second_list]
# * est pour dépaqueter une séquence. Il sert aussi à fusionner  des collection
print(my_first_list)

# task 2.1
result = 1
for x in range(1, 6):
    result *= x
print(result)

# task 2.2
print([x + 10 for x in [3, 2, 6, 7, 1, 4]]) # modification in a list whith a for loop in one line

# task 2.3
test = [*filter(lambda a: a < 10, [42, 3, 4, 7])]
# filter prend en paramètre une fonction et un truc à filtrer
# IL filtre le tout et retourne un iterable(qui n'est pas directement utilisable
#  - so ne pas oublier de récupérer la valeur dans une liste )
print(test)

# task 2.4
mylist2 = [3, 2, 6, 7, 1, 4]
min, max = min(mylist2), max(mylist2)
print(f"max : {max} \nmin : {min}")


# task 2.5
mylist2.sort(reverse = True)
print(mylist2)

# task 2.6
test2 = [x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]]
# pour chaque élement de la liste, faire:
# x // 2  si x est pair ou
# x * 2 si ce n'est pas le cas
print(test2)

# task 2.7
test2 = [*enumerate([42, 3, 4, 18, 3, 10])]
# enumarate prend une collection de chose (liste, tuple..) et la retourne comme
# un bojet numéroter
# * est pour dépaqueter une séquence. Il sert aussi à fusionner  des collection
print(test2)

# task 2.8
first_names = ["Jackie" , "Chuck" , "Arnold" , "Sylvester"]
last_names = ["Stallone" , "Schwarzenegger" , "Norris" , "Chan"]
magic = [* zip ( first_names , last_names[::-1]) ]
print(magic)
print (magic[0])
print (magic[3])
print (magic[1][0])
print (magic[0][1])

# CHALLENGE
x = 1
sort_list = []
while x <= 1000000:
    sort_list.append(random.randrange(1, 9999999))
    x += 1
sort_list.sort()
print(sort_list)
print(datetime.datetime.now() - start)


# task 3.1
student = {
    "player" : "Charles",
    "team" : "anonymous"
}
print(student)
print(student.keys())
print(student.values())


# task 3.2
superheroes = {
    "Batman" : {
        "id" : 1,
        "aliases" : ["Bruce Wayne", "Dark Knight"],
        "location" : {
            "number" : 1007,
            "street" : "Mountain Drive",
            "city" : "Gotham"
        }
    },
    "Superman" : {
        "id" : 2,
        "aliases" : ["Kal-El", "Clark Kent", "The Man of Steel"],
        "location" : {
            "number" : 344,
            "street" : "Clinton Street",
            "apartment" : "3D",
            "city" : "Metropolis"
        }
    }
}
print(f"Superman's city : {superheroes["Superman"]["location"]["city"]}")

# task 3.3
superheroes["Batman"]["aliases"] = ["Bruce Wayne", "Dark Knight", "Caped Crusader"]
print(superheroes["Batman"]["aliases"])
# revoir une manière de faire indépendamment des éléments

# task 3.4
random_dictionary = {
    " dalmatians ": 101 ,
    " pi ": 3.14 ,
    " beast ": 3*2*111 ,
    " life ": 42 ,
    " googol ": 10^100
}
random_dictionary_values = []
for x in random_dictionary:
    random_dictionary_values.append(random_dictionary.get(x))

for x in random_dictionary.items():
    print(type(x))
    if x[1] == max(random_dictionary_values):
        max_key = x[0]
print(f"max key : {max_key}")

# task 4.1
list_of_names = "the ambassador's banquet guest".strip().split(" ")
name = input("Write your name : ")
if name.lower() in list_of_names:
    print("Welcome")
else:
    print("get lost!")

# task 4.2
list2 = [1, 1, 2, 2, 3]
list2 = list(dict.fromkeys(list2)) # dict.fromkeys() permet de retirer les doublons d'une liste
print(list2)
"""

# task 4.3
programme = [
    ["Monday", "3:30 PM", "Joe", "Sam"],
    ["Monday", "4:30 PM", "Bob", "Alice"],
    ["Tuesday", "3:30 PM", "Joe", "Bob", "Alice", "Sam"],
    ["Tuesday", "9:30 AM", "Joe", "Bob"]
]
individual_programme = []
name_given = input("Enter the name : ")
for x in programme:
    for y in x:
        if y == name_given:
            gram = x[0] + " " + x[1]
            individual_programme.append(gram)

print(f"Day and time of all meetings ({name_given}) : {individual_programme}")
            

