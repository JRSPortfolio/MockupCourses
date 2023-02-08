import re
from datetime import date

class Carro:
    def __init__ (self, matricula, marca, modelo, data):
        self.ValMat(matricula)
        if not marca:
            raise AtributoInvalido (f'O campo "marca" deve ser preechido.')
        if not modelo:
            raise AtributoInvalido (f'O campo "modelo" deve ser preechido.')
        self.ValData(data)
        
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.data = data
    
    def __str__ (self):
        return f"Marca : {self.marca} - Modelo: {self.modelo} - Matricula: {self.matricula} - Data: {self.data}"
    
    def ValMat(self, matricula):
        vmat1 = r"\d\d-[A-Z]{2}-\d\d"
        vmat2 = r"[A-Z]{2}-\d\d-\d\d"
        vmat3 = r"\d\d-\d\d-[A-Z]{2}"
        vmat4 = r"[A-Z]{2}-\d\d-[A-Z]{2}"
        vmat = re.search(f"{vmat1}|{vmat2}|{vmat3}|{vmat4}", matricula)
        if not vmat:
            raise AtributoInvalido (f"{matricula=} Matricula em formato inválido")
                             
    def ValData(self, data):
        if date.fromisoformat(data):
            pass
        else:
            AtributoInvalido(f"{data} não é uma data válida")
            
class AtributoInvalido(ValueError):
    pass

class ValorDuplicado(Exception):
    pass

class CatalogoCarros:
    def __init__(self):
        self._carros = {}
        
    def append(self, car: Carro):
        if car.matricula in self._carros:
            raise ValorDuplicado(f"Já existe o carro com a matricula {car.matricula} no catalogo.")
        self._carros[car.matricula] = car    
    
    def _dump(self):
        for m, i in self._carros.items():
            print(m, i)
    
    def pes_matricula(self, mat: str):
        return {self._prods.get(mat)}
    
    def pesquisa(self, criterio):
        encontrados = CatalogoCarros()
        for car in self._carros.values():
            if criterio in car:
                encontrados.append(car)
        return encontrados
    
    def criterio(self):
        print("\tQual o criterior que deseja procurar:")
        print("\t1 - Maricula")
        print("\t2 - Marca")
        print("\t3 - Modelo")
        print("\t4 - Data:")
        print("\tV - Voltar ao menu anterior")
        esc = input("Opção: ")
        while True:    
            match esc:
                case '1':
                    procura = input("\tInsira a matricula: ")
                case '2':
                    procura = input("\tInsira a marca: ")
                case '3':
                    procura = input("\tInsira o modelo")
                case '4':
                    procura = input("\tInsira a data: ")
                case 'V':
                    print("\tVoltando ao menu anterior...")
                    break
                case other:
                    print("Opção inválida, escolha novamente...")
        return procura
                
        
                
    def __str__(self):
        class_name = self.__class__.__name__
        return f'{class_name} [Quantidade Carros: {len(self._carros)}]'
    
    def __len__(self):
        return len(self._carros)
    
    def __iter__(self):
        for car in self._carros.values():
            yield car  

def add_car(carros: CatalogoCarros):
    matricula = input("Insira a matricula: ")
    marca = input("Insira a marca: ")
    modelo = input("Insira o modelo: ")
    data = input("Insira a data: ")
    carros.append(Carro(matricula, marca, modelo, data))     

def menu(carros: CatalogoCarros):
    while True:
        print("\n\tMENU:")
        print("\t1 - Listar Viaturas")
        print("\t2 - Pesquisar Viaturas")
        print("\t3 - Adicionar Viatura")
        print("\t4 - Remover Viatura")
        print("\t5 - Actualizar Catalogo")
        print("\t6 - Recarregar Catalogo")
        print("\tT - Terminar")
        esc = input("\n\tOpção:")
        match esc:    
            case '1':
                for car in carros:
                    print(f"\t{car}")
            case '2':
                carros.pesquisa(carros.criterio)
            case '3':
                add_car(carros)     
        #     case '4':
        #     case '5':
        #     case '6':
        #     case '7':
            case 'T':
                print("\tA sair do programa.")
                break
            case other:
                print("\topção inválida, escolha novamente.")
                
    

def main():
    carros = CatalogoCarros()
    try:
        carros.append(Carro("10-XY-20","Opel","Corsa XL","2019-10-15"))
        carros.append(Carro("20-PQ-15","Mercedes","300SL","2017-05-31"))
        carros.append(Carro("AF-58-HJ","Honda","Civic","2020-02-29"))
        #carros.append(Carro("DD-FF-DD","BMW","Serie5","2018-10-12"))
        #carro5 = Carro("34-84-FR","Volvo","S40","29-02-2021")
        #carro6 = Carro("PO-78-85","","i30","20-10-2022")
        #carro7 = Carro("98-DD-77","Mazda","","20-02-2019")
        #carro8 = Carro("97-DD-56","VW","Golf","125-08-2022")

        
        # print(carro2)
        # print(carro3)
        #print(carro4)
        #print(carro5)
        #print(carro6)
        #print(carro7)
        #print(carro8)
        
    except ValueError as ve:
        print("Erro de registo!")
        print(ve)
    carros._dump()
        
    menu(carros)
    
if __name__ == "__main__":
    main()


# # matricula (str), marca, modelo, data
# 10-XY-20,Opel,Corsa XL,2019-10-15
# 20-PQ-15,Mercedes,300SL,2017-05-31

# Menu
#       1 - Listar Viaturas
#       2 - Pesquisar Viaturas
#       3 - Adicionar Viatura
#       4 - Remover Viatura
#       5 - Actualizar Catálogo
#       6 - Recarregar Catálogo
#       T - Terminar
# 
#       Opção >> 