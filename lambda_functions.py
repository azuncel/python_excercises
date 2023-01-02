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