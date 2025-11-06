# Instruction:
# As a member of the ones above all you have been tasked with completing the following... tasks.


# Exercise 1:
# Write a function that takes in a string as a parameter and returns a tuple of:
def take_in_string(sentence:str)->tuple:
   sentence=sentence.lower()
   count=0
# 1) A Dictionary that counts how many times a letter in the string appear.
   my_dict=[]
   for char in tuple(sentence):
       if char in set(sentence):
        count+=1
        my_dict.append((char,count))
        
# 2) A list of all the letters that appear in the string.
   my_list=list(set(sentence))
   return (my_dict,my_list)

# Exercise 2:
# Hello there, you are a software engineer right? Rhetorical question.
# You are one of the top coders on campus after all so please help me out here i'm in a bind.
# I was trying to write a function that would decode morse code and return it's string representation 
# however I just can't get it to work. Help me out please.
"""
    Letters
    'A' : '.-',    'B' : '-...',  'C' : '-.-.',  'D' : '-..'
    'E' : '.',     'F' : '..-.',  'G' : '--.',   'H' : '....'
    'I' : '..',    'J' : '.---',  'K' : '-.-',   'L' : '.-..'
    'M' : '--',    'N' : '-.',    'O' : '---',   'P' : '.--.'
    'Q' : '--.-',  'R' : '.-.',   'S' : '...',   'T' : '-'
    'U' : '..-',   'V' : '...-',  'W' : '.--',   'X' : '-..-'
    'Y' : '-.--',  'Z' : '--..',

    Numbers
    '0' : '-----', '1' : '.----', '2' : '..---', '3' : '...--',
    '4' : '....-', '5' : '.....', '6' : '-....', '7' : '--...',
    '8' : '---..', '9' : '----.'

    Special Characters
    ',' : '--..--'
    ':' : '---...'
    "'" : '.----.'
    '.' : '.-.-.-'
    '!' : '-.-.--'
    '?' : '..--..'
    space: ' '

    *Each character is separated by a space.
     Each word is separated by three spaces ( ).
"""


morse_code = ".- .-. -- --- .-. . -..   .. -.   ..-. . .. - .... --..--   ... .... .. . .-.. -.. . -..   -... -.--   -.. . ...- --- - .. --- -. --..--   .- .-. -- . -..   .-- .. - ....   .--. ..- .-. .. - -.--   --- ..-.   .--. ..- .-. .--. --- ... . --..--   - .... .   . -- .--. . .-. --- .-. .----. ...   .-- .. .-.. .-..   -- .- -.. .   -- .- -. .. ..-. . ... - -.-.--   .-- .   .- .-. .   - .... .   .-- .- .-. .-. .. --- .-. ...   --- ..-.   - .... .   --. .-. . -.--   -.- -. .. --. .... - ... --..--   -... ..- --.   .... ..- -. - . .-. ... -.-.--   ..-. --- .-.   .-- .   .- .-. .   -.. . -.-. --- -.. . .-. ... -.-.--"

def decoding_mose_code(code):
    words = code.split(" ")
    words_in_code = len(words)

    for_A = ".-"

    decoded_message = ""

    for i in words:
        if i == for_A:
            decoded_message + i 


    return decoded_message


#print(decoding_mose_code(morse_code)) #Who even uses morse code these days 


# Exercise 3:
# Write a function that takes 2 parameters as lists and returns 
def my_lists(list1,list2:list)->list:
   my_list=set.union(list1,list2)
   return my_list
   
# a new list made up of the original list but with not duplicates.



# Exercise 4:
# Write a funtion that takes a 2D array/matrix as a parameter and prints out the following meta data:
# The number of rows
# The number of elemnts*
# The element that appears the most along with its frequency and it's index in the matrix.



# Exercise 5:
# Write a function that takes an integer as a parameter and prints a right-angled number triangle
def triangle(n:int):
   return 
# where each row contains numbers from 1 up to the row number
if __name__=="__main__":
    print(take_in_string('ABCDEFGHIJ'))
    print(my_lists({1,2,3,4,5},{2,3,4,6,7,8}))