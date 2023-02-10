import viaturas_instrucoes as vi
                    
def main():
    carros = vi.vcv.CatalogoCarros()
    try:
        carros.append(vi.vcv.Carro("10-XY-20","Opel","Corsa XL","2019-10-15"))
        carros.append(vi.vcv.Carro("20-PQ-15","Mercedes","300SL","2017-05-31"))
        carros.append(vi.vcv.Carro("AF-58-HJ","Honda","Civic","2020-02-29"))
        carros.append(vi.vcv.Carro("AD-88-LP","Mercedes","300S","2022-01-31"))
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
    print(carros)
        
    vi.menu(carros)
    
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