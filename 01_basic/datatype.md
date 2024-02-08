object types / data type

- Number : 1234, 3.14, 3+4j, 0b111, Decimal(), fraction()
-string: 'spam' , "BOb's", b'a\x01c'
-List : [1, [2, 'three'], 4, 5]
-Turple : (1, 'spam', 4, 'U'),turple('spam'), namedturple
Dictionary : {'food': 'spam', 'taste' : 'yum'}, dict(hours=10)

- set : set('abc'), {'a', 'b', 'c'}

- File : open('eggs.txt'), open(r'C:\ham.bim', 'wb')

-Bollean : true, False
- None : none
- functions,modules,classes

- Advance : Decorators, Generators, Iterators, MetaProgramming



terminal
SKY Computer@JAYMAHAKAL MINGW64 /d/python (main)
$ python
Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 4+4
8   
>>> 4/4
1.0 
>>> 4%4
0   
>>> 4%1
0   
>>>  x = 2
  File "<stdin>", line 1
    x = 2
IndentationError: unexpected indent
>>> x = 2
>>> y = 3
>>> z = 4
>>> x+y
5
>>> x // y
0
>>> y / x
1.5
>>> x + y * z
14
>>> (x + y) * z
20
>>> 'rajiv' + 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> int(2.23)
2   
>>> float(40)
40.0
>>> 'chai' + 'code'
'chaicode'
>>> x, y, z
(2, 3, 4)
>>> x +1 , y *2
(3, 6)
>>> y % 2
1   
>>> z ** 2
16  
>>> 2 ** 1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
>>> result 1/3.0
  File "<stdin>", line 1
    result 1/3.0
           ^
SyntaxError: invalid syntax
>>> result = 1/3.0
>>> result
0.3333333333333333
>>> repr('chai')
"'chai'"
>>> srt('chai')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'srt' is not defined. Did you mean: 'set'?
>>> str('chai')
'chai'
>>> print('chai')
chai
>>> clear
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'clear' is not defined
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>>
>>> 1 < 2
True
>>> 1 > 2
False
>>> 5.0 == 2.0
False
>>> 5.0 === 5
  File "<stdin>", line 1
    5.0 === 5
          ^
SyntaxError: invalid syntax
>>> 4.0 != 5.0
True
>>> x <y < z
True
>>> x < y and y < z
True
>>> x > y or y < z
True
>>> x > y and y < z 
False
>>> 1 == 2 < 3
False
>>> import math
>>> math.floor(3.5)
3
>>> math.floor(-3.5) 
-4
>>> math.floor(3.6)  
3
>>> math.trunc(2.8) 
2
>>> math.trunc(-2.8) 
-2
>>> 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 +1
1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
>>> 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 * 2.1
2.1000000000000002e+100
>>> 2 ** 200 
1606938044258990275541962092341162602522202993782792835301376
>>> D
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'D' is not defined
>>> 2 + 1j
(2+1j)
>>> 2 + 1j * 3
(2+3j)
>>> (2 + 1j) * 3 
(6+3j)
>>> 0o20
16
>>> 0xff
255
>>> 0b1000
8
>>> oct(64)
'0o100'
>>> hex(64)
'0x40'
>>> bin(64)
'0b1000000'
>>> int(3.14)
3
>>> int('64,8') 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '64,8'
>>> int('64, 8') 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '64, 8'
>>> int('64', 8) 
52
>>> int('64', 16) 
100
>>> int('100', 2) 
4
>>> x = 1
>>> x << 2
4
>>> import random
>>> random.random()
0.5208863217064497
>>> random.random()
0.45902043470302545
>>> random.random()
0.6402220560739199
>>> random.randomint(1, 10) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'random' has no attribute 'randomint'. Did you mean: 'randint'?
>>> random.randint(1, 10)   
5
>>> random.randint(1, 10)
2
>>> random.randint(1, 10)
7
>>> l1 = ['lemon', 'masala', 'ginger']
>>> random.choice(l1)
'masala'
>>> random.choice(l1)
'ginger'
>>> random.choice(l1)
'masala'
>>> random.choice(l1)
'lemon'
>>> random.choice(l1)
'masala'
>>> random.shuffle(l1)
>>> l1
['masala', 'ginger', 'lemon']
>>> l1
['masala', 'ginger', 'lemon']
>>> l1
['masala', 'ginger', 'lemon']
>>> l1
['masala', 'ginger', 'lemon']
>>> 0.1 + 0.1 + 0.4
0.6000000000000001
>>> 0.1 + 0.1 + 0.1
0.30000000000000004
>>> 0.1 + 0.1 + 0.1 - 0.3
5.551115123125783e-17
>>> (0.1 + 0.1 + 0.1) - 0.3 
5.551115123125783e-17
>>> from decomal import Decimal
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'decomal'
>>> from decimal import Decimal
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
Decimal('0.3')
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - decimal('0.3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'decimal' is not defined. Did you mean: 'Decimal'? Or did you forget to import 'decimal'?
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3') 
Decimal('0.0')
>>> from fractions import Fraction
>>> myFra = Fraction(2, 4)
>>> myFra
Fraction(1, 2)
>>> setone = {1, 2, 3, 4} 
>>> setone & {1, 3
... 
... 
KeyboardInterrupt
>>> setone & {1, 3}
{1, 3}
>>> setone | {1, 3, 7} 
{1, 2, 3, 4, 7}
>>> setone - {1, 3, 7} 
{2, 4}
>>> setpne
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'setpne' is not defined. Did you mean: 'setone'?
>>> setone
{1, 2, 3, 4}
>>> setone - {1, 2, 3, 4}
set()
>>> type({})
<class 'dict'>
>>> type(True)
<class 'bool'>
>>> True == 1
True
>>> False == 0
True
>>> True is 1
<stdin>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
False
>>> True
True
>>> True + 4
5
>>>


String in terminal
SKY Computer@JAYMAHAKAL MINGW64 /d/python (main)
$ python
Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> chai = "Lemon Chai"
>>> chai
'Lemon Chai'
>>> print(chai)
Lemon Chai
>>> chai = "Masala chai"
>>> first_char = chai[0]
>>> print(first_char)
M   
>>> chai
'Masala chai'
>>> sllice_chai = chai[0:6] 
>>> print(slice_chai)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'slice_chai' is not defined. Did you mean: 'sllice_chai'?
>>> print(sllice_chai)
Masala
>>> chai[0:6]
'Masala'
>>> num_list = "0123456789"
>>> num_list[:]
'0123456789'
>>> num_list[3:]
'3456789'
>>> num_list[:7]
'0123456'
>>> num_list[0:7:2] 
'0246'
>>> num_list[0:7:3] 
'036'
>>> num_list[0:7:4] 
'04'
>>> num_list[0:7:-4] 
''
>>> num_list[0:9:-4] 
''
>>> num_list[0:9:4]  
'048'
>>> chai
'Masala chai'
>>> print(chai.lower()) 
masala chai
>>> print(chai.upper()) 
MASALA CHAI
>>> chai
'Masala chai'
>>> chai = "  Masala Chai   " 
>>> chai
'  Masala Chai   '
>>> print(chai.strip())
Masala Chai
>>> chai = "Lemon Chai"
>>> print(chai.replace("Lemon", "Ginger"))
Ginger Chai
>>> chai
'Lemon Chai'
>>> chai = "Lemon, Ginger, Masala, Mint"
>>> print(chai.split()) 
['Lemon,', 'Ginger,', 'Masala,', 'Mint']
>>> print(chai.split(", ")) 
['Lemon', 'Ginger', 'Masala', 'Mint']
>>> chai = "Masala Chai"
>>> print(chai.find("chai")) 
-1
>>> print(chai.find("Chai") 
... 
... 
KeyboardInterrupt
>>>
>>> print(chai.find("Chai"))
7
>>> print(chai.find("Chai"))
7
>>> chai = "Masala Chai Chai Chai"
>>> print(chai.count("Chai"))
3
>>> chai_type = "Masala"
>>> quantity = 2
>>> order = "I ordere {} cups of {} chai"
>>> order
'I ordere {} cups of {} chai'
>>> print(order.format(quantity, chai_type)) 
I ordere 2 cups of Masala chai
>>> chai_variety = ["Lemon", "masala", "Ginger"}
  File "<stdin>", line 1
    chai_variety = ["Lemon", "masala", "Ginger"}
                                               ^
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> chai_variety = ["Lemon", "masala", "Ginger"]
>>> chai_variety
['Lemon', 'masala', 'Ginger']
>>> print("".join(chai_variety)) 
LemonmasalaGinger
>>> print(" ".join(chai_variety)) 
Lemon masala Ginger
>>> print("-".join(chai_variety)) 
Lemon-masala-Ginger
>>> print(", ".join(chai_variety)) 
Lemon, masala, Ginger
>>> chai
'Masala Chai Chai Chai'
>>> chai ="Masala Chai"
>>> print(len(chai)) 
11
>>> chai
'Masala Chai'
>>> for letter in chai:
...     print(letter)
... 
M
a
s
a
l
a

C
h
a
i
>>> chai = "He said, \"Masala chai is awesome\" " 
>>> chai
'He said, "Masala chai is awesome" '
>>> chai = "Masala \n chai"
>>> print(chai)
Masala 
 chai
>>> chai = r"Masla\nchai" 
>>> print(chai)
Masla\nchai
>>> chai = r"c:\user\pwd\" 
  File "<stdin>", line 1
    chai = r"c:\user\pwd\"
           ^
SyntaxError: unterminated string literal (detected at line 1)
>>> chai = r"c:\\user\\pwd\\" 
>>> print(chai)              
c:\\user\\pwd\\
>>> chai = r"c:\user\pwd"     
>>> print(chai)
c:\user\pwd
>>> chai = "c:\user\pwd"  
  File "<stdin>", line 1
    chai = "c:\user\pwd"
           ^^^^^^^^^^^^^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
>>> chai = "c:\\user\\pwd" 
>>> print(chai)
c:\user\pwd
>>> chai
'c:\\user\\pwd'
>>> chai = "Masala chai"
>>> print("Masala" in chai) 
True
>>> print("Masalaa" in chai) 
False
>>>


list in terminal


SKY Computer@JAYMAHAKAL MINGW64 /d/python (main)
$ python
Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> tea_variety = ["Black", "Green", "Oolong", "White"] 
>>> tea_variety
['Black', 'Green', 'Oolong', 'White']
>>> print(tea_variety) 
['Black', 'Green', 'Oolong', 'White']
>>> print(tea_variety[1]) 
Green
>>> print(tea_variety[-1]) 
White
>>> print(tea_variety[1:3]) 
['Green', 'Oolong']
>>> print(tea_variety[:2])  
['Black', 'Green']
>>> print(tea_variety[2:])  
['Oolong', 'White']
>>> tea_variety[3]            
'White'
>>> tea_variety[3]= "Herbal"
>>> print(tea_variety)      
['Black', 'Green', 'Oolong', 'Herbal']
>>> tea_variety[1:2]
['Green']
>>> tea_variety[1:2] = "Lemon"
>>> tea_variety
['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']
>>> tea_variety = ["Black", "Green", "Oolong", "White"]
>>> tea_variety
['Black', 'Green', 'Oolong', 'White']
>>> tea_variety[1:2]
['Green']
>>> tea_variety[1:2] = ["Lemon"]
>>> tea_variety
['Black', 'Lemon', 'Oolong', 'White']
>>> tea_variety[1:3]
['Lemon', 'Oolong']
>>> tea_variety[1:3] = ["green", "Masala"]
>>> tea_variety
['Black', 'green', 'Masala', 'White']
>>> tea_variety
['Black', 'green', 'Masala', 'White']
>>> tea_variety[1:1]
[]
>>> tea_variety[1:1] = ["test","test"]
>>> tea_variety
['Black', 'test', 'test', 'green', 'Masala', 'White']
>>> tea_variety[1:2]
['test']
>>> tea_variety[1:3]
['test', 'test']
>>> tea_variety[1:3] = []
>>> tea_variety
['Black', 'green', 'Masala', 'White']
>>> ^Z


SKY Computer@JAYMAHAKAL MINGW64 /d/python (main)
$ python
Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> tea_variety
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tea_variety' is not defined
>>> tea_variety = ["black", "green", "Masala", "White"]
>>> tea_variety
['black', 'green', 'Masala', 'White']
>>> for tea in tea_variety:
... 
  File "<stdin>", line 2

    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for tea in tea_variety:
...     print(tea)
... 
black
green
Masala
White
>>> for tea in tea_variety:
...     print(tea, end="-") 
... 
black-green-Masala-White->>> 
>>> tea_variety
['black', 'green', 'Masala', 'White']
>>> if "Oolong" in tea_variety
  File "<stdin>", line 1
    if "Oolong" in tea_variety
                              ^
SyntaxError: expected ':'
>>> if "Oolong" in tea_variety:
...     print("I have Oolong tea")
... 
>>> tea_variety.append("Oolong")   
>>> tea_variety                    
['black', 'green', 'Masala', 'White', 'Oolong']
>>> if "Oolong" in tea_variety
  File "<stdin>", line 1
    if "Oolong" in tea_variety
                              ^
SyntaxError: expected ':'
>>> if "Oolong" in tea_variety:
...     print("I have Olong Tea")
... 
I have Olong Tea
>>> tea_variety                   
['black', 'green', 'Masala', 'White', 'Oolong']
>>> tea_variety.pop()
'Oolong'
>>> tea_variety       
['black', 'green', 'Masala', 'White']
>>> tea_variety.pop(1:3) 
  File "<stdin>", line 1
    tea_variety.pop(1:3)
                     ^
SyntaxError: invalid syntax
>>> tea_variety.remove("green")
>>> tea_variety
['black', 'Masala', 'White']
>>> tea_variety.insert(1, "green")
>>> tea_variety
['black', 'green', 'Masala', 'White']
>>> tea_variety_copy = tea_variety.copy()
>>> tea_variety_copy
['black', 'green', 'Masala', 'White']
>>> tea_variety_copy.append("Lemon")
>>> tea_variety_copy
['black', 'green', 'Masala', 'White', 'Lemon']
>>> tea_variety     
['black', 'green', 'Masala', 'White']
>>> squared_nums = [x**2 for x in range(10)]
>>> range(10)
range(0, 10)
>>> print(range(10))
range(0, 10)
>>> y = range(10)
>>> y
range(0, 10)
>>> squared_nums = [x**2 for x in range(10)]
>>> square_nums
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'square_nums' is not defined. Did you mean: 'squared_nums'?
>>>
>>> yes
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'yes' is not defined
>>> square_nums
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'square_nums' is not defined. Did you mean: 'squared_nums'?
>>> squared_nums
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cube_num = [y**3 for y in range(5)]
>>> cube_num
[0, 1, 8, 27, 64]
>>>

dictoniry in terminal


SKY Computer@JAYMAHAKAL MINGW64 /d/python (main)
$ python
Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green":"Mild"}} 
  File "<stdin>", line 1
    chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green":"Mild"}}
                                                                       ^
SyntaxError: unmatched '}'
>>> chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green":"Mild"} 
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types["Green"]
'Mild'
>>> chai_types.get("Ginger")
'Zesty'
>>> chai_types               
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types["Green"] = "Fresh"
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> for chai in chai_types:
...     print(chai)
... 
Masala
Ginger
Green 
>>> for chai in chai_types:
...     print(chai, chai_types[chai])
... 
Masala Spicy
Ginger Zesty
Green Fresh 
>>> for key, values  in chai_types.items():
...     print(key, value)
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'value' is not defined. Did you mean: 'values'?
>>> for key, value  in chai_types.items():  
...     print(key, value)
... 
Masala Spicy
Ginger Zesty
Green Fresh
>>> if "Masala" in chai_types:
...     print("I have masala chai")
... 
I have masala chai
>>> print(len(chai_types))
3
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> chai_types["Earl Grey"] = "Citrus"
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
>>> chai_types.pop("Ginger") 
'Zesty'
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
>>> chai_types.popitem()              
('Earl Grey', 'Citrus')
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Fresh'}
>>> del chai_types["Green"]
>>> chai_types
{'Masala': 'Spicy'}
>>> chai_types_copy = chai_types.copy() 
>>> tea_shop = {
... "chai": {"Masla": "Spicy", "Ginger": "Zesty"}, 
... "tea": {"Green":"MIld", "Black":"Strong}
  File "<stdin>", line 3
    "tea": {"Green":"MIld", "Black":"Strong}
                                    ^
SyntaxError: unterminated string literal (detected at line 3)
>>> "tea": {"Green":"MIld", "Black": "Strong} 
  File "<stdin>", line 1
    "tea": {"Green":"MIld", "Black": "Strong}
                                     ^
SyntaxError: unterminated string literal (detected at line 1)
>>> "tea": {"Green":"MIld", "Black": "Strong"} 
  File "<stdin>", line 1
    "tea": {"Green":"MIld", "Black": "Strong"}
    ^^^^^
SyntaxError: illegal target for annotation
>>> "tea": {"Green":"MIld", "Black": "Strong"} 
  File "<stdin>", line 1
    "tea": {"Green":"MIld", "Black": "Strong"}
    ^^^^^
SyntaxError: illegal target for annotation
>>>  tea_shop = {
  File "<stdin>", line 1
    tea_shop = {
IndentationError: unexpected indent
>>> ... "chai": {"Masla": "Spicy", "Ginger": "Zesty"},
  File "<stdin>", line 1
    ... "chai": {"Masla": "Spicy", "Ginger": "Zesty"},
        ^^^^^^
SyntaxError: invalid syntax
>>> ... "tea": {"Green":"MIld", "Black":"Strong}
  File "<stdin>", line 1
    ... "tea": {"Green":"MIld", "Black":"Strong}
        ^^^^^
SyntaxError: invalid syntax
>>> ... "tea" : {"Green":"MIld", "Black":"Strong} 
  File "<stdin>", line 1
    ... "tea" : {"Green":"MIld", "Black":"Strong}
        ^^^^^
SyntaxError: invalid syntax
>>> ... "chai": {"Masla": "Spicy", "Ginger": "Zesty"}, 
  File "<stdin>", line 1
    ... "chai": {"Masla": "Spicy", "Ginger": "Zesty"},
        ^^^^^^
SyntaxError: invalid syntax
>>> tea_shop = {
... "chai": {"Masla": "Spicy", "Ginger": "Zesty"},
... "Tea": {"Green": "Mild", "Black": "Strong"}
... }
>>> tea_shop    
{'chai': {'Masla': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
>>> print(tea_shop)
{'chai': {'Masla': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
>>> tea_shop["chai"] 
{'Masla': 'Spicy', 'Ginger': 'Zesty'}
>>> tea_shop["chai"]["Giger"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Giger'
>>> tea_shop["chai"]["Ginger"] 
'Zesty'
>>> squared_nums = {x:x**2 for x in range(6)} 
>>> print(square_nums)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'square_nums' is not defined. Did you mean: 'squared_nums'?
>>> print(squared_nums) 
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> squared_nums.clear()                     
>>> squared_nums        
{}
>>> keys = ["masla", "Ginger", "LEmon"]
>>> keys
['masla', 'Ginger', 'LEmon']
>>> default_vlaue = "Delicious"
>>> new_dict = dict.fromkeys(keys, default_vlaue)
>>> new_dict
{'masla': 'Delicious', 'Ginger': 'Delicious', 'LEmon': 'Delicious'}
>>> new_dict = dict,fromkeys(keys, keys)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fromkeys' is not defined
>>> new_dict = dict.fromkeys(keys, keys) 
>>> new_dict
{'masla': ['masla', 'Ginger', 'LEmon'], 'Ginger': ['masla', 'Ginger', 'LEmon'], 'LEmon': ['masla', 'Ginger', 'LEmon']}