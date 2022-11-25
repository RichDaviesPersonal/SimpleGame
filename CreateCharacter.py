class CreateCharacter:
    def __init__ (self, name, type):
        self.name = name 
        self.type = type
        print('Hi ' + self.name + '. You are a ' + self.type)
        if self.type == 'barbarian': 
            hp = 10
        else: 
            print ("invalid type")
        print('Your HP starts at ' + str(hp))