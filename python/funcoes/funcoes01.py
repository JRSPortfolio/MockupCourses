# concat('abc', 'def') => 'abcdef'
# concat('abc', 23, True, ['alberto', 19]) => "abc23True['alberto', 19]"
# concat('abc', 23, 'def', sep='/', end='.') => 'abc/23/def.'

from typing import Iterable


def concat(*args, sep=' ', end='\n'):
    item_str = []
    for arg in args:
        item_str.append(str(arg))
    item_str.append(end)
    
    return sep.join(item_str)

def fun1(a, b, *args):
    print(a)
    print(b)
    print(args)

def fun2(a, b, *args, c):
    print(a)
    print(b)
    print(args)
    print(c)

def fun3(a, b, *args, c=78, d=90, **kargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kargs)
    
def fun4(*args, **kargs):
    print(args)
    print(kargs)

#####################################################
# 
#       FUNÇÕES DE PRIMEIRA ORDEM
#       Funções parametrizadas com outras funções
#
#####################################################

nums = [100, -2, -1, 59, 44, 46, 77]
nomes = ['alberto', 'bruno', 'armando', 'josé', 'albertina']

def filtra_positivos(items: Iterable):
    selecionados = []
    for item in items:
        if item > 0:
            selecionados.append(item)
    return selecionados

def filtra_pares(items: Iterable):
    selecionados = []
    for item in items:
        if item % 2 == 0:
            selecionados.append(item)
    return selecionados

def filtra_maior50(items: Iterable):
    selecionados = []
    for item in items:
        if item > 50:
            selecionados.append(item)
    return selecionados

def filtra_nomes_maior_6(items: Iterable):
    selecionados = []
    for item in items:
        if len(item) > 6:
            selecionados.append(item)
    return selecionados

def filtra (items :Iterable, criterio):
    selecionados = []
    for item in items:
        if criterio(item):
            selecionados.append(item)
    return selecionados

def e_par(num: int):
    return num % 2 == 0

def nome_maior_q_6(nome: str):
    return len(nome) > 6

def e_positivo(num: int):
    return num > 0



#####################################################
# 
#       RECURSIVIDADE
#       FUNÇÕES INTERNAS / ANINHADAS / NESTED
#
#####################################################
nums2 = [1, 2, [3, [4, 5], 6], 7] 


def factorial (n: int):
    res = 1
    for i in range(n, 1, -1):
        res *= i
    return res

def factorialR(n: int):
    if n in (0, 1) or n < 0:
        return 1
    return n * factorialR(n-1)

def fibI(n):
    if n in (0, 1):
        return n
    x, y = 0, 1
    for _ in range(2, n+1):
        y, x = y + x, y
    return y

def fibi2(n):
    if n in (0, 1):
        return n
    f2, f1, fN = 0, 1, 0
    for _ in range(2, n + 1):
        fN = f1 + f2
        f2 = f1 + f2
        f2 = f1
        f1 = fN
    return fN    

def fibR(n):
    if n in (0, 1):
        return n
    return fibR(n -1 ) + fibR(n - 2)

def e_palindromoI(txt: str):
    i, k = 0, len(txt) -1
    while i < k:
        if txt[i] != txt[k]:
            return False
        i += 1
        k -= 1 
    return True

def e_palindromoR(txt: str):
    if len(txt) <= 1:
        return True
    return txt[0] == txt[-1] and e_palindromoR(txt[1:-1])

def flatten1(lst: list):
    if len(lst) == 0:
        return lst
    
    first, rest = lst[0], lst[1:]
    if isinstance(first, list):
        return flatten1(first) + flatten1(rest)
    return [first] + flatten1(rest)

def flatten2(lst: list):
    def do_flatten(lst: list, pos: int, ret_list: list):
        if pos == len(lst):
            return
        
        curr = lst[pos]
        if isinstance(curr, list):
            do_flatten(curr, 0, ret_list)
        else:
            ret_list.append(curr)
        do_flatten(lst, pos + 1, ret_list)
    
    ret_list = []
    do_flatten(lst, 0, ret_list)
    return ret_list

def flattenI(lst: list):
    ret_list = []
    pos = 0
    while pos < len(lst):
        if isinstance(lst[pos], list):    
            temp = lst[pos:]
            while isinstance(temp, list):
                if isinstance(temp, list):
                    temp = temp[0]
        else:
            temp = lst[pos]
        ret_list.append(temp)
        pos += 1
    return ret_list
                    
            
 
 
#####################################################
# 
#       FUNÇÕES INTERNAS: CLOSURES
#
#####################################################

# def verde(Z):
#     X = ...    # definir X
#     def vermelha(...):
#         Y = ...
#         # tem acesso a X e a Y e a Z
#         ...
#     ...
#     # tem acesso apenas X 
#     return vermelha 
#
#         ┌─────────────────────────────────┐
#         │              ┌───────────────┐  │
#         │              │               │  │
#         │  VERMELHA    │     VERDE     │  │
#         │              │               │  │
#         │              └───────────────┘  │
#         └─────────────────────────────────┘

def somador(x: int):
    def soma(y: int):
        return x + y
    return soma

def somador2(x: int):
    return lambda y: x + y    
 
def contador(inicio = 0):
    i = inicio - 1 
    def conta():
        nonlocal i
        i += 1
        return i
    return conta


months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

def month_name(month_num: int):
    return months[month_num -1]

def month_name2(month_num: int):
    months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
    ]
    return months[month_num - 1]

def _make_month_name():
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]

    return lambda month_num: months[month_num -1]

import re
import time

def is_valid_date(date: str) -> bool:
    YEAR       = '(19[0-9][0-9]|20[0-4][0-9]|2050)';
    DD_MM_31   = '(0[1-9]|[12][0-9]|30|31)/(0[13578]|1[02])';
    DD_MM_30   = '(0[1-9]|[12][0-9]|30)/(0[469]|11)';
    DD_FEB     = '(0[1-9]|1[0-9]|2[0-8])/02';
    LEAP_YEARS = ('(1904|1908|1912|1920|1924|1928|1932|1936|1940|1944'
                    '|1948|1952|1956|1960|1964|1968|1972|1976|1980'
                    '|1984|1988|1992|1996|2000|2004|2008|2012|2016'
                    '|2020|2024|2028|2032|2036|2040|2044|2048)' )
    DD_FEB_LEAP_YEAR = f'(0[1-9]|[12][0-9])/02/{LEAP_YEARS}';
    date_reg_exp = re.compile(
        rf'^({DD_FEB_LEAP_YEAR}|({DD_MM_31}|{DD_MM_30}|{DD_FEB})/{YEAR})$'
    )
    return bool(date_reg_exp.match(date.strip()))
# is_valid_date('10/02/2021')   DD/MM/AAAA

def make_is_valid_date():
    YEAR       = '(19[0-9][0-9]|20[0-4][0-9]|2050)';
    DD_MM_31   = '(0[1-9]|[12][0-9]|30|31)/(0[13578]|1[02])';
    DD_MM_30   = '(0[1-9]|[12][0-9]|30)/(0[469]|11)';
    DD_FEB     = '(0[1-9]|1[0-9]|2[0-8])/02';
    LEAP_YEARS = ('(1904|1908|1912|1920|1924|1928|1932|1936|1940|1944'
                    '|1948|1952|1956|1960|1964|1968|1972|1976|1980'
                    '|1984|1988|1992|1996|2000|2004|2008|2012|2016'
                    '|2020|2024|2028|2032|2036|2040|2044|2048)' )
    DD_FEB_LEAP_YEAR = f'(0[1-9]|[12][0-9])/02/{LEAP_YEARS}';
    date_reg_exp = re.compile(
        rf'^({DD_FEB_LEAP_YEAR}|({DD_MM_31}|{DD_MM_30}|{DD_FEB})/{YEAR})$'
    )
    return lambda date: bool(date_reg_exp.match(date.strip()))
# is_valid_date('10/02/2021')   DD/MM/AAAA

def timed_run(fun, *args, **kargs):
    start  = time.time()
    for _ in range(10_000_000):
        fun(*args, **kargs)
    return int(time.time() - start)
    
                    
# MAPEIA

def mapeia(items: Iterable, mapeamento):
    transformados = []
    for item in items:
        transformados.append(mapeamento(item))
    return transformados

def dobro(num: int | float):
    return num * 2

#####################################################
# 
#       EXPRESSÃO LISTA (e outras)
#       Alternativa mais idiomática a MAP e FILTER
#
#####################################################

# list(map(lambda x: 2 * x, nums))
# list(filter(lambda x: x > 0, nums))
# list(map(lambda x: 2 * x, filter(lambda x: x > 0, nums)))

# print([2 * x for x in nums])
# print([x for x in nums if x > 0])
# print([2 * x for x in nums if x > 0])


# print (concat('argumento1', 355, 'argumento2'))
# print (fun1(b = 3, a = 6))
# print (fun2(3, '7', 677, c= 'argumento'))
# print (fun3('argumento1', 789, 577, 'argumento2', 454, d = 9999,  e = 8777, xpto = 'nome'))
# print (fun4())
# print (filtra_nomes_maior_6(nomes))
# print(filtra(nomes, nome_maior_q_6))
# print(filtra(nums, lambda num: num % 2 == 0))
# print(filtra(nums,e_positivo))

#dim = int(input("Tamanho: "))
# print(filtra(nomes, lambda nome: len(nome) > dim))



# ------------------- filter--------------------------------------
# print(list(filter(lambda nome: len(nome) > dim, nomes)))
# for val in filter(lambda nome: len(nome) > dim, nomes):
#     print(val)
#-----------------------------------------------------------------



# print(mapeia(nums, dobro))
# print(mapeia(nums, lambda num: 2 * num))
# print(mapeia(nomes, lambda nome: nome[0]))
# print(mapeia(nomes, lambda nome: nome[-1]))
# print(mapeia(nomes, len))



#---------------------map-----------------------------------------
# print(tuple(map(lambda num: 2 * num, nums)))



#Três primeiras letras dos nomes com mais que 5 caracteres
# print(tuple(map(lambda nome: nome[:3],filter(lambda nome: len(nome) > 5, nomes))))
# com_mais_q_6 = filter(lambda nome: len(nome) > 5, nomes)
# print(tuple(map(lambda nome: nome[:3], com_mais_q_6)))



#-------------------------------sorted----------------------------------
# print(sorted(nums))
# print(sorted(nomes))
# print(sorted(nums, key = lambda num: str(abs(num))[0]))
# print(sorted(nomes, key = lambda nome: nome[-1]))

# print (factorialR(-2))
# print(fibR(50))

print(flattenI(nums2))