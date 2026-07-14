juegos = {}
invetario = {}

def menu():
    print("====== menu principal ======")
    print("1. stock por plataforma")
    print("2. busqueda de juego por rango de precio")
    print("3. Actualizar precio de juego")
    print("4. agregar juego")
    print("5. eliminar juego")
    print("6. salir")

def leer_opcion():
    return input("ingrese una opcion (1 - 6)")
    pass 

# opcion 1 - stock de plataforma
def stock_plataforma(plataforma):
    pass

#opcion 2 busqueda de juego por rango de precio
def busqueda_precio(p_min, p_max):
    pass

#opcion 3 - actualizar precio de juego
def buscar_codigo(codigo):
    pass
def actualizar_precio(codigo, nuevo_precio):
   

# opcion 4 - agregar juegos
def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, juegos, inventario):
    pass
def validar_codigo():
    pass
def validar_titulo():
    pass
def validar_plataforma():
    pass
def validar_clasificacion():
    pass
def validar_multiplayer():
    pass
def validar_editor():
    pass
def validar_precio():
    pass
def validar_stock():
    pass

#opcion 5 - eliminar juego
def eliminar_juego(codigo):
    pass


continuar = True

def inciar_menu(juegos, inventario):
    menu()
    global continuar

while continuar:
     menu()
        opcion = leer_opcion()

        if opcion == "1":

        elif opcion == "2":
        
        elif opcion == "3":
        
        elif opcion == "4":
        
        elif opcion == "5":
        
        elif opcion == "6":
            print("Programa finalizado")
            continuar = False
        
        else:
            print("Opción inválida")
        
        print()

if __name__ == "__main__":
    iniciar_menu(juegos, inventario)
