def bordered(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)


class Tank():

    def __init__(self, health, model, damage, armor):
        self.health = health
        self.model = model
        self.damage = damage
        self.armor = armor

    def attack(self, enemy):
        enemy.armor -= self.damage
        if enemy.armor < 0:
            enemy.health += enemy.armor
            if enemy.health < 0:
                enemy.health = 0
                enemy.armor = 0
        print(self.model, 'атакует', enemy.model, '\n')
        # sleep(0.1)
        print(f'Текущая броня {enemy.model} - {enemy.armor} ед.')
        # sleep(0.1)
        print(f'Текущее здоровье {enemy.model} - {enemy.health} hp.')
        # sleep(0.1)

    def print_info(self):
        print('Модель:', self.model)
        print('Здоровье:', self.health)
        print('Дамаг:', self.damage)
        print('Броня:', self.armor)

    def armor_active(self):
        print('Не пробил!')


class EasyTank(Tank):
    def __init__(self, health, model, damage, armor, perk):
        super().__init__(health, model, damage, armor)
        self.perk = perk

    def mask(self):
        print(bordered(f'{self.model} не видно. Нельзя атаковать.'))


class MediumTank(Tank):
    def __init__(self, health, model, damage, armor, perk):
        super().__init__(health, model, damage, armor)
        self.perk = perk

    def mask(self):
        print(bordered(f'{self.model} не видно. Нельзя атаковать.'))


class HeavyTank(Tank):
    pass
    # def __init__(self, health, model, damage, armor):
    #     super().__init__(health, model, damage, armor)


class Artillery(Tank):
    def __init__(self, health, model, damage, crit, armor=0):
        super().__init__(health, model, damage, armor)
        self.crit = crit

    def critical_damage(self, enemy):
        enemy.armor -= self.damage * 2
        if enemy.armor < 0:
            enemy.health += enemy.armor
            if enemy.health < 0:
                enemy.health = 0
                enemy.armor = 0
        print(self.model, 'атакует', enemy.model, '\n')
        # sleep(0.1)

        print(f'Текущая броня {enemy.model} - {enemy.armor} ед.')
        # sleep(0.1)
        print(f'Текущее здоровье {enemy.model} - {enemy.health} hp.')
        # sleep(0.1)