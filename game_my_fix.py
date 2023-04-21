from random import randint, choice
from objects import *
from classes import bordered

team_1 = list_teams[0]
team_2 = list_teams[1]

dead_team_1 = []
dead_team_2 = []

while len(dead_team_1) < 5 and len(dead_team_2) < 5:
    '''randint'''
    # res_1 = team_1[randint(0, len(team_1) - 1)]
    # res_2 = team_2[randint(0, len(team_2) - 1)]
    # '''randrange'''
    # res_1 = team_1[randrange(len(team_1))]
    # res_2 = team_2[randrange(len(team_2))]
    '''choice'''
    res_1 = choice(team_1)
    res_2 = choice(team_2)

    final_res = randint(1, 2)

    if final_res == 1:
        if hasattr(res_2, 'perk'):
            if res_2.perk == 1:
                res_2.mask()
                # res_2.perk = randint(1, 2)
            else:
                res_1.attack(res_2)
                if res_2.health <= 0:
                    dead_team_2.append(res_2)
                    team_2.remove(res_2)
                    print(bordered(f'{res_2.model} убит.\nЭто уже {len(dead_team_2)} погибший из 2ой команды'))
        #  ЗДЕСЬ ГЛЯНЬ , АРТЕ ДОБАВИЛ КРИТИЧЕСКИЙ, ХЗ РАБОТАЕТ ИЛИ НЕТ
        elif hasattr(res_1, 'crit'):
            if res_1.crit == 1:
                res_1.critical_damage(res_2)
                print(f'\n{res_2.model} СЛОВИЛ КРИТИЧЕСКИЙ УРОН!!!\n')
                if res_2.health <= 0:
                    dead_team_2.append(res_2)
                    team_2.remove(res_2)
                    print(bordered(f'{res_2.model} убит.\nЭто уже {len(dead_team_2)} погибший из 2ой команды'))
            else:
                res_2.attack(res_1)
                if res_2.health <= 0:
                    dead_team_2.append(res_2)
                    team_2.remove(res_2)
                    print(bordered(f'{res_2.model} убит.\nЭто уже {len(dead_team_2)} погибший из 2ой команды'))
        else:
            res_1.attack(res_2)
            if res_2.health <= 0:
                dead_team_2.append(res_2)
                team_2.remove(res_2)
                print(bordered(f'{res_2.model} убит.\nЭто уже {len(dead_team_2)} погибший из 2ой команды'))

    else:
        if hasattr(res_1, 'perk'):
            if res_1.perk == 1:
                res_1.mask()
                # res_1.perk = randint(1, 2)
            else:
                res_2.attack(res_1)
                if res_1.health <= 0:
                    dead_team_1.append(res_1)
                    team_1.remove(res_1)
                    print(bordered(f'{res_1.model} убит.\nЭто уже {len(dead_team_1)} погибший из 1ой команды'))
        elif hasattr(res_2, 'crit'):
            if res_2.crit == 1:
                res_2.critical_damage(res_1)
                print(f'\n{res_1.model} СЛОВИЛ КРИТИЧЕСКИЙ УРОН!!!\n')
                if res_1.health <= 0:
                    dead_team_1.append(res_1)
                    team_1.remove(res_1)
                    print(bordered(f'{res_1.model} убит.\nЭто уже {len(dead_team_1)} погибший из 2ой команды'))
        else:
            res_2.attack(res_1)
            if res_1.health <= 0:
                dead_team_1.append(res_1)
                team_1.remove(res_1)
                print(bordered(f'{res_1.model} убит.\nЭто уже {len(dead_team_1)} погибший из 1ой команды'))

if len(dead_team_1) == 5:
    print('Команда 2 победила!')
elif len(dead_team_2) == 5:
    print('Команда 1 победила!')