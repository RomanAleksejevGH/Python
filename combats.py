import random
player = {
    'bonus_stats': 0,
    'level': 1,
    'expirience': 0,
    'health': 100,
    'damage': 10,
    'crit': 0,
    'dodge': 0,
    'deffence': 0,
    'strength': 10,
    'agility': 10,
    'vitality': 10,
    'luck': 10}


class Fighter:

    level = expirience = health = damage = crit = dodge = deffence = strength = agility = vitality = luck = 0

    def __init__(self, level, expirience, health, damage, crit, dodge, deffence, strength, agility, vitality, luck):
        self.level = level
        self.expirience = expirience
        self.health = health
        self.damage = damage
        self.crit = crit
        self.dodge = dodge
        self.deffence = deffence
        self.strength = strength
        self.agility = agility
        self.vitality = vitality
        self.luck = luck
        self.damage_total = self.damage + self.strength
        self.crit_total = self.crit + self.luck
        self.deffence_total = self.deffence + self.agility
        self.dodge_total = self.dodge+self.agility/2+self.luck/2
        self.health_total = self.health+self.vitality*5


newFighter = Fighter(player['level'], player['expirience'], player['health'], player['damage'], player['crit'],
                     player['dodge'], player['deffence'], player['strength'], player['agility'], player['vitality'], player['luck'])

newBotFighter = Fighter(player['level'], player['expirience'], player['health'], player['damage'], player['crit'],
                        player['dodge'], player['deffence'], player['strength'], player['agility'], player['vitality'], player['luck'])


def Hit(fighter_dodge, fighter_crit, fighter_deffence, fighter_damage, who):
    who_hit = who
    dodge = float(fighter_dodge)
    dodge_random = random.uniform(0, 100)
    crit = float(fighter_crit)
    crit_random = random.uniform(0, 100)
    dmg_done = float(fighter_damage-fighter_deffence/2)
    if dodge < dodge_random:
        if crit < crit_random:
            print('на ', dmg_done)
            if who_hit == 'player':
                newBotFighter.health_total = newBotFighter.health_total-dmg_done
            elif who_hit == 'bot':
                newFighter.health_total = newFighter.health_total-dmg_done
        elif crit > crit_random:
            dmg_done = dmg_done*2
            print('на ', dmg_done, 'Критический урон!')
            if who_hit == 'player':
                newBotFighter.health_total = newBotFighter.health_total-dmg_done
            elif who_hit == 'bot':
                newFighter.health_total = newFighter.health_total-dmg_done
    elif dodge > dodge_random:
        if who_hit == 'bot':
            print('Вы в последний момент увернулись от атаки противника!')
        elif who_hit == 'player':
            print('Противник в последний момент увернулся от вашей атаки!')


def block_atk():
    while True:
        where = {'1': 'в голову', '2': 'в корпус',
                 '3': 'в пах', '4': 'по ногам'}
        get_block = input('Выберите блок:\n'
                          'Блок головы - 1     Блок корпуса - 2\n'
                          'Блок паха - 3       Блок ног - 4\n')
        get_atk = input('Выберите удар:\n'
                         'В голову - 1     В корпус - 2\n'
                          'В пах - 3        По ногам - 4\n')
        bot_block = str(random.randint(1, 4))
        bot_atk = str(random.randint(1, 4))
        if get_block == bot_atk:
            print('Вы заблокировали удар в ', where[get_block])
        elif get_block != bot_atk:
            print('Противник ударил вас ', where[bot_atk])
            Hit(newFighter.dodge_total, newBotFighter.crit_total, newFighter.deffence_total,
                    newBotFighter.damage_total, 'bot')
        if get_atk == bot_block:
            print('Противник заблокировал вашу атаку ', where[get_atk])
        elif get_atk != bot_block:
            print('Вы ударили противника ', where[get_atk])
            Hit(newBotFighter.dodge_total, newFighter.crit_total, newBotFighter.deffence_total,
                    newFighter.damage_total, 'player')
            print('Ваше здоровье: ', newFighter.health_total,
                  '     Здоровье противника: ', newBotFighter.health_total, '\n')
        if newFighter.health_total == 0:
            print('Вы пали в бою ...')
            break
        elif newBotFighter.health_total == 0:
            print('Победа!')
            break


def tavern():
    print('Вы чувствуете как ваши силы возвращаются...')
    newFighter.health_total = player['health']+newFighter.vitality*5


def menu():
    while True:
        print('Ваше здоровье: ', newFighter.health_total, '\n')
        flag = input('Выбирите направление:\n'
                     'Таверна - 1     Арена - 2\n')
        if flag == '1':
            tavern()
        elif flag == '2':
            block_atk()


menu()
