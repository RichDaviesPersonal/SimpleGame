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
            evasion=2
        elif self.type == 'rogue':
            hp = 18
            armourclass=18
        elif self.type == 'mage':
            hp = 16
            armourclass=16
        else: 
            print ("invalid type")
        print('Your HP starts at ' + str(hp) + '. Your Armour Class is ' + str(armourclass))
        return (hp, armourclass)

