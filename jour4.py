import re
file = open("data.txt", "r")
"""
# task 1.1
print(42 > 12)
print(12 == 12)
print("hello" == "world")
print(218 >= 118)
print("a".upper() == "A")
print(1*2*3*4 <= 9)
print("z" in "azerty")

# task 1.2
number_verify = 0
while number_verify != 42:
    number_verify = int(input("Write an integer :"))
print("This is correct!")

# task 1.3
interger1 = int(input("Enter an integer : "))
if interger1 % 2 == 0:
    print("This integer is even")
else:
    print("This integer is odd")

# task 1.4
string1 = True
while string1:
    string1 = input("Enter a string to open the gate : ")
    if string1 == "open sesame":
        print("access granted")
        string1 = False
    elif string1 == "will you open, you goddamn !@&/°":
        print("access fucking granted")
        string1 = False
    else:
        print("permission denied")

# task 1.5
def task1_5(number):
    param = 42
    if number  == param:
        print("a")
    elif number <= param // 2:
        print("b")
    elif number < param // 2:
        print("d")    
    elif number % 2 == 0:
        print("c")
    elif number % 2 != 0 and number >= param + 3:
        print("e")
    else:
        print("f")
        
task1_5(int(input("Enter an integer : ")))

# task 1.6
a = 42
b = 41
if a == b:
    print("A and B are the same")
else:
    print("A and B are different")
if b < a:
    print("B is lower than A")


# task 2.1
indice = 1
while indice <= 1000:
    print(indice)
    indice += 1

#task 2.2
string2 = input("Enter a string : ")
for x in string2:
    print(x+x, end="")
print()

# task 2.3
def divisible_par_7(number):
    str_number = str(number)
    number_length = len(str_number)
    final_valeur = number
    while number_length > 2:
        final_valeur = int(str_number[-1])*5 + int(str_number[:number_length-1])
        number_length = len(str(final_valeur))
        str_number = str(final_valeur)
    if final_valeur % 7 == 0:
        return True
    else:
        return False

i = 10000
while i >= 1:
    verdict = divisible_par_7(i)
    if verdict:
        print(i, "is divisible by 7")
    i -= 1

# task 2.4
integer = -30
while integer <= 30:
    if integer % 3 == 0 and integer % 5 == 0:
        print("FizzBuzz")
    elif integer % 5 == 0:
        print("Buzz")
    elif integer % 3 == 0:
        print("Fizz")
    else:
        print(integer)
    integer += 1


# task 2.5
def print_song_lyrics(n):
    song_lyrics = f'''
{n} bottles of beer on the wall.
{n} bottles of beer.
If one of the bottles just happen to fall,
'''
    print(song_lyrics)

n = 99
while n >=0 :
    if n != 0:
        print_song_lyrics(n)
    else:
        print(
            '''
No more bottles of beer on the wall,
no more bottles of beer.
Go to the store and buy some more.
            ''')
    n -= 1

#task 2.6
i = 2
n = int(input("Enter an integer :"))
x = n
while i <= n/2:
    while x >= 1:
        if n > i*x:
            print(i*x, end=" ")
        x -= 1   
    i += 1
    x = n
    print()

# CHALLENGE
# regex
regex = '[aeiouAEIOU]'
int_and_string = input("Enter simultaneously an integer and a string : ").strip().split()
if int(int_and_string[0]) == 0:
    exit()
elif re.search(regex, int_and_string[1]) or int(int_and_string[0]) >= 42:
    print(int_and_string[0])
else:
    print(int_and_string[1])
"""
    
# task 3.1
key = int(input("Enter a key(number, at least 1) : "))
message = input("Enter a clear message(string) : ").upper()


def encrypt_message(key_, message_):
    alphabet = file.read().strip().split()
    tab = ['', '', '', '', '', '', '', '', 
        '', '', '', '', '', '', '', '', 
        '', '', '', '', '', '', '', '', 
        '', '']
    lenght = len(alphabet)-1
    tab_message = []

    for x in alphabet:
        index_de_x = alphabet.index(x)
        index_et_key = index_de_x + key_
        if index_et_key < lenght-1:
            tab[index_et_key] = x
        else:
            tab[index_et_key - lenght - 1] = x
    
    print(alphabet)
    print(tab)

    for y in message_:
        index_de_y = alphabet.index(y)
        tab_message.append(tab[index_de_y])

    res = ''.join(tab_message)
    print(res)

encrypt_message(key, message)

"""
# task 3.2
message_crypted = input("Enter a message crypted(string) : ").upper()

def encrypt_alphabet(key_):
    alphabet = file.read().strip().split()
    tab = ['', '', '', '', '', '', '', '', 
        '', '', '', '', '', '', '', '', 
        '', '', '', '', '', '', '', '', 
        '', '']
    lenght = len(alphabet)-1

    for x in alphabet:
        index_de_x = alphabet.index(x)
        index_et_key = index_de_x + key_
        if index_et_key < lenght-1:
            tab[index_et_key] = x
        else:
            tab[index_et_key - lenght - 1] = x
    return tab


def decrypt_message(message_):
    alphabet = file.read().strip().split()
    tab_message = []
    tabs = list()
    for i in range(1,26):
        tabs.append(encrypt_alphabet(i,alphabet))
    tab1 = encrypt_alphabet(1, alphabet)
    tab2 = encrypt_alphabet(2, alphabet)
    tab3 = encrypt_alphabet(3, alphabet)
    tab4 = encrypt_alphabet(4, alphabet)
    tab5 = encrypt_alphabet(5, alphabet)
    tab6 = encrypt_alphabet(6, alphabet)
    tab7 = encrypt_alphabet(7, alphabet)
    tab8 = encrypt_alphabet(8, alphabet)
    tab9 = encrypt_alphabet(9, alphabet)
    tab10 = encrypt_alphabet(10, alphabet)
    tab11 = encrypt_alphabet(11, alphabet)
    tab12 = encrypt_alphabet(12, alphabet)
    tab13 = encrypt_alphabet(13, alphabet)
    tab14 = encrypt_alphabet(14, alphabet)
    tab15 = encrypt_alphabet(15, alphabet)
    tab16 = encrypt_alphabet(16, alphabet)
    tab17 = encrypt_alphabet(17, alphabet)
    tab18 = encrypt_alphabet(18, alphabet)
    tab19 = encrypt_alphabet(19, alphabet)
    tab20 = encrypt_alphabet(20, alphabet)
    tab21 = encrypt_alphabet(21, alphabet)
    tab22 = encrypt_alphabet(22, alphabet)
    tab23 = encrypt_alphabet(23, alphabet)
    tab24 = encrypt_alphabet(24, alphabet)
    tab25 = encrypt_alphabet(25, alphabet)
    global_tab = []
    global_tab.append(tab1)
    global_tab.append(tab2)
    global_tab.append(tab3)
    global_tab.append(tab4)
    global_tab.append(tab5)
    global_tab.append(tab6)
    global_tab.append(tab7)
    global_tab.append(tab8)
    global_tab.append(tab9)
    global_tab.append(tab10)
    global_tab.append(tab11)
    global_tab.append(tab12)
    global_tab.append(tab13)
    global_tab.append(tab14)
    global_tab.append(tab15)
    global_tab.append(tab16)
    global_tab.append(tab17)
    global_tab.append(tab18)
    global_tab.append(tab19)
    global_tab.append(tab20)
    global_tab.append(tab21)
    global_tab.append(tab22)
    global_tab.append(tab23)
    global_tab.append(tab24)
    global_tab.append(tab25)

    for z in global_tab:
        for y in message_:
            if 
            index_de_y = z.index(y)
            tab_message.append(alphabet[index_de_y])

        res = ''.join(tab_message)
        print(res)
"""

#encrypt_alphabet(5)
#decrypt_message(message_crypted)

