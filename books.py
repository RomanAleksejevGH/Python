class library:
    """
        Создание списков :
        BOOK - список названий книг
        AUTHOR - список авторов книг
        REVIEW - список обзоров на книги
        BUY - список ссылок на книги
    """
    #создание пустых раздельных списков...
    BUY = []
    REVIEW = []
    BOOK = []
    AUTHOR = []
    def __init__(self):
        self.AUTHOR
        self.BOOK
        self.BUY
        self.REVIEW

        #чтение из файлов и перевод в списки строк
        with open('books.txt', 'r', encoding='utf-8-sig')as f:              #чтение из файла и создание списка типа [книга;автор]
            book_author = f.read().splitlines()
        with open("booksinfo.txt", "r", encoding=("utf-8-sig")) as f:       #чтение из файла и создание списка типа [книга;инфо]
            review_list = f.read().splitlines()
        with open("bookbuy.txt", "r", encoding=("utf-8-sig")) as f:         #чтение из файла и создание списка типа [книга;link]
            buy_list = f.read().splitlines()
            

        #разбивка 
        for n_str in range (0,len(book_author)):            # n_str - перебор строк в списке [книга;автор] от 0 до конца списка
            book_buy_value=str(buy_list[n_str])             # book_buy_value - переменная типа str получающая значение ('книга;link'[номер строки в списке])
            book_author_value=str(book_author[n_str])       # тоже самое что и book_buy_value только 'книга;автор'
            book_review_value=str(review_list[n_str])       # тоже самое что и book_buy_value только 'книга;инфо'
            
            for x in range(0,len(book_author_value)):       # x - номер символа в строке 'книга;автор'
                
                if book_author_value[x] == ';':                              # находим где в строке находится знак ';'
                    buy = book_buy_value[x+1:len(book_buy_value)]           #режим строку и берем в переменную значение после ';'
                    review = book_review_value[x+1:len(book_review_value)]  #режим строку и берем в переменную значение после ';'
                    book = book_author_value[0:x]                           #режим строку и берем в переменную значение до ';'
                    author = book_author_value[x+1:len(book_author_value)]  #режим строку и берем в переменную значение после ';'
                    
                    #заполнение отдельных списков... прим: в конец списока BOOK добовляется значение переменной book 
                    self.BUY.append(buy)
                    self.REVIEW.append(review)
                    self.BOOK.append(book)
                    self.AUTHOR.append(author)
                    
    def info (self,name):                                               #принимает значение(в данном случае название книги)
            for k in range(len(self.BOOK)):                             # k- номер строки в списке с совпадением, если переделать например на self.AUTHOR можно организовать поиск по автору
                if self.BOOK[k] == name:
                    self.book = print('названия\n', self.BOOK[k])       #вывод значения списка по типу НазваниеСписка[номер строки в списке]
                    self.author=print('авторы\n', self.AUTHOR[k])
                    self.review=print('обзор\n', self.REVIEW[k])
                    self.buy = print('ссылка на книгу\n', self.BUY[k])
            return 'Нет такой книги'

newLib=library()
newLib.info("Математика_для_тех,_кто_не_открывал_учебник")  #пример вывода info
