bandas=[]


#Construyendo la interfaz
print("***Altavoz Es tu Voz***")
print("***********************")

opcion=100
while(opcion!=5):
    print("1. Registrar Banda")
    print("2. Buscar información de una Banda")
    print("3. Agenda del Evento")
    print("4. MOdificar una Banda")
    print("5. Salir")

    opcion=int(input("Digita una opción: "))

    if opcion==1:
        banda={}
        #Creando los datos del diccionario
        banda["id"]=int(input("Digita el id: "))
        banda["nombre"]=input("Nombre del Banda: ")
        banda["genero"]=input("Genero: ")
        banda["clasificacion"]=input("Clasificación: ")
        banda["tiempo"]=int(input("Tiempo: "))
        banda["costo"]=int(input("Costo: ($) "))
        
        #Agregando un diccionario a una lista
        bandas.append(banda)

    elif opcion==2:
        bandabuscada=input("Digita el nombre de la banda que estas buscando: ")
        for bandAuxiliar in bandas:
            if bandAuxiliar["nombre"]==bandabuscada:
                #como lo encontre muestro los datos de bandAuxiliar
                print(f"id:{bandAuxiliar["id"]} --- nombre: {bandAuxiliar["nombre"]}")
            else:
                print("parce siga buscando.....")
    elif opcion==3:

        print(bandas)
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    else:
        pass

1
