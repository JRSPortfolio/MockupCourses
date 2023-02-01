"""
Programa para gestão do catálogo de produtos. Este programa permite:
    - Listar o catálogo
    - Pesquisar por alguns campos 
    - Eliminar um registo do catálogo
    - Guardar o catálogo em ficheiro
"""

from decimal import Decimal as dec
import subprocess
import sys
from typing import TextIO

CSV_DEFAULT_DELIM = ','
DEFAULT_INDENTATION = 3

################################################################################
##
##       PRODUTOS E CATÁLOGO
##
################################################################################


PRODUCT_TYPES = {'AL' : 'Alimentação', 'DL' : 'Detergente p/ loiça', 'FRL' : 'Frutas e Legumes'}

class Produto:
    def __init__(self, id: int, nome: str, tipo: str, quantidade: int, preco: dec):
        if id < 0 or len(str(id)) != 5:
            raise ValueError(f'{id=} inválido (deve ser > 0 e ter 5 dígitos)')
        if not nome:
            raise ValueError (f"{nome=} nome não pode ser vazio")
        # if len(nome) == 0:
        #     raise ValueError (f"{nome=} nome não pode ser vazio")
        if quantidade < 0:
            raise ValueError(f"{quantidade=} a quantidade deve ser > 0")
        if tipo not in PRODUCT_TYPES:
            raise ValueError(f"{tipo=} não se encontra na lista de produtos")
        if preco <= 0:
            raise ValueError (f"{preco=} o preço têm de ser > 0")
        
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.quantidade = quantidade
        self.preco = preco
    #:
    
    @property
    def desc_tipo(self):
        return PRODUCT_TYPES(self.tipo)
    
    def __str__(self):
        return f"Produto[id: {self.id} nome: {self.nome} tipo: {self.tipo} quantidade: {self.quantidade} preco: {self.preco}]"
    #:
#:

def main():
    prod1 = Produto(30987, "pão de milho", "AL", 10, dec('1'))
    prod2 = Produto(30098, "leite mimosa", "AL",25, dec('2'))

    print(prod1)
    print(prod2)

    try:
        Produto(39877, "leite mimosa", "AL", 1, dec(0))
    except ValueError as ex:
        print("ATENÇÃO: Produto inválido!")
        print(ex)
#:

if __name__ == '__main__':
    main()
#:



# class Xpto {

#     public toString() {
#         return String.format("Xpto: valor de a -> %d", a);
#     }

#     private int a;
# }

# var obj = new Xpto();
# obj.a = 100;
# System.out.println(obj);    // Xpto: valor de a -> 100