pl=''
def player_add ():
    global pl
    pl=input('Имя игрока?')
    player_add=open(pl+'.txt','a')
    player_add.write('0'+'\n')
    player_add.close()
    print('pl add',pl)
def score_drop ():
    score_drop=open(pl+'.txt','a')
    score_drop.write('-100'+'\n')
    score_drop.close()
    print('pl drop',pl)
    menu()
def score_read ():
    score_read=open(pl+'.txt','r')
    score_all=[line.strip() for line in score_read]
    score_total=sum(int(i) for i in score_all)
    print('Ваши очки: ', score_total)
    print('pl read',pl)
    score_read.close()
    menu()
def menu():
    while True:
        print('pl menu',pl)  
        st=input('очки [o], отнять очки [q], изменить игрока[p]')
        if st=='q':
            score_drop()
        if st=='o':
            score_read()
        if st=='p':
            player_add()
        else:
            break
player_add()
menu()
