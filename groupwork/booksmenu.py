import books

newLib=books.library()
#newLib.info("Математика для тех, кто не открывал учебник")
def book_search():
    get_book=input('\nВведите название книги:\n')
    newLib.infoBook(get_book)
def author_search():
    get_author = input('\nВведите имя автора:\n')
    newLib.infoAuthor(get_author)
def book_by_letter():
    get_book = input('\nВведите название книги:\n')
    newLib.book_by_letter(get_book)
def author_by_letter():
    get_author = input('\nВведите имя автора:\n')
    newLib.author_by_letter(get_author)
def menu():
    while True:
        flag = input('\n'
            'Поиск книги[п]         Поиск по букве книги[1]      Добавление книги[н]\n'
            'Поиск по автору[а]     Поиск по букве автора[2]     Выход[в]\n')
        if flag == 'п':
            print('\nПоиск книги')
            book_search()
        elif flag == '1':
            print('\nПоиск по букве книги')
            book_by_letter()
        elif flag== 'н':
            print('\nДобавление книги')
            newLib.add_book()
        elif flag == 'а':
            print('\nПоиск по автору')
            author_search()
        elif flag == '2':
            print('\nПоиск по букве автора')
            author_by_letter()
        elif flag == 'в':
            print('\nВыход')
            break
        else:
            break

print('Добро пожаловать в бибилиотеку.\n')
menu()
