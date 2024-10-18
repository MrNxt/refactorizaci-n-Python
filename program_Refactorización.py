def ingresar_puntuacion_y_comentario():
    """Solicita puntuación y comentario al usuario y lo guarda en el archivo."""
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdecimal():
            point = int(point)
            
            if point <= 0 or point > 5:
                print('Por favor, introduzca un valor entre el 1 y 5')
            else:
                print('Por favor, introduzca un comentario')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post} \n')
                break
        else:
            print('Por favor, introduzca la puntuación en números')

def comprobar_resultados():
    """Muestra los resultados almacenados hasta la fecha."""
    print('Resultados hasta la fecha:')
    try:
        with open("data.txt", "r") as read_file:
            data = read_file.read()
            if data:
                print(data)
            else:
                print("No hay resultados almacenados aún.")
    except FileNotFoundError:
        print("No hay resultados almacenados aún.")

def mostrar_menu():
    """Presenta el menú principal con las opciones disponibles."""
    print('Seleccione el proceso que desea aplicar')
    print('1: Ingresar puntuación y comentario')
    print('2: Comprueba los resultados obtenidos hasta ahora.')
    print('3: Finalizar')

def gestionar_seleccion():
    """Gestiona la selección del usuario y valida la entrada."""
    while True:
        mostrar_menu()
        num = input()

        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_puntuacion_y_comentario()
            elif num == 2:
                comprobar_resultados()
            elif num == 3:
                print('Finalizando')
                break
            else:
                print('Por favor, introduzca del 1 al 3')
        else:
            print('Por favor, introduzca del 1 al 3')

# Iniciar el programa
gestionar_seleccion()