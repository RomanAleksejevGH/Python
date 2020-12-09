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
        with open('books.txt', 'r', encoding='utf-8-sig')as f:
            book_author = f.read().splitlines()
        with open("booksinfo.txt", "r", encoding=("utf-8-sig")) as f:
            review_list = f.read().splitlines()
        with open("bookbuy.txt", "r", encoding=("utf-8-sig")) as f:
            buy_list = f.read().splitlines()
            

        #разбивка 
        for n_str in range (0,len(book_author)):
            book_buy_value=str(buy_list[n_str])
            book_author_value=str(book_author[n_str])
            book_review_value=str(review_list[n_str])
            
            for x in range(0,len(book_author_value)):
                
                if book_author_value[x] == ';':
                    buy = book_buy_value[x+1:len(book_buy_value)]
                    review = book_review_value[x+1:len(book_review_value)]
                    book = book_author_value[0:x]
                    author = book_author_value[x+1:len(book_author_value)]
                    
                    #заполнение отдельных списков...
                    self.BUY.append(buy)
                    self.REVIEW.append(review)
                    self.BOOK.append(book)
                    self.AUTHOR.append(author)
    def info (self,name):
            for k in range(len(self.BOOK)):
                if self.BOOK[k] == name:
                    self.book = print('названия\n', self.BOOK[k])
                    self.author=print('авторы\n', self.AUTHOR[k])
                    self.review=print('обзор\n', self.REVIEW[k])
                    self.buy = print('ссылка на книгу\n', self.BUY[k])
            return 'Нет такой книги'

newLib=library()
newLib.info("Математика_для_тех,_кто_не_открывал_учебник")
