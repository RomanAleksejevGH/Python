
def max2(x,y):          #функция возврата максимального значения из 2х входящих
    if x>y:
        return x        # return - обрывает функцию и возвращает значение (все что написано после return не исполняется!)
    return y

# функция max3 использует max2 2 раза чтобы вычислить максимальное значение из 3х. 
# сначала выполняется max2(y,z) после max2(x, и максимальное значение из y и z)
def max3(x,y,z):
    return max2(x,max2(y,z)) 

#Separator вставляется между переменными вывода.
#Если при создании метода присвоить какоето значение переменой, то во время вызова метода он будет использовать ее, если не
#получил другое значение!
def new_separator(name = "World",separator="-"):
    print("Hello",name,sep=separator)
"""
new_separator(separator="***",name="John")
new_separator()
new_separator("Sam")
new_separator("Din","!!!")
"""
def is_simple_number(x):
    """ Определяет, является ли число простым.
    x - целое положительное число.
    Если простое, то возвращает True, а иначе - False"""
    divisor=2
    while divisor<x:
        if x%divisor==0:
            return False
        divisor+=1
    return True
def factorize_number(x):
    """Раскладывает число на множители.
       Печатает их на экран.
       х - целое положительное число.
    """
    divisor = 2
    while x > 1:
        if x%divisor==0:
            print(divisor)
            x//=divisor
        else:
            divisor+=1


