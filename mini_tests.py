class Fighter:

    level = deffence = 0
    health = 100
    damage = 10
    crit = dodge = float(1.0)
    strength = agility = vitality = luck = 5
    damage_total = damage + strength
    crit_total = crit + luck/2
    dodge_total = dodge + (agility+luck)/2
    health_total = health + vitality
    deffence_total = deffence + agility


class Player(Fighter):
    gold=10
    expirience=0
    
