def mas01():
    """ Создание списка A нужной величины.
    заполнение и вывод значений в обратном порядке
    """
    A=[0]*10                # 10 - число ячеек в списке
    top=0                   # top - переменная для перебора по порядку значений в списке
    x=int(input('Ввод значений в список(если значение равно нулю, то ввод прикратится'))
    while x!=0:
        A[top]=x
        top+=1
        x=int(input())
    for k in range (top-1,-1,-1):  # вывод в обратном порядке начнется после заполнения списка
        print(A[k]) 
def mas02():
    """создание 2х списков 'A' и 'B' (n - пользователь вводит длину списка) 
    1ый цикл for заполняет список 'A'
    2ой цикл for копирует значения из 'A' в 'B'
    'C' не является списком, а только ссылается на 'A'
    'D' с помощью конструктора класса списков 'list' копирует данные из списка 'A' 
    """
    n=int(input())
    A=[0]*n
    B=[0]*n
    for k in range (n):
        A[k]=int(input())
    for k in range (n):
        B[k]=A[k]
    C=A
    D=list(A)

def list_search(array:list,search_in:int,what_to_search:int):
    """Поиск значения в списке.
    'array' - выбор списка, 'list' - какой тип списка должен быть
    'search_in' - в какой области списка искать значение типа 'int'
    'what_to_search' - искомое значение типа 'int'
    Возвращает индекс элемента списка или -1 если такого нет.
    Если в списке найдено несколько  одинаковых элементов, то вернуть индекс первого по счету.
    """
    for k in range(search_in):
        if array[k] == what_to_search:
            return k
    return -1

def test_arrray_search():
    A1=[1, 2, 3, 4, 5]
    m=list_search(A1, 5, 8)
    if m==-1:
        print("#test1 - ok")
    else:
        print("#test1 - fail")
        
    A2 = [-1, -2, -3, -4, -5]
    m = list_search(A2, 5, -3)
    if m == 2:
        print("#test2 - ok")
    else:
        print("#test2 - fail")
        
    A3 = [10, 20, 30, 10, 10]
    m = list_search(A3, 5, 10)
    if m == 0:
        print("#test3 - ok")
    else:
        print("#test3 - fail")


def invert_array(A:list, N:int):
    """Обращение списка (поворот задом-наперед)
       в рамках индексов от 0 до N-1
    """
    for k in range (N//2):
        A[k], A[N-1-k] = A[N-1-k], A[k]
        
def test_invert_array():
    A1 = [1, 2, 3, 4, 5]
    invert_array(A1,5)
    if A1 == [5, 4, 3, 2, 1]:
        print("#test1 - ok")
    else:
        print("#test1 - fail")
    print(A1)
        
    A2 = [0, 0, 0, 0, 0, 0, 0, 10]
    invert_array(A2, 8)
    if A2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print("#test2 - ok")
    else:
        print("#test2 - fail")
        

def cyclic_shift(A:list,N:int):
    """Циклический сдвиг в лево значений в списке
    для сдвига в право: 
    tmp = A[N-1]
    for k in range (N-2,-1,-1)
        A[+1]=A[k]
    A[0]=tmp"""
    tmp=A[0]
    for k in range(N-1):
        A[k]=A[k+1]
    A[N-1]=tmp
    
def test_cyclic_shift():
    A1 = [1, 2, 3, 4, 5]
    cyclic_shift(A1, 5)
    if A1 == [2, 3, 4, 5, 1]:
        print("#test1 - ok")
    else:
        print("#test1 - fail")
    print(A1)
    

def sieve_of_eratosthenes(A:list,N:int):
    """решето эратосфена"""
    A=[True]*N
    A[0]=A[1]= False
    for k in range (2,N):
        if A[k]:
            for m in range(2*k,N,k):
                A[m]=False
    for k in range (N):
        print(k,'-',"простое" if A[k]else "составное")


def test_sieve_of_eratosthenes():
    A1 = [1, 2, 3, 4, 5]
    sieve_of_eratosthenes(A1, 5)

def blank_list ():
    """ A[] - Списки можно создавать без определенного количества элементов.
    List comprehensions:
    A=[x**2 for x in range(10)] <=> A=[]
                                    for x in range(10)
                                        A.append(x**2)
    """
    A=[]
    B = []
    x = int(input())
    A.append(x)  #добавление значения в конец списка
    n=len(A)  # n = количество элементов в списке
    x=A.pop() # удаляет последнее значение в списке
    """Копирование квадрата числа находящегося в четной ячейке списка A в список B"""
    
    for x in A:             # <=> B=[x**2 for x in A if x%2==0] <=> B=[0 if x<0 else x**2 for x in A if x%2==0]
        if x%2==0:
            B.append(x**2)

def insert_sort(A):
    """ Сортировка списка A вставками """
    N = len(A)
    for top in range (1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1
def choise_sort(A):
    """ сортировка списка А выбором """
    N = len(A)
    for pos in range (0, N-1):
        for k in range (pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]
def bubble_sort(A):
    """ сортировка списка А методом пузырька """
    N=len(A)
    for bypass in range (1, N):
        for k in range (0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
                
def test_sort(sort_alorithm):
    print("Тестируем: ", sort_alorithm.__doc__) # так можно вывести коментарий к методу
    print("testcase #1: ", end="")
    A=[4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_alorithm(A)
    print("Ok" if A == A_sorted else "Fail")
    
    print("testcase #2: ", end="")
    A = list(range(10,20)) + list(range(0,10))   # range - гениратор арифметической прогрессии
    A_sorted = list(range(20))
    sort_alorithm(A)
    print("Ok" if A == A_sorted else "Fail")
    
    print("testcase #3: ", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_alorithm(A)
    print("Ok" if A == A_sorted else "Fail")

""" Запуск тестов
test_sort(insert_sort)
test_sort(choise_sort)
test_sort(bubble_sort)
"""

def count_sort(A):
    """
    Сортировка подсчетом
    Для работы необходимо знать допустимый диапазон значений списка
    """
    N=len(A)
    F=[0]*R   # R - количество разных допустимых значений списка
    for i in range (N):
        x=int(input())  # ввод разных значений списка
        F[x] +=1

