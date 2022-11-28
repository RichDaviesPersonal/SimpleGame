class CharacterManagement:
    def __init__(self):
        self.name = NameError
        self.type = type
    def CreateACharacter(self, name, type):
        self.name = name 
        self.type = type
        print('Hi ' + self.name + '. You are a ' + self.type)
        if self.type == 'barbarian': 
            hp = 24
            armourclass=14
            weapon=['Axe',5]
        elif self.type == 'rogue':
            hp = 18
            armourclass=18
            weapon=['Dagger',3]
        elif self.type == 'mage':
            hp = 16
            armourclass=16
            weapon= ['Staff',3]
        else: 
            print ("invalid type")
        print('Your HP starts at ' + str(hp) + '. Your Armour Class is ' + str(armourclass) + '. Your Weapon is a ' + weapon[0] + ', with damage of ' + str(weapon[1]))        
        return (hp, armourclass,weapon)

