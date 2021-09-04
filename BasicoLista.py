equipos=[]
equipo=[]
isRegTeam=True
op=0
while isRegTeam==True:
    print("1.Registrar equipo\n2.Listar Equipos\n3.Listar Equipos\n4.Salir")
    op=int(input())
    if op==1:
        equipo=[]
        codigo="E"+str(len(equipos)+1)
        nombre=input("Ingrese Nombre del Equipo : ")
        equipo=[codigo,nombre,[0,0,0,0]]
        equipos.append(equipo)
    elif op==3:
        for item in equipos:
            for i in range(0,len(item)):
                if i==0:
                    print(f"Equipo : {item[0]} {item[1]}")
                if i==2:
                    print("PJ PG PE PP TP")
                    print(f"{str(item[i][0]).zfill(2)} {str(item[i][1]).zfill(2)} {str(item[i][2]).zfill(2)} {str(item[i][3]).zfill(2)} {str(((item[i][1]*3)+(item[i][2]*1))).zfill(2)}")
    elif op==4:
        codigo=input("Ingrese el codigo del Equipo")
        for item in equipos:
            if codigo in item:
                print(f"Equipo : {item[0]} {item[1]}")
                print("PJ PG PE PP TP")
                print(f"{str(item[2][0]).zfill(2)} {str(item[2][1]).zfill(2)} {str(item[2][2]).zfill(2)} {str(item[2][3]).zfill(2)} {str(((item[2][1]*3)+(item[2][2]*1))).zfill(2)}")
    elif op==5:
        rta=input("Desea cerrar el programa S o N")
        if rta.upper()=="S":
           isRegTeam=False 
        elif rta.upper()=="N":
            isRegTeam=True
        else:
            print("Opcion no valida")
