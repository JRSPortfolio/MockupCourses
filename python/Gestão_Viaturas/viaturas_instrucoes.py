import sys
import subprocess
import viaturas_classes_validacoes as vcv 

CSV_DEFAULT_DELIM = ','
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
        
def crit_pesquisa():
    procura = None
    while True:
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
                vcv.val_mat(procura)
                break
            case '2':
                procura = entrada("Insira a marca: ")
                vcv.val_marca(procura)
                break
            case '3':
                procura = entrada("Insira o modelo: ")
                vcv.val_modelo(procura)
                break
            case '4':
                procura = entrada("Insira a data: ")
                vcv.val_data(procura)
                break
            case 'V':
                exibe_msg("Voltando ao menu anterior...")
                break
            case other:
                exibe_msg("Opção inválida, escolha novamente...")
    if procura:
        return procura
    
def add_car(carros: vcv.CatalogoCarros):
    matricula = entrada("Insira a matricula: ")
    marca = entrada("Insira a marca: ")
    modelo = entrada("Insira o modelo: ")
    data = entrada("Insira a data: ")
    try:
        carros.append(vcv.Carro(matricula, marca, modelo, data))
        exibe_msg("Veiculo Adicionado.")
    except vcv.AtributoInvalido as ai:
        exibe_msg(f"Erro de inserção: {ai}")    
    pause()
    print()
    
def rem_car(carros: vcv.CatalogoCarros):
    remover = entrada("Insira a matricula do veiculo a remover: ")
    vcv.val_mat(remover)
    if remover in carros.valores_carros:
        carros.valores_carros.pop(remover)
        exibe_msg(f"Veiculo com a matricula {remover} removido.")
    else:
        exibe_msg(f"Não foi encontrado veiculo com matricula {remover}")
    pause()
    print()     

def menu(carros: vcv.CatalogoCarros):
    while True:
        exibe_msg("***********************************")
        exibe_msg("* MENU:                           *")
        exibe_msg("* 1 - Listar Viaturas             *")             
        exibe_msg("* 2 - Pesquisar Viaturas          *")
        exibe_msg("* 3 - Adicionar Viatura           *")
        exibe_msg("* 4 - Remover Viatura             *")
        exibe_msg("* 5 - Actualizar Catalogo         *")
        exibe_msg("* 6 - Recarregar Catalogo         *")
        exibe_msg("* T - Terminar                    *")
        exibe_msg("***********************************")
        print()
        esc = entrada("Opção: ").strip().upper()
        match esc:    
            case '1':
                for car in carros:
                    exibe_msg(f"{car}")
            case '2':
                pesquisa = crit_pesquisa()
                #carros.pesquisa_catalogo(pesquisa)
                exibe_msg("Veiculos encontrados:")
                exibe_msg(f"{carros.pesquisa(pesquisa)}")
                print()
                pause()
            case '3':
                add_car(carros)
            case '4':
                rem_car(carros)
        #     case '5':
        #     case '6':
        #     case '7':
            case 'T':
                exibe_msg("A sair do programa.")
                break
            case other:
                exibe_msg("opção inválida, escolha novamente.")
                
    