file = open("esperanto-text.txt", "r")
"""
aSentence = "What_an_incredible_game_!"
aSentence2 = "tutu on the tuki-kata"
a_two = '''
We_don't_play_with_it
Be_polite
Be_professional
'''
print(a_two)
print(aSentence)

print(aSentence[0])
print(aSentence[12])
print(aSentence[-1])

print(aSentence[0:3])
print(len(aSentence))  #for lenght

print("_d" not in aSentence)
tab = aSentence[5:]
print(tab)
print(aSentence[:5])
print(aSentence[-4: -1])

a = " Just remember ALL CAPS when you spell the man name."
print(a.upper())
print(a.lower())
print(a.strip()) # remove the space before and/or after the actual text 

print(aSentence2.replace("u", "a")) # replace a string
        
string = "Hello, world!"

print(string.split(",")) #split the string into substringd if it finds instances of the separator |=> becoming an array
print(string)
print("Welcome".upper())

position = string.find("rld") # this method finds the first occurence of the specified value and return its position, if not, returns -1
# position2 = string.index("ss") # this method is the same as find(), the only difference is that it raises an exception if the value is not found
print(position)
# print(position2)

p = "abcdefghij"
print(p[::-2][:5][::-1][3:]) # c'est juste une concaténation, tu as quatres opérations à faire. tu fais d'abord la première, ensuite tu fais la deuxième avec le résultat de la première, ainsi de suite


given_string = input("Enter something: ")
i = 0
while i < 10:
    print(given_string)
    i += 1

print("hello", 42)

s1, s2, s3 = "42", "is", "the answer"
print(s1, s2, s3)

# data
cat, garden, mice = "CAT", "GARDEN", "MICE"
strings1 = "the CataCat attaCk a Cat"
strings2 = "thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN"
# operation strings 1
x1 = strings1.upper().count(cat) + strings1.upper().count(garden) + strings1.upper().count(mice)
y1 = strings1.upper()[::-1].count(cat) + strings1.upper()[::-1].count(garden) + strings1.upper()[::-1].count(mice)
print(strings1, "should return", x1+y1)
# operation strings 2
x2 = strings2.upper().count(cat) + strings2.upper().count(garden) + strings2.upper().count(mice)
y2 = strings2.upper()[::-1].count(cat) + strings2.upper()[::-1].count(garden) + strings2.upper()[::-1].count(mice)
print(strings2, "should return", x2+y2)

username = input("What's your name Mr/Mrs/Ms ? ")
print("Hello", username.capitalize(), "!")

number = input("Enter a number : ")
print(type(number))

numbers = input("Enter two numbers (separated by a space) : ")
numbers_list = numbers.split()
print("Sum : ", float(numbers_list[0]) + float(numbers_list[1]))

# task 3.4
x = ""
sentence = input("Enter a word or a sentence : ")
sentence = sentence.strip().split()
for word in sentence:
    x = x + word[0]
print("Final word base on the first letter of each word in the string : ", x)
"""

# task 3.5
# esperanto
a = ["A", 11.55]
i = ["I", 10.41]
e = ["E", 9.05]
o = ["O", 8.86]
n = ["N", 7.75]
l = ["L", 6.16]
s = ["S", 5.97]
r = ["S", 5.88]
t = ["T", 5.38]
k = ["K", 4.08]
j = ["J", 3.32]
u = ["U", 3.01]
m = ["M", 2.99]
d = ["D", 2.91]
p = ["P", 2.91]
v = ["V", 1.81]
g = ["G", 1.33]
f = ["F", 1.07]
b = ["B", 1.03]
c = ["C", 1.00]
g_chap = ["Ĝ", 0.69]
c_chap = ["Ĉ", 0.60]
z = ["Z", 0.54]
u_bizz = ["Ŭ", 0.50]
h = ["H", 0.42]
s_chap = ["Ŝ", 0.36]
j_chap = ["Ĵ", 0.09]
h_chap = ["Ĥ", 0.01]
esperanto = []
esperanto.insert(0, a)
esperanto.insert(1, i)
esperanto.insert(2, e)
esperanto.insert(3, o)
esperanto.insert(4, n)
esperanto.insert(5, l)
esperanto.insert(6, s)
esperanto.insert(7, r)
esperanto.insert(8, t)
esperanto.insert(9, k)
esperanto.insert(10, j)
esperanto.insert(11, u)
esperanto.insert(12, m)
esperanto.insert(13, d)
esperanto.insert(14, p)
esperanto.insert(15, v)
esperanto.insert(16, g)
esperanto.insert(17, f)
esperanto.insert(18, b)
esperanto.insert(19, c)
esperanto.insert(20, g_chap)
esperanto.insert(21, c_chap)
esperanto.insert(22, z)
esperanto.insert(23, u_bizz)
esperanto.insert(24, h)
esperanto.insert(25, s_chap)
esperanto.insert(26, j_chap)
esperanto.insert(27, h_chap)


esperanto_text = file.read()
removeThis = [" ", "-", ".", '"', ",", "\n", "!"]
for x in removeThis:
    esperanto_text = esperanto_text.replace(x, "")

esperanto_text = esperanto_text.upper()
print(len(esperanto_text))
