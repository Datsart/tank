from classes import EasyTank, MediumTank, HeavyTank, Artillery
from random import randint


def teams(all_tanks):
    team_1 = list()
    team_2 = list()
    while len(team_1) != 5:
        random_tank_1 = all_tanks[randint(0, len(all_tanks) - 1)]
        team_1.append(random_tank_1)
        random_tank_2 = all_tanks[randint(0, len(all_tanks) - 1)]
        team_2.append(random_tank_2)
    return [team_1, team_2]


# Легкие танки   здесь исчезновение
T_100_LT = EasyTank(1500, 'T-100 LT', randint(300, 360), 500, randint(1, 2))
AMX_13_105 = EasyTank(1400, 'AMX 13 105', randint(390, 480), int(1400 / 3), randint(1, 2))
Panzerwagen = EasyTank(1600, 'Panzerwagen', randint(320, 420), 1600 / 3, randint(1, 2))
Manticore = EasyTank(1400, 'Manticore', randint(390, 480), int(1400 / 3), randint(1, 2))
WZ_132_1 = EasyTank(1500, 'WZ 132-1', randint(390, 480), 500, randint(1, 2))

# Средние танки
T_62_A = MediumTank(1950, 'T-62 A', randint(320, 420), int(1950 / 3), randint(1, 2))
E_50 = MediumTank(2050, 'E 50', randint(390, 510), int(2050 / 3), randint(1, 2))
Patton = MediumTank(2000, 'Patton', randint(390, 480), int(2000 / 3), randint(1, 2))
Bat_Chat = MediumTank(1800, 'Bat-Chat', randint(240, 320), 1800 / 3, randint(1, 2))
Progetto = MediumTank(1900, 'Progetto', randint(360, 440), int(1900 / 3), randint(1, 2))

# Тяжелые танки
Maus = HeavyTank(3000, 'Maus', randint(490, 630), 3000 / 3)
IS_7 = HeavyTank(2400, 'IS-7', randint(490, 640), 2400 / 3)
T_57_Heavy = HeavyTank(2250, 'T57 Heavy', randint(400, 515), int(2250 / 3))
WZ_111 = HeavyTank(2200, 'WZ 111', randint(490, 640), int(2200 / 3))
AMX_50_B = HeavyTank(2100, 'AMX 50B', randint(400, 515), 2100 / 3)

# ПТшки     здесь прием крит урона
Grile_15 = Artillery(1800, 'Grile 15', randint(750, 950), 1800 / 3, randint(1, 2))
Object_268 = Artillery(1950, 'Объект 268', randint(750, 1100), int(1950 / 3), randint(1, 2))
T_110_E4 = Artillery(2000, 'T 110 E4', randint(750, 1100), int(2000 / 3), randint(1, 2))
FV_215_B = Artillery(2000, 'FV 215B', randint(1150, 1750), int(2000 / 3), randint(1, 2))
STRV = Artillery(1800, 'STRV', randint(390, 480), 1800 / 3, randint(1, 2))

# САУ       здесь прием крит урона
GWE_100 = Artillery(550, 'GWE 100', randint(640, 900), randint(1, 2))
Object_261 = Artillery(510, 'Объект 261', randint(520, 800), randint(1, 2))
T92 = Artillery(500, 'T 92', randint(750, 1100), randint(1, 2))

# общий список танков
all_tanks = list()
all_tanks.extend([Maus, IS_7, T_57_Heavy, WZ_111, AMX_50_B, Grile_15, Object_268, T_110_E4])
all_tanks.extend([FV_215_B, STRV, GWE_100, Object_261, T92, T_100_LT, AMX_13_105])

list_teams = teams(all_tanks)
