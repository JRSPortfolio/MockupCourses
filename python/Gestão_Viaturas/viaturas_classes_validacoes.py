import re
from datetime import date

class Carro:
    def __init__ (self, matricula, marca, modelo, data):
        val_mat(matricula)
        val_marca(marca)
        val_modelo(modelo)
        val_data(data)
        
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.data = data
    
    def __str__ (self):
        return f"Marca : {self.marca} - Modelo: {self.modelo} - Matricula: {self.matricula} - Data: {self.data}"
        
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
    
    # def pesquisa(self, criterio, valor):
    #     encontrados = CatalogoCarros()
    #     try:    
    #         crit = criterio()
    #         for car in self._carros.values():
    #             if crit == car.matricula or crit == car.marca or crit == car.marca or crit == car.data:
    #                 encontrados.append(car)
    #         if encontrados:
    #             print("\tVeiculos Encontrados:")        
    #             for c in encontrados:
    #                 print (f"\t{c}")
    #         else:
    #             print("\tNão foram encontrados veiculos.")        
    #     except AtributoInvalido as ai:
    #         print("Erro na pesquisa")
    #         print(ai)
            
    def pesquisa(self, criterio):
        encontrados = CatalogoCarros()
        for car in self._carros.values():
            list_cars = [car.matricula, car.marca, car.modelo, car.data]
            if criterio in list_cars:
                encontrados.append(car)
        return encontrados
    
    def pesquisa_catalogo(self, valor):
        if valor in self._carros.values():
            return True
        else:
            return False
                       
    def __str__(self):
        for car in self._carros.values():
            print(f"     {car}")
        return ''
    
    def __len__(self):
        return len(self._carros)
    
    def __iter__(self):
        for car in self._carros.values():
            yield car
    
    @property
    def valores_carros(self):
        return self._carros  

class AtributoInvalido(ValueError):
    pass

class ValorDuplicado(Exception):
    pass

def val_mat(matricula):
    vmat1 = r"\d\d-[A-Z]{2}-\d\d"
    vmat2 = r"[A-Z]{2}-\d\d-\d\d"
    vmat3 = r"\d\d-\d\d-[A-Z]{2}"
    vmat4 = r"[A-Z]{2}-\d\d-[A-Z]{2}"
    vmat = re.search(f"{vmat1}|{vmat2}|{vmat3}|{vmat4}", matricula)
    if not vmat:
        raise AtributoInvalido (f"{matricula=} Matricula em formato inválido")
                             
def val_data(data):
    if date.fromisoformat(data):
        pass
    else:
        AtributoInvalido(f"{data} não é uma data válida")
 
def val_marca (marca):    
    if not marca:
        raise AtributoInvalido (f'O campo "marca" deve ser preechido.')
                
def val_modelo(modelo):
    if not modelo:
        raise AtributoInvalido (f'O campo "modelo" deve ser preechido.')