juegos = {}
inventario = {}

def menu():
    print("====== menu principal ======")
    print("1. stock por plataforma")
    print("2. busqueda de juego por rango de precio")
    print("3. Actualizar precio de juego")
    print("4. agregar juego")
    print("5. eliminar juego")
    print("6. salir")
    print("=============================")

def leer_opcion():
    return input("Seleccione una opción (1-6): ")

#opcion 1 - stock por plataforma
def stock_plataforma(plataforma, juegos, inventario):
    plataforma = plataforma.lower()
    resultados = []
    for codigo, info in juegos.items():
        if info['plataforma'].lower() == plataforma:
            stock = inventario[codigo]['stock']
            resultados.append((info['titulo'], stock))
    
    if resultados:
        resultados.sort()
        for titulo, stock in resultados:
            print(f"el total de stock disponible de {titulo}: es {stock} unidades")
    else:
        print(f"No hay juegos para la plataforma: {plataforma}")

# opcion 2 - busqueda de juego x rango de precio
def busqueda_precio(p_min, p_max, inventario, juegos):
    resultados = []
    for codigo, info in inventario.items():
        if p_min <= info['precio'] <= p_max:
            titulo = juegos[codigo]['titulo']
            resultados.append((codigo, titulo))
    
    if resultados:
        resultados.sort()
        for codigo, titulo in resultados:
            print(f"{titulo} - {codigo}", end="  |  ")
        print()
    else:
        print(f"No hay juegos en el rango de ${p_min} a ${p_max}")

#opcion 3 - actualizar precio de juego
def buscar_codigo(codigo, juegos): 
    return codigo in juegos

def actualizar_precio(codigo, nuevo_precio, juegos, inventario):
    if buscar_codigo(codigo, juegos):
        inventario[codigo]['precio'] = nuevo_precio
        print(f"Precio actualizado exitosamente")
        return True
    else:
        print("El código no existe")
        return False

#opcion 4 - agregar juego 
def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, juegos, inventario):
    juegos[codigo] = {
        'titulo': titulo,
        'plataforma': plataforma,
        'genero': genero,
        'clasificacion': clasificacion,
        'multiplayer': multiplayer,
        'editor': editor
    }
    inventario[codigo] = {
        'precio': precio,
        'stock': stock
    }
    print(f"agregado exitosamente")

def validar_codigo(codigo, juegos):
    if codigo.strip() and codigo not in juegos:
        return True
    return False

def validar_titulo():
    titulo = input("Ingrese título del juego: ").strip()
    if titulo:
        return True, titulo
    return False, None

def validar_plataforma():
    plataforma = input("Ingrese plataforma: ").strip()
    if plataforma:
        return True, plataforma
    return False, None

def validar_genero():
    genero = input("Ingrese género: ").strip()
    if genero:
        return True, genero
    return False, None

def validar_clasificacion():
    clasificacion = input("Ingrese clasificación (E/T/M): ").upper().strip()
    if clasificacion in ['E', 'T', 'M']:
        return True, clasificacion
    return False, None

def validar_multiplayer():
    respuesta = input("¿Es multiplayer? (S/N): ").upper().strip()
    if respuesta == 'S':
        return True, True
    elif respuesta == 'N':
        return True, False
    return False, None

def validar_editor():
    editor = input("Ingrese editor: ").strip()
    if editor:
        return True, editor
    return False, None

def validar_precio():
    try:
        precio = int(input("Ingrese precio: "))
        if precio > 0:
            return True, precio
    except ValueError:
        pass
    return False, None

def validar_stock():
    try:
        stock = int(input("Ingrese stock: "))
        if stock > 0:
            return True, stock
    except ValueError:
        pass
    return False, None

#opcion 5 - eliminar juego
def eliminar_juego(codigo, juegos, inventario):
    if buscar_codigo(codigo, juegos):
        del juegos[codigo]
        del inventario[codigo]
        print(f"Juego con código {codigo} eliminado exitosamente")
        return True
    else:
        print(f"El código {codigo} no existe")
        return False

continuar = True

def iniciar_menu(juegos, inventario):
    global continuar
    while continuar:
        menu()
        opcion = leer_opcion()
        
        if opcion == '1':
            plataforma = input("Ingrese plataforma: ")
            stock_plataforma(plataforma, juegos, inventario)
        
        elif opcion == '2':
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                    busqueda_precio(p_min, p_max, inventario, juegos)
                else:
                    print("Precios inválidos")
            except ValueError:
                print("Ingrese números enteros válidos")
        
        elif opcion == '3':
            codigo = input("Ingrese código del juego: ")
            try:
                nuevo_precio = int(input("Ingrese nuevo precio: "))
                if nuevo_precio > 0:
                    actualizar_precio(codigo, nuevo_precio, juegos, inventario)
                    respuesta = input("¿Desea actualizar otro precio? (S/N): ").upper().strip()
                    while respuesta == 'S':
                        codigo = input("Ingrese código del juego: ")
                        nuevo_precio = int(input("Ingrese nuevo precio: "))
                        if nuevo_precio > 0:
                            actualizar_precio(codigo, nuevo_precio, juegos, inventario)
                            respuesta = input("¿Desea actualizar otro precio? (S/N): ").upper().strip()
                        else:
                            print("El precio debe ser mayor que cero")
                            break
                else:
                    print("El precio debe ser mayor que cero")
            except ValueError:
                print("Ingrese un número entero válido")
        
        elif opcion == '4':
            codigo = input("Ingrese código del juego: ")
            if not validar_codigo(codigo, juegos):
                print("Error: código vacío o ya existe")
                continue
            
            valido, titulo = validar_titulo()
            if not valido:
                print("Error: título inválido")
                continue
            
            valido, plataforma = validar_plataforma()
            if not valido:
                print("Error: plataforma inválida")
                continue
            
            valido, genero = validar_genero()
            if not valido:
                print("Error: género inválido")
                continue
            
            valido, clasificacion = validar_clasificacion()
            if not valido:
                print("Error: clasificación inválida (debe ser E, T o M)")
                continue
            
            valido, multiplayer = validar_multiplayer()
            if not valido:
                print("Error: ingrese S o N")
                continue
            
            valido, editor = validar_editor()
            if not valido:
                print("Error: editor inválido")
                continue
            
            valido, precio = validar_precio()
            if not valido:
                print("Error: precio inválido")
                continue
            
            valido, stock = validar_stock()
            if not valido:
                print("Error: stock inválido")
                continue
            
            agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, juegos, inventario)
        
        elif opcion == '5':
            codigo = input("Ingrese código del juego a eliminar: ")
            eliminar_juego(codigo, juegos, inventario)
        
        elif opcion == '6':
            print("Programa finalizado")
            continuar = False
        
        else:
            print("Opción inválida")
        
        print()

if __name__ == "__main__":
    iniciar_menu(juegos, inventario)

#tengan piedad, solo necesito un 4.1 :( 
