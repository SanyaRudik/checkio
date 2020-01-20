class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit, count):
        for i in range(count):
            self.units.append(unit)


class Warrior:
    def __init__(self):
        self.attack = 5
        self.HP = 50
        self.is_alive = True


class Knight(Warrior):
    def __init__(self):
        super(Knight, self).__init__()
        self.attack = 7


def live_warrior(unit_live):
    unit_live.HP = 50
    unit_live.is_alive = True


def fight(unit_1, unit_2):
    first_hit = False
    while (unit_1.HP > 0) and (unit_2.HP > 0):

        if not first_hit:
            unit_2.HP -= unit_1.attack
            first_hit = True
        else:
            unit_1.HP -= unit_2.attack
            first_hit = False
    if unit_2.HP <= 0:
        unit_2.is_alive = False
    if unit_1.HP <= 0:
        unit_1.is_alive = False
    return first_hit


class batlle():

    def fight_a(self, ArmyMy, ArmyEn):
        iE = 0
        iM = 0
        while len(ArmyMy.units) and len(ArmyEn.units):
            fight(ArmyMy.units[iM], ArmyEn.units[iE])
            if not ArmyMy.units[iM].is_alive:
                if iM == len(ArmyMy.units) - 1:
                    return False
                iM += 1
                live_warrior(ArmyMy.units[iM])

            if not ArmyEn.units[iE].is_alive:
                if iE == len(ArmyEn.units) - 1:
                    return True
                iE += 1
                live_warrior(ArmyEn.units[iE])
        return ' No Army '


if __name__ == '__main__':
    # chuck = Warrior()
    # bruce = Knight()
    # carl = Knight()
    # dave = Warrior()
    # mark = Warrior()
    # print(fight(carl, bruce))  # == True
    # print(carl.HP,bruce.HP)

    # print(fight(dave, carl))  # == False
    # print(chuck.is_alive)  # == True
    # print(bruce.is_alive)  # == False
    # print(carl.is_alive)  # == True
    # print(dave.is_alive)  # == False
    # print(fight(carl, mark))  # == False
    # print(carl.is_alive)  # == False
    MyArmy = Army()
    EnemyArmy = Army()
    EnemyArmy.add_units(Knight(), 1)
    EnemyArmy.add_units(Warrior(), 2)

    MyArmy.add_units(Knight(), 3)
    batlle_A = batlle()
    print(batlle_A.fight_a(MyArmy, EnemyArmy))
