from dicerolls import diceroll
class battle:
    def attack(self,armourclass,attacker,defender,weapon):
        d = diceroll()
        rollforhit = d.rolladice(20)
        print(attacker + ' rolls a ' + str(rollforhit))
        if rollforhit == 20:
            print('Nat20 rolled! Double Damage!')
        if int(rollforhit) > armourclass:
            print(attacker + ' hits, now rolling a d12')
            rollfordamage=int(d.rolladice(12))
            print(attacker + ' rolls a ' + str(rollfordamage))
            if rollforhit == 20:
                rollfordamage = rollfordamage * 2
            damage = rollfordamage + weapon
            print(attacker + ' hits for ' + str(damage))
            return damage

        else:
            print('it misses')
            return 0