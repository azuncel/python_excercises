#ADD
add = lambda input1: input1 + 10
print(add(3))

#Check in string
my_string = lambda string1: string1 in "Hola mundo, hola Azu"
print(my_string('Azu'))
print(my_string(','))
print(my_string('Az'))
print(my_string('Dia'))

#Different inputs
check_input = lambda input_var: 'Mayor a 10' if input_var >= 10 else 'Menor a 10'
print(check_input(10))
print(check_input(7))

#Short string
short_string = lambda word: len(word) < 10
print(short_string("fanta"))
print(short_string("supercalifrajilisticoespiralidoso"))

#Ends
ends = lambda word: "a" in word[-1]
print(ends('Diana'))
print(ends('Carlos'))

#Even Odd
number = lambda num: " Is even" if num%2 == 0 else "Is odd"
print(number(10))
print(number(13))

#Random
import random
num_random = lambda num: num + random.randint(1,10)
print(num_random(5))

