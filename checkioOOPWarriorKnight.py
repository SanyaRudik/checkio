class Warrior:
    attack = 5
    HP = 50
    is_alive = True


class Knight(Warrior):
    attack = 7


def live(unit):
    if unit.HP <= 0:
        unit.is_alive = False


def fight(unit_1, unit_2):
    first_hit = False
    while (unit_1.HP > 0) and (unit_2.HP > 0):

        if not first_hit:
            unit_2.HP -= unit_1.attack
            first_hit = True
        else:
            unit_1.HP -= unit_2.attack
            first_hit = False
        # print(unit_1.HP, unit_2.HP)
        live(unit_1)
        live(unit_2)

    return first_hit


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()

    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    # fight(chuck, bruce)
    print(fight(chuck, bruce))  # == True
    print(fight(dave, carl))  # == False
    print(chuck.is_alive)  # == True
    print(bruce.is_alive)  # == False
    print(carl.is_alive)  # == True
    print(dave.is_alive)  # == False
    print(fight(carl, mark))  # == False
    print(carl.is_alive)  # == False
