import random
class diceroll:
    def __init__(self) -> None:
        pass
    def rolladice (self, dicetype):
        self.dicetype = dicetype
        result = random.randint(1, dicetype)
        return (result)




