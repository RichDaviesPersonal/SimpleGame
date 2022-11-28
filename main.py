from CharacterManagement import CharacterManagement
from dicerolls import diceroll
from battle import battle 
import additionalmaps

name = input('What is your characters name?')
typechosen = False
while typechosen == False or confirmation==False:
    type=input('What is your character type?')
    if type == 'barbarian':
        print('Barbarian: High HP, but low defence')
        typechosen = True
    elif type == 'rogue':
        print('Rogue: Medium HP, high defence')
        typechosen = True
    elif type == 'mage':
        print('Mage: low HP, low defence')
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
print ('Your name is ' + name + ' and your type is ' + type)

c = CharacterManagement()
b = battle()
playerhp, armourclass, weapon = c.CreateACharacter(name, type)
d=diceroll()

beasthp = 10
beastweapon = d.rolladice(6)
beastarmourclass = 13
playerweapon = weapon[1]
print('you walk into the room and are attacked by a beast with a weapon of +' + str(beastweapon))
print('ROLL FOR INITIATIVE!!!')
input('\nPress the enter key to continue.\n')
playerroll=d.rolladice(20)
print(name + ' has rolled a ' + str(playerroll))
beastroll=d.rolladice(20)
print('Beast has rolled a ' + str(beastroll))
if playerroll > beastroll:
    print(name + ' attacks first')
    input('\nPress the enter key to continue.\n')
    damage = b.attack(beastarmourclass,name,'beast',playerweapon)
    beasthp -= int(damage)
    input('\nPress the enter key to continue.\n')
else:
    print('Beast attacks first')
    input('\nPress the enter key to continue.\n')
while playerhp > 0 and beasthp > 0:
    damage = b.attack(armourclass,'Beast',name,beastweapon)
    playerhp -= int(damage)
    input('\nPress the enter key to continue.\n')
    damage = b.attack(beastarmourclass,name,'beast',playerweapon)
    beasthp -= int(damage)
    input('\nPress the enter key to continue.\n')
nextstep='you continue on, well done' if playerhp >0 else 'Game Over'
print (nextstep)
a = additionalmaps
print ('Which Direction do you want to head next?')
for key, value in a.map1.items():
    print (key, value)



