import random
class Hero:
    """ класс герой"""
    def __init__(self,name:str):
        self.Name=name
        self.lvl=0
"""Создание двух героев"""
redHero=Hero('Red')
blueHero=Hero('Blue')

def ARMY_RANGE():
    """Изменение длинны списка солдат и повышение уровня героя"""
    
    RED=[]        #Red army
    BLUE=[]        #Blue army
    R=len(RED)
    B=len(BLUE)
    while R<20 and B<20:
        x=random.randint(1,2)
        if x==1:
            RED.append(x)
            redHero.lvl +=1
            R=len(RED)
        elif x==2:
            BLUE.append(x)
            blueHero.lvl +=1
            B=len(BLUE)
    print("У {} героя {} уровень и {} солдат" .format(
        redHero.Name, redHero.lvl, R))
    print("У {} героя {} уровень и {} солдат" .format(
        blueHero.Name, blueHero.lvl, B))
ARMY_RANGE()
