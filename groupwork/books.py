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
            book_author = f.read().split('\n')
        with open("booksinfo.txt", "r", encoding=("utf-8-sig")) as f:       #чтение из файла и создание списка типа [книга;инфо]
            review_list = f.read().split('\n')
        with open("bookbuy.txt", "r", encoding=("utf-8-sig")) as f:         #чтение из файла и создание списка типа [книга;link]
            buy_list = f.read().split('\n')
            

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
                    
    def add_book(self):
        addBook = str(input("Введите название новой книги: "))
        addAuthor = str(input("Введите автора новой книги: "))
        addReview = str(input("Введите описание новой книги: "))
        addBuy = str(input("Введите ссылку на покупку новой книги: "))
        self.BOOK.append(addBook)
        self.REVIEW.append(addReview)
        self.BUY.append(addBuy)
        self.AUTHOR.append(addAuthor)
        with open('bookbuy.txt', 'a', encoding=('utf-8-sig')) as s:
            s.write('\n')
            s.write(addBook)
            s.write(';')
            s.write(addBuy)
        with open('books.txt', 'a', encoding=('utf-8-sig')) as s:
            s.write('\n')
            s.write(str(addBook))
            s.write(';')
            s.write(str(addAuthor))
        with open('booksinfo.txt', 'a', encoding=('utf-8-sig')) as s:
            s.write('\n')
            s.write(str(addBook))
            s.write(';')
            s.write(str(addReview))
                    
    def infoBook (self,name):                                               #принимает значение(в данном случае название книги)
        for k in range(len(self.BOOK)):                             # k- номер строки в списке с совпадением, если переделать например на self.AUTHOR можно организовать поиск по автору
            if self.BOOK[k] == name:
                    self.book = print('\nназвание\n', self.BOOK[k])       #вывод значения списка по типу НазваниеСписка[номер строки в списке]
                    self.author=print('\nавтор\n', self.AUTHOR[k])
                    self.review=print('\nобзор\n', self.REVIEW[k])
                    self.buy = print('\nссылка на книгу\n', self.BUY[k])
            if name not in self.BOOK:
                print('\nК сожилению такой книги пока что нет в нашей библиотеке\n')

    def infoAuthor(self, name):
        for k in range(len(self.AUTHOR)):
            if self.AUTHOR[k] == name:
                    self.book = print('\nназвание\n', self.BOOK[k])
                    self.author = print('\nавтор\n', self.AUTHOR[k])
                    self.review = print('\nобзор\n', self.REVIEW[k])
                    self.buy = print('\nссылка на книгу\n', self.BUY[k])
            if name not in self.AUTHOR:
                print('\nК сожилению автора с таким именем пока что нет в нашей библиотеке\n')
    
    def book_by_letter(self,letter):
        print("\nНайденные совпадения\n")
        print("\n".join(s for s in self.BOOK if letter.lower() in s.lower()))
    
    def author_by_letter(self, letter):
        print("\nНайденные совпадения\n")
        print("\n".join(s for s in self.AUTHOR if letter.lower() in s.lower()))

