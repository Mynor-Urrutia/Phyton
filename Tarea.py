carnets=[]
nombres=[]
secciones=[]
cursos=[]
notas=[]

cantidad=int(input("Ingrese la cantidad de alumnos a registrar: "))
for x in range(cantidad):
    carnet=input("\nIngrese No. de Carné del Alumno # "+str(x+1)+" : ")
    carnets.append(carnet)
    nombre = input("Ingrese Nombre del Alumno: ")
    nombres.append(nombre)
    seccion = input("Ingrese la sección del Alumno: ")
    secciones.append(seccion)
    curso = input("Curso asignado del Alumno: ")
    cursos.append(curso)
    nota = int(input("Ingrese nota Final del Alumno: "))
    notas.append(nota)

#Se muestran los registros ordenados por pantalla del total de datos ingresados por el usuario
print(' {:<30} {:<22} {:<23} {:<33} {:<10} '.format("\n\nCODIGO","NOMBRE","SECCION","CURSO_ASIGNADO","NOTA:"))
for x in range(cantidad):
    print(' {:<21} {:<30} {:<15} {:<40} {:<5} '.format(carnets[x],nombres[x],secciones[x],cursos[x],notas[x]))

#Se solicita el valor de busqueda para los registros y se realiza la comparacion en las listas para encontrarlo
busqueda=input("\nIndique el dato que desea buscar en los registros: ")
if busqueda in carnets:
    print("El dato se encuentra registrado: ")
    posicion=carnets.index(busqueda)
    print(' {:<30} {:<22} {:<23} {:<33} {:<10} '.format("\nCODIGO", "NOMBRE", "SECCION", "CURSO_ASIGNADO", "NOTA:"))
    print(' {:<21} {:<30} {:<15} {:<40} {:<5} '.format(carnets[posicion],nombres[posicion],secciones[posicion],cursos[posicion],notas[posicion]))
elif busqueda in nombres:
    print("El dato se encuentra registrado: ")
    posicion = nombres.index(busqueda)
    print(' {:<30} {:<22} {:<23} {:<33} {:<10} '.format("\nCODIGO", "NOMBRE", "SECCION", "CURSO_ASIGNADO", "NOTA:"))
    print(' {:<21} {:<30} {:<15} {:<40} {:<5} '.format(carnets[posicion], nombres[posicion], secciones[posicion],cursos[posicion], notas[posicion]))

#SE AGREGARON LAS BUSQUEDAS POR SECCION, CURSO Y NOTAS. UNICAMENTE COMO UNA PRUEBA, SIN EMBARGO ESTAS SOLO MUESTRAN EL PRIMER DATO ENCONTRADO EN LOS REGISTROS
#YA QUE LAS BUSQUEDAS EFICACEZ SE REALIZAN POR EL NUMERO DE carnetT O EL NOMBRE DEL ALUMNO EN ESTE CASO.
elif busqueda in secciones:
    print("El dato se encuentra registrado: ")
    posicion = secciones.index(busqueda)
    print(' {:<30} {:<22} {:<23} {:<33} {:<10} '.format("\nCODIGO", "NOMBRE", "SECCION", "CURSO_ASIGNADO", "NOTA:"))
    print(' {:<21} {:<30} {:<15} {:<40} {:<5} '.format(carnets[posicion], nombres[posicion], secciones[posicion], cursos[posicion], notas[posicion]))
elif busqueda in cursos:
    print("El dato se encuentra registrado: ")
    posicion = cursos.index(busqueda)
    print(' {:<30} {:<22} {:<23} {:<33} {:<10} '.format("\nCODIGO", "NOMBRE", "SECCION", "CURSO_ASIGNADO", "NOTA:"))
    print(' {:<21} {:<30} {:<15} {:<40} {:<5} '.format(carnets[posicion], nombres[posicion], secciones[posicion], cursos[posicion], notas[posicion]))
elif busqueda in notas:
    print("El dato se encuentra registrado: ")
    posicion = notas.index(busqueda)
    print(' {:<30} {:<22} {:<23} {:<33} {:<10} '.format("\nCODIGO", "NOMBRE", "SECCION", "CURSO_ASIGNADO", "NOTA:"))
    print(' {:<21} {:<30} {:<15} {:<40} {:<5} '.format(carnets[posicion], nombres[posicion], secciones[posicion], cursos[posicion], notas[posicion]))
else:
    print("La busqueda del dato no encontro ningun resultado en el registro. Gracias")