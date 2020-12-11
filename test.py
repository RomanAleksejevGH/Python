
    # Создаём список с элементами название;автор
autor = open("books.txt", "r", encoding=("utf-8"))
autor_list = autor.read().splitlines()

print(autor_list)

