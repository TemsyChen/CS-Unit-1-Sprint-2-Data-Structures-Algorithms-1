'''
Given an integer, write a function that reverses 
the bits (in binary) and returns the integer result.

Understand:
417 --> 267
167 --> 417
0 --> 0

Plan:
Use bin() to convert the binary into a string. 
Use bracket indexing to reverse the order. 
Use int() to convert it into a decimal number.
'''

def csReverseIntegerBits(n):
    str_n = bin(n).replace("0b","")
    rev_str_n = str_n[::-1]
    int_n = int(rev_str_n, 2)
    return int_n

#Author's Answer
def csReverseIntegerBits(n):
    return int(bin(n)[:1:-1],2)

'''
Given a binary string (ASCII encoded), write a function 
that returns the equivalent decoded text.

Every eight bits in the binary string represents one 
character on the ASCII table.

Understand:
csBinaryToASCII("011011000110000101101101011000100110010001100001") -> "lambda"
"" --> ""

Plan:
Split the string into a list of every 8 digits. 
Convert each 8 digit into its ASCII character. 
Join the string.
'''

def csBinaryToASCII(binary):
    str_list = []
    for i in range(0, len(binary), 8):
        str_list.append(int(binary[i:i+8], 2))
    chr_binary = []
    for str_ in str_list:
        chr_binary.append(chr(str_))
    return "".join(chr_binary)
    
#Author's Answer
def csBinaryToASCII(binary):
    return "".join( [ chr(int(binary[i: i+8], 2)) for i in range(0, len(binary), 8) ] )

'''
Given a number, write a function that converts 
that number into a string that contains "raindrop sounds" 
corresponding to certain potential factors. A factor 
is a number that evenly divides into another number, 
leaving no remainder. The simplest way to test if one 
number is a factor of another is to use the modulo operator.

Here are the rules for csRaindrop. If the input number:

has 3 as a factor, add "Pling" to the result.
has 5 as a factor, add "Plang" to the result.
has 7 as a factor, add "Plong" to the result.
does not have any of 3, 5, or 7 as a factor, the result 
should be the digits of the input number.

Understand:
28 --> "Plong"
30 --> "PlingPlang"
34 --> "34"

Plan:
Using if statements, check if the number has a factor 
of 3, 5, or 7. If so, append an empty string with Pling, 
Plang, or Plong. Else, return the number as the string.
'''

def csRaindrops(number):
    result = ""
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    if result == "":
        result += str(number)
    return result

#Author's Answer
def csRaindrops(number):
    result = ''
    result += "Pling" * (number % 3 == 0)
    result += "Plang" * (number % 5 == 0)
    result += "Plong" * (number % 7 == 0)

    return result or str(number)

