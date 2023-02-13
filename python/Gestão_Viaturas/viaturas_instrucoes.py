import sys
import subprocess
#from viaturas_classes import *
from op_ficheiros import *

DEFAULT_INDENTATION = 5
            
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
    
def val_mat(matricula):
    vmat1 = r"\d\d-[A-Z]{2}-\d\d"
    vmat2 = r"[A-Z]{2}-\d\d-\d\d"
    vmat3 = r"\d\d-\d\d-[A-Z]{2}"
    vmat4 = r"[A-Z]{2}-\d\d-[A-Z]{2}"
    vmat = re.search(f"{vmat1}|{vmat2}|{vmat3}|{vmat4}", matricula)
    if not vmat:
        raise AtributoInvalido (f"{matricula=}  em formato inválido")
                             
def val_data(data):
    try:
        date.fromisoformat(data)
    except:
       raise AtributoInvalido(f"{data=} não é uma data válida")
 
def val_marca (marca):    
    if not marca:
        raise AtributoInvalido (f'O campo "marca" deve ser preechido.')
                
def val_modelo(modelo):
    if not modelo:
        raise AtributoInvalido (f'O campo "modelo" deve ser preechido.')
        
def menu(carros):
    while True:
        cls()
        exibe_msg("***********************************")
        exibe_msg("* MENU:                           *")
        exibe_msg("* 1 - Listar Viaturas             *")             
        exibe_msg("* 2 - Pesquisar Viaturas          *")
        exibe_msg("* 3 - Adicionar Viatura           *")
        exibe_msg("* 4 - Remover Viatura             *")
        exibe_msg("* 5 - Gravar Catalogo             *")
        exibe_msg("* 6 - Recarregar Catalogo         *")
        exibe_msg("* T - Terminar                    *")
        exibe_msg("***********************************")
        print()
        esc = entrada("Opção: ").strip().upper()
        match esc:    
            case '1':
                lis_viaturas(carros)
            case '2':
                pes_viaturas(carros)
            case '3':
                add_car(carros)
            case '4':
                rem_car(carros)
            case '5':
                gravar_calalogo(carros)
            case '6':
                carros = recarrega_cat(carros)
            case 'T':
                exibe_msg("A sair do programa.")
                break
            case other:
                exibe_msg("opção inválida, escolha novamente.")

def lis_viaturas(carros: CatalogoCarros):
    titulos = f"|{'Marca':^16}|{'Modelo':^20}|{'Data':^12}|{'Matricula':^14}|"
    divisor = f"|{'-' * 16}+{'-' * 20}+{'-' * 12}+{'-' * 14}|"
    exibe_msg("Lista de Viaturas:\n")
    exibe_msg(titulos)
    exibe_msg(divisor)
    
    for car in carros:
        linha = f"|{car.marca:^16}|{car.modelo:^20}|{car.data:^12}|{car.matricula:^14}|"
        exibe_msg(linha)
    print()
    pause()
    
def pes_viaturas(carros: CatalogoCarros):
    try:
        pesquisa = crit_pesquisa()
        if pesquisa:
            resultado = carros.pesquisa(pesquisa)
            if resultado:
                exibe_msg("Veiculos encontrados: ")   
                exibe_msg(f"{resultado}")
            else:
                exibe_msg("Não foram encontrados veiculos.")
    except AtributoInvalido as ai:
        exibe_msg(f"Erro de inserção: {ai}")    
    #carros.pesquisa_catalogo(pesquisa)
    print()
    pause()    
                
def crit_pesquisa():
    procura = None
    while True:
        print()
        exibe_msg("++++++++++++++++++++++++++++++++++++++++++++")
        exibe_msg("+ Qual o criterior que deseja procurar:    +")
        exibe_msg("+ 1 - Maricula                             +")
        exibe_msg("+ 2 - Marca                                +")
        exibe_msg("+ 3 - Modelo                               +")
        exibe_msg("+ 4 - Data:                                +")
        exibe_msg("+ V - Voltar ao menu anterior              +")
        exibe_msg("++++++++++++++++++++++++++++++++++++++++++++")
        print()
        esc = entrada("Opção: ").strip().upper() 
        match esc:
            case '1':
                procura = entrada("Insira a matricula: ")
                val_mat(procura)
                return procura
            case '2':
                procura = entrada("Insira a marca: ")
                val_marca(procura)
                return procura
            case '3':
                procura = entrada("Insira o modelo: ")
                val_modelo(procura)
                return procura
            case '4':
                procura = entrada("Insira a data: ")
                val_data(procura)
                return procura
            case 'V':
                exibe_msg("Voltando ao menu anterior...")
                break
            case other:
                exibe_msg("Opção inválida, escolha novamente...")
    
def add_car(carros: CatalogoCarros):
    try:   
        matricula = entrada("Insira a matricula: ")
        val_mat(matricula)
    except AtributoInvalido as ai:
        exibe_msg(ai)
        print()
        pause()
        return
    try:
        marca = entrada("Insira a marca: ")
        val_marca(marca)
    except AtributoInvalido as ai:
        exibe_msg(ai)
        print()
        pause()
        return
    try:
        modelo = entrada("Insira o modelo: ")
        val_modelo(modelo)
    except AtributoInvalido as ai:
        exibe_msg(ai)
        print()
        pause()
        return
    try:
        data = entrada("Insira a data: ")
        val_data(data)
    except AtributoInvalido as ai:
        exibe_msg(ai)
        print()
        pause()
        return

    carros.append(Carro(matricula, marca, modelo, data))
    exibe_msg("Veiculo Adicionado.")
   
    pause()
    print()
    
def rem_car(carros: CatalogoCarros):
    remover = entrada("Insira a matricula do veiculo a remover: ")
    try:    
        val_mat(remover)
        if remover in carros.valores_carros:
            carros.valores_carros.pop(remover)
            exibe_msg(f"Veiculo com a matricula {remover} removido.")
        else:
            exibe_msg(f"Não foi encontrado veiculo com matricula {remover}")    
    except AtributoInvalido as ai:
        exibe_msg(f"Erro de formato: {ai}")
    pause()
    print() 

def gravar_calalogo(carros: CatalogoCarros):
    gravar_carros(carros, FILEPATH)
    exibe_msg("Catalogo Actualizado.")
    print()
    pause()
    
def recarrega_cat(carros: CatalogoCarros):
    carros = ler_carros(FILEPATH)
    exibe_msg("Catalogo Atualizado.")
    print()
    pause()
    return carros

    