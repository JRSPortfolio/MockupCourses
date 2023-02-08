import re

class Carro:
    def __init__ (self, matricula, marca, modelo, data):
        self.ValMat(matricula)
        if not marca:
            raise ValueError (f'O campo "marca" deve ser preechido.')
        if not modelo:
            raise ValueError (f'O campo "modelo" deve ser preechido.')
        self.ValData(data)
        
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.data = data
    
    def __str__ (self):
        return f"Marca : {self.marca} - Modelo: {self.modelo} - Matricula: {self.matricula} - Data: {self.data}"
    
    def ValMat(self, matricula):
        vmat = re.search("^\d\d-[A-Z]{2}-\d\d$", matricula)
        vmat2 = re.search("^[A-Z]{2}-\d\d-\d\d$", matricula)
        vmat3 = re.search("^\d\d-\d\d-[A-Z]{2}$", matricula)
        vmat4 = re.search("^[A-Z]{2}-\d\d-[A-Z]{2}$", matricula)
        # vmat = re.search("^[A-Z]{2}-\d\d-\d\d$ | ^\d\d-[A-Z]{2}-\d\d$ | ^\d\d-\d\d-[A-Z]{2}$ | ^[A-Z]{2}-\d\d-[A-Z]{2}$", matricula)
        # if not vmat:
        if not vmat and not vmat2 and not vmat3 and not vmat4:
            raise ValueError (f"{matricula=} Matricula em formato inválido")
        
    def ABis(self, ano):
        ano = float(ano)
        if ano % 4 == 0 and ano % 100 != 0:
            return True
        elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
            return True
        else:
            return False        
                
    def ValData(self, data):
        vdata = re.search("^\d\d-\d\d-\d{4}$", data)
        
        if not vdata:
            raise ValueError (f"{data=} Data em formato inválido")
        else:
            dia = int(data[0:2])
            mes = int(data[3:5])
            ano = int(data[6:])
            
            if (dia > 0 and dia <= 31) and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
                pass
            elif (dia > 0 and dia <=30) and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
                pass
            elif (dia > 0 and dia <= 29) and mes == 2:
                ab = self.ABis(ano)
                if dia <= 29 and ab == True:
                    pass
                elif dia <=28 and ab == False:
                    pass
                else:
                    raise ValueError (f"{data=} Data com parametros inválidos")
            else:
                raise ValueError (f"{data=} Data com parametros inválidos")

def main():
    try:
        carro1 = Carro("10-XY-20","Opel","Corsa XL","15-10-2019")
        carro2 = Carro("20-PQ-15","Mercedes","300SL","31-05-2017")
        carro3 = Carro("AF-58-HJ","Honda","Civic","29-02-2020")
        #carro4 = Carro("DD-FF-DD","BMW","Serie5","10-12-2018")
        #carro5 = Carro("34-84-FR","Volvo","S40","29-02-2021")
        #carro6 = Carro("PO-78-85","","i30","20-10-2022")
        #carro7 = Carro("98-DD-77","Mazda","","20-02-2019")
        #carro8 = Carro("97-DD-56","VW","Golf","125-08-2022")

        print(carro1)
        print(carro2)
        print(carro3)
        #print(carro4)
        #print(carro5)
        #print(carro6)
        #print(carro7)
        #print(carro8)
        
    except ValueError as ve:
        print("Erro de registo!")
        print(ve)
    
if __name__ == "__main__":
    main()