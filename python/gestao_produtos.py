"""
Programa para gestão do catálogo de produtos. Este programa permite:
    - Listar o catálogo
    - Pesquisar por alguns campos 
    - Eliminar um registo do catálogo
    - Guardar o catálogo em ficheiro
"""

from decimal import Decimal as dec, InvalidOperation as io
import subprocess
import sys
from typing import TextIO

CSV_DEFAULT_DELIM = ','
DEFAULT_INDENTATION = 3
FILEPATH = 'python\\produtos_rasc.csv'

################################################################################
##
##       PRODUTOS E CATÁLOGO
##
################################################################################


PRODUCT_TYPES = {'AL' : 'Alimentação', 'DL' : 'Detergente p/ loiça', 'FRL' : 'Frutas e Legumes'}

class Produto:
    def __init__(self, id: int, nome: str, tipo: str, quantidade: int, preco: dec):
        if id < 0 or len(str(id)) != 5:
            raise InvalidProdAttribute(f'{id=} inválido (deve ser > 0 e ter 5 dígitos)')
        if not nome:
            raise InvalidProdAttribute (f"{nome=} nome não pode ser vazio")
        # if len(nome) == 0:
        #     raise ValueError (f"{nome=} nome não pode ser vazio")
        if quantidade < 0:
            raise InvalidProdAttribute(f"{quantidade=} a quantidade deve ser > 0")
        if tipo not in PRODUCT_TYPES:
            raise InvalidProdAttribute(f"{tipo=} não se encontra na lista de produtos")
        if preco <= 0:
            raise InvalidProdAttribute (f"{preco=} o preço têm de ser > 0")
        
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
        cls_name = self.__class__.__name__
        #return f"Produto[id: {self.id} nome: {self.nome} tipo: {self.tipo} quantidade: {self.quantidade} preco: {self.preco}]"
        return f'{cls_name}[id_ = {self.id} nome = "{self.nome}" tipo = "{self.tipo}" quantidade = "{self.quantidade}" preço = "{self.preco}"]'
    #:
    
    @classmethod
    def from_csv(cls, linha: str, delim = CSV_DEFAULT_DELIM):
        attrs = linha.split(delim)
        #return cls(id = int(attrs[0]), nome = attrs[1], tipo = attrs[2], quantidade = int(attrs[3]), preco = dec(attrs[4]))
        return Produto(id = int(attrs[0]), nome = attrs[1], tipo = attrs[2], quantidade = int(attrs[3]), preco = dec(attrs[4]))
#:

# class ProdutoEspecial(Produto):
#     def __init__(self, promocao, *args, **kargs):
#         super().__init__(*args, **kargs)
#         self.promocao = promocao
#     def valor_stock(self):
#         return self.quantidade * self.preco

class InvalidProdAttribute(ValueError):
    pass

class CatalogoProdutos:
    def __init__(self):
        self._prods = {}
        
    def append(self, prod: Produto):
        if prod.id in self._prods:
            raise DuplicateValue(f"Já existe produto com id {prod.id} no catalogo.")
        self._prods[prod.id] = prod     
    
    def _dump(self):
        for prod, n in self._prods.items():
            print(prod, n)
    
    def obtem_por_id(self, id: int):
        return {self._prods.get(id)}
    
    def pesquisa(self, criterio):
        encontrados = CatalogoProdutos()
        for prod in self._prods.values():
            if criterio(prod):
                encontrados.append(prod)
        return encontrados
    
    def __str__(self):
        class_name = self.__class__.__name__
        return f'{class_name} [Quantidade de Produtos: {len(self._prods)}]'
    
    def __len__(self):
        return len(self._prods)
    
    def __iter__(self):
        for prod in self._prods.values():
            yield prod  
            
    @property
    def list_produtos(self):
        return self._prods   
         
class DuplicateValue(Exception):
    ...

###########################################################
##
##              Leitura e Escrita de ficheiros
##
###########################################################

def le_produtos(caminho_fich: str, delim = CSV_DEFAULT_DELIM):
    prods = CatalogoProdutos()
    with open(caminho_fich, 'rt', encoding='UTF-8') as fich:
        for linha in linhas_relevantes(fich):
            prods.append(Produto.from_csv(linha, delim))
            # attrs = linha.split(delim)
            # prods.append(Produto(id = int(attrs[0]), nome = attrs[1], tipo = attrs[2], quantidade = int(attrs[3]), preco = dec(attrs[4])))
    return prods

def linhas_relevantes(fich: TextIO):
    for linha in fich:
        linha = linha.strip()
        if len(linha.strip()) == 0 or linha[0] ==  '#':
            continue
        yield linha

def add_produto(caminho_fich: str, prod: Produto):
    with open (caminho_fich, 'at') as fich:
        fich.write(f"{prod.id},{prod.nome},{prod.tipo},{prod.quantidade},{prod.preco}\n") 
        
def rem_produto(caminho_fich: str, iden: int):
    with open(caminho_fich, "rt") as fich:
        linhas = fich.readlines()
    with open(caminho_fich, "wt") as fich:
        for linha in linhas:
            if linha[0:5] != str(iden):
                fich.write(linha)
                
def actualizar_produtos(caminho_fich: str, produtos: CatalogoProdutos, lista_ids: list):               
    with open(FILEPATH, 'rt') as fich:
        for linha in linhas_relevantes(fich):
            for prod in produtos:
                if linha[0:5] == str(prod.id):
                    lista_ids.append(prod.id)
    with open(FILEPATH, 'at') as fich:
        for prod in produtos:
            if prod.id not in lista_ids:
                fich.write(f"{prod.id},{prod.nome},{prod.tipo},{prod.quantidade},{prod.preco}\n")   
                
#######################################################################
##
##
##            Menu, Opções e Interacção com o utilizador
##
##
#######################################################################

def exibe_msg(*args, indent = DEFAULT_INDENTATION, **kargs):
    print(' ' * (indent - 1), *args, **kargs)
    
def entrada(msg: str, indent = DEFAULT_INDENTATION):
    return input(f"{' ' * DEFAULT_INDENTATION}{msg}")
    
def cls():
    if sys.platform == 'win32':
        subprocess.run(['cls'], shell=True, check=True)
    elif sys.platform in ('darwin', 'linux', 'bsd', 'unix'):
        subprocess.run(['clear'], check=True)
        
def pause(msg: str="Pressione ENTER para continuar...", indent = DEFAULT_INDENTATION):
    input(f"{' ' * indent}{msg}")

produtos = CatalogoProdutos()

def exec_menu():
    while True:
        #cls()
        exibe_msg("***************************************")
        exibe_msg("* L - Listar Catlálogo                *")
        exibe_msg("* P - Pesquisar por ID                *")
        exibe_msg("* A - Acrescentar Produto             *")
        exibe_msg("* E - Eliminar Produto                *")
        exibe_msg("* G - Guardar Catalogo em Ficheiro    *")
        exibe_msg("*                                     *")
        exibe_msg("* T - Terminar Programa               *")
        exibe_msg("***************************************")
        
        print()
        opcao = entrada("Opção: ").strip().upper()
        
        if opcao in ('L', 'LISTAR'):
            exec_listar()
        elif opcao in ('P', 'PESQUISAR'):
            exec_pesquisar()
        elif opcao in ('A', 'ACRESCENTAR'):            
            exec_add()
        elif opcao in ('T', 'TERMINAR'):
            exec_terminar()
        elif opcao in ('E', 'ELIMINAR'):
            exec_eleminar()
        elif opcao in ('G', 'GUARDAR'):
            exec_guardar()
        else:
            exibe_msg(f"opção{opcao} inválida.")
            pause()
            
def exec_listar():
    cabecalho = f'{"ID":^8}|{"Nome":^26}|{"Tipo":^8}|{"Quantidade":^16}|{"Preço":^16}|'
    separador = f'{"-" * 8}+{"-" * 26}+{"-" * 8}+{"-" * 16}+{"-" * 16}+'
    print()
    exibe_msg(cabecalho)
    exibe_msg(separador)
    for prod in produtos:
        linha = f"{prod.id:^8}|{prod.nome:^26}|{prod.tipo:^8}|{prod.quantidade:^16}|{prod.preco:^16}|"
        exibe_msg(linha)
    exibe_msg(separador)
    print()
    pause()
    
def exec_pesquisar():
    print()
    pesq = int(entrada("Insira o nº de ID a pesquisar: "))
    
    def criterio_pes(prod: Produto, valor = pesq):
        if prod.id == valor:
            return True
        
    encontrados = produtos.pesquisa(criterio_pes)
    
    if encontrados:    
        exibe_msg("Foi encontrado:")
        exibe_msg(f"ID: {encontrados.list_produtos[pesq].id} || Tipo: {encontrados.list_produtos[pesq].tipo}\
 || Quantidade: {encontrados.list_produtos[pesq].quantidade} || Preço: {encontrados.list_produtos[pesq].preco}")
    else:
        exibe_msg(f"Não foi encontrado ID {pesq}")
    print()
    pause()
    
def exec_add():
    try:
        iden = int(entrada("Insira o ID do produto: "))
    except ValueError as ipa:
        exibe_msg(f"Erro de inserção: {ipa}")
        print()
        return 
    for prod in produtos:
        if prod.id == iden:
            exibe_msg(f"Já existe um produto com o codigo {iden}")
            print()
            pause()
            return
    nome = entrada("Insira o nome do produto: ")
    tipo = entrada("Insira o tipo do produto: ")
    try:    
        quant = int(entrada("Insira o quantidade do produto: "))
    except ValueError as ipa:
        exibe_msg(f"Erro de inserção: {ipa}")
        print()
        pause()
        return
    try:
        preco = dec(entrada("Insira o preco do produto: "))
    except io as ipa:
        exibe_msg(f"Erro de inserção: {ipa}")
        print()
        pause()
        return
    try:
        prod = Produto(iden,nome,tipo,quant,preco)
        add_produto(FILEPATH, prod)
        produtos.append(prod)
    except InvalidProdAttribute as ipa:
        exibe_msg(f"Erro de inserção: {ipa}")
        print()
        pause()
        
def exec_eleminar():
    try:
        iden = int(entrada("Insira o ID do produto a eliminar: "))
    except ValueError as ipa:
        exibe_msg(f"Erro de inserção: {ipa}")
        print()
        pause()
        return 
    if iden in produtos.list_produtos.keys():
        produtos.list_produtos.pop(iden)
        # with open (FILEPATH, 'wt') as fich:
        #     for prod in produtos:
        #         fich.write(f"{prod.id},{prod.nome},{prod.tipo},{prod.quantidade},{prod.preco}\n")
        rem_produto(FILEPATH, iden)
        exibe_msg(f"Produto com o codigo {iden} removido")
        print()
        pause()
    else:
        exibe_msg(f"Não foi encontrado produto com o codigo {iden}")
        print()
        pause()    

def exec_guardar():
    id_fich = []
    actualizar_produtos(FILEPATH, produtos, id_fich)
    exibe_msg("Catalogo Guardado.")
    print()
    pause()            
    
def exec_terminar():
    sys.exit(0)
        
def main():
    global produtos
    produtos = le_produtos(FILEPATH)
    exec_menu()
    
    
    # produtos = CatalogoProdutos()
    # produtos.append(Produto(30987, "pão de milho", "AL", 10, dec('1')))
    # produtos.append(Produto(30098, "leite mimosa", "AL",25, dec('2')))
    # produtos.append(Produto(21109,"fairy","DL",20,dec('3')))
        
    # produtos = le_produtos('python\\produtos.csv')
    
    # produtos._dump()
    # print(produtos)
    
    # print("-------------------------------")
    
    # produto = ProdutoEspecial.from_csv("21112,sonasol,DL,25,2.5")
    # print(produto)
    #le_produtos('produtos.csv')
    #le_produtos('python\\produtos.csv')
    #le_produtos('C:\\Users\\João\\Documents\\Programação\\GitProgs\\TIS09788\\python\\produtos.csv')

    # print(prod1)
    # print(prod2)

    # try:
    #     Produto(39877, "leite mimosa", "AL", 1, dec(0))
    # except ValueError as ex:
    #     print("ATENÇÃO: Produto inválido!")
    #     print(ex)
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