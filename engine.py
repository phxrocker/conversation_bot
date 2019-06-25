name = input('What is your name? ' )
color = input('\nHi ' + name + "! What's your favorite color? ")

# Color Condition
while color == 'blue':
    print('\n' + color + "?! That's awesome " + name + "!! Blue's my favorite color too!!")
    break
else:
    print('\n' + color + "'s ok... i guess ")

eye_color = input('\nWhat color are your eyes? ')

# Eye Color Condition
while eye_color != color:
    print('\nNo way,' + name + '! I would think that ' + eye_color + ' would be your favorite color then!')
    break
else:
    print('\nFigures')

car_check = input('\nDo you have a car, yes or no? ')

# Did the user have a car
while car_check == 'yes':
    car_color = input('\nWell good for you.  What color is it? ')
else:
    print("\nThat's ok, " + name + ".  We'll skip that one for now")

input()