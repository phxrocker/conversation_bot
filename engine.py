from floyd import floyd

def main():

  name = input('What is your name? ' )
  
  color = input('\nHi ' + name + "! What's your favorite color? ")

  # Color Condition
  if color == 'blue':
      print('\n' + color + "?! That's awesome " + name + "!! Blue's my favorite color too!!")
  else:
      print('\n' + color + "'s ok... i guess ")

  eye_color = input('\nWhat color are your eyes? ')

  # Eye Color Condition
  if eye_color != color:
      print('\nNo way,' + name + '! I would think that ' + eye_color + ' would be your favorite color then!')
  else:
      print('\nFigures')

  car_check = input('\nDo you have a car, yes or no? ')

  # Did the user have a car
  if car_check.startswith('y'):
    car_color = input('\nWell good for you.  What color is it? ')
  else:
    print("\nThat's ok, " + name + ".  We'll skip that one for now\n")
     
  # Car Color Condition
  if car_color == color:
    print('\nOf course it is\n')
  else:
    print('\nuh...ok\n')
  
  # Offer a game
  game_check = input('\nWould you like to play a game?\n')
  
  # Yes
  if game_check.startswith('y'):
    floyd()
  else:
    return


while True:
    main()
