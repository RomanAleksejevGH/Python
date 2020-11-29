import random
pl=''
def player_add ():
    global pl
    pl=input('Имя игрока?')
    player_add=open(pl+'.txt', 'a')
    player_add.write('0'+'\n')
    player_add.close()
def score_drop ():
    score_drop=open(pl+'.txt', 'a')
    score_drop.write('-100'+'\n')
    score_drop.close()
    menu()
def score_add ():
    score_add=open(pl+'.txt', 'a')
    score_add.write('100'+'\n')
    score_add.close()
    menu()
def score_resset ():
    score_resset=open(pl+'.txt', 'w')
    score_resset.write('0'+'\n')
    score_resset.close()
    menu()
def score_read ():
    score_read=open(pl+'.txt', 'r')
    score_all=[line.strip() for line in score_read]
    score_total=sum(int(i) for i in score_all)
    print('Ваши очки: ', score_total)
    score_read.close()
    
def get_question ():
    with open('questions.txt','r',encoding='utf8')as f:
        question_list=f.read().splitlines()
    number_question=random.randrange(0,len(question_list))
    question_answer=str(question_list[number_question])
    for i in range(0,len(question_answer)):
        if question_answer[i]==';':
            question=question_answer[0:i]
            answer=question_answer[i+1:len(question_answer)]
    return answer,question
def game():
    at=0
    answer,question=get_question()
    print(question)
    curent_view=[]
    for i in range(0,len(answer)):
        curent_view.append('*')
    print(''.join(curent_view))  
    while True:
        try:
            user=input('Введите букву или назовите слово')
            if user==answer:
                print('Вы правильно назвали слово!')
                score_add()
                break
            if (user in answer):
                print('Есть такая буква!')
                for i in range(0,len(answer)):
                    if answer[i]==user:
                        curent_view[i]=user
                        user_answer=''.join(curent_view)
                if user_answer==answer:
                    print('Вы правильно назвали слово!')
                    score_add()
                    break
            else:
                print('Нет какой буквы!')
                at=at+1
                if at==5:
                    print('У вас кончились попытки, попробуйте еще раз!')
                    score_drop()
                    break
        except Exception:
            continue   
        print(''.join(curent_view))
        print('Количество попыток: ', 5-at)

def menu():
    while True:
        score_read()    
        st=input('Получить вопрос[н], выход[в], сброс очков[р], изменить игрока[и]')
        if st=='н':
            game()
        if st=='р':
            score_resset()
        if st=='и':
            player_add()
        else:
            break
player_add()
menu()