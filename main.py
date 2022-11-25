from CreateCharacter import CreateCharacter

name = input('What is your characters name?')
typechosen = False
while typechosen == False or confirmation==False:
    type=input('What is your character type?')
    if type == 'barbarian':
        print('Barbarian: High HP, but low defence')
        typechosen = True
    else:
        print('Sorry, thats an invalid choice')
    confirmation=False if typechosen==True else print('Try again')
    while confirmation == False:
        yesorno= input('do you wish to continue as a '  + type + '? Please enter y or n\n')
        if yesorno == 'y':
            confirmation=True
        else:
            print ('Please choose again')
            confirmation = 'reset'
            typechosen = False
p1 = CreateCharacter(name, type)

