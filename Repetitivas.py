# EJERCICIO 1
nombre = input("Cliente: ").strip()

while nombre == "" or not nombre.isalpha():
    print("Error: ingresa un nombre no vacio y solo con letras")
    nombre = input("Cliente: ") .strip()

cantidad_str = input("Ingresa la cantidad de productos: ").strip()

while not cantidad_str.isdigit() or int(cantidad_str) == 0:
    print("Error: ingresa un numero entero positivo mayor a cero")
    cantidad_str = input("Ingresa la cantidad de productos: ").strip

cantidad_int = int(cantidad_str)
total_sin_descuento = 0
total_con_descuento = 0.0

for i in range(1,cantidad_int+1):
    precio_str = input(f"Producto {i} - Precio: ").strip()

    while not precio_str.isdigit() or int(precio_str) <= 0:
        print("Error: el precio debe ser un entero positivo")
        precio_str = input(f"Producto {i} - Precio: ").strip()

    precio_int = int(precio_str)

    desc = input("Descuento (S/N): ").strip().lower()

    while desc != "s" and desc != "n":
        print("Error: Ingrese S para si o N para no")
        desc = input("Descuento (S/N): ").strip(). lower()

    total_sin_descuento += precio_int

    if desc == "s":
        precio_final = precio_int * 0.9
    else:
        precio_final = precio_int

    total_con_descuento += precio_final

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_int

print()
print(f"Total sin descuento: ${total_sin_descuento}")
print(f"Total con descuento: ${total_con_descuento :.2f}")
print(f"Ahorro total: ${ahorro :.2f}")
print(f"Promedio: ${promedio :.2f}")




#EJERCICIO 2

USUARIO_CORRECTO = "alumno"
CLAVE_CORRECTA = "python123"

clave_actual = CLAVE_CORRECTA

intento = 1
acceso_concedido = False

while intento <= 3 and acceso_concedido == False:
    usuario = input(f"Intento {intento}/3 - Usuario: ").strip()
    clave = input("Clave: ").strip()

    if usuario == USUARIO_CORRECTO and clave == clave_actual:
        print("Acceso concedido.")
        acceso_concedido = True
    else:
        print("Error: credenciales inválidas.")
        intento += 1

if acceso_concedido == False:
    print("Cuenta bloqueada")
else:
    seguir_menu = True

    while seguir_menu == True:
        print("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opcion_str = input("Opción: ").strip()

        while not opcion_str.isdigit():
            print("Error: ingrese un número válido.")
            opcion_str = input("Opción: ").strip()

        opcion = int(opcion_str)

        while opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            opcion_str = input("Opción: ").strip()

            while not opcion_str.isdigit():
                print("Error: ingrese un número válido.")
                opcion_str = input("Opción: ").strip()

            opcion = int(opcion_str)



        if opcion == 1:
            print("Inscripto")

        elif opcion == 2:
            cambio_exitoso = False

            while cambio_exitoso == False:
                nueva = input("Nueva clave: ").strip()

                if len(nueva) < 6:
                    print("Error: mínimo 6 caracteres.")
                else:
                    confirmacion = input("Confirmar clave: ").strip()

                    if nueva != confirmacion:
                        print("Error: las claves no coinciden.")
                    else:
                        clave_actual = nueva
                        print("Clave actualizada correctamente.")
                        cambio_exitoso = True

        elif opcion == 3:
            print("¡Paso a paso: si insistís, te sale!")

        elif opcion == 4:
            print("Sesión cerrada.")
            seguir_menu = False






#EJERCICIO 3
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Nombre del operador: ").strip()

while operador == "" or not operador.isalpha():
    print("Error: el nombre del operador debe ser no vacío y solo con letras.")
    operador = input("Nombre del operador: ").strip()

print(f"\nSistema iniciado. Operador: {operador}\n")



while opcion != 5:
    print("1) Reservar turno")
    print("2) Cancelar turno (por nombre)")
    print("3) Ver agenda del día")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")

    opcion_str = input("Opción: ").strip()


    while (not opcion_str.isdigit()) or (int(opcion_str) < 1) or (int(opcion_str) > 5):
        if not opcion_str.isdigit():
            print("Error: ingrese un número válido.")
        else:
            print("Error: opción fuera de rango (1 a 5).")
        opcion_str = input("Opción: ").strip()

    opcion = int(opcion_str)


    if opcion == 1:
        dia_str = input("Día (1=Lunes, 2=Martes): ").strip()


        while (not dia_str.isdigit()) or (int(dia_str) < 1) or (int(dia_str) > 2):
            if not dia_str.isdigit():
                print("Error: ingrese un número válido.")
            else:
                print("Error: opción fuera de rango (1 o 2).")
            dia_str = input("Día (1=Lunes, 2=Martes): ").strip()

        dia = int(dia_str)


        paciente = input("Nombre del paciente: ").strip()

        while paciente == "" or not paciente.isalpha():
            print("Error: el nombre del paciente debe ser no vacío y solo con letras.")
            paciente = input("Nombre del paciente: ").strip()


        repetido = False

        if dia == 1:
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                repetido = True
        else:
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                repetido = True

        if repetido == True:
            print("Error: ese paciente ya tiene un turno reservado en ese día.\n")
        else:
            reservado = False

            if dia == 1:
                if lunes1 == "":
                    lunes1 = paciente
                    reservado = True
                    print("Turno reservado en Lunes - Turno 1.\n")
                elif lunes2 == "":
                    lunes2 = paciente
                    reservado = True
                    print("Turno reservado en Lunes - Turno 2.\n")
                elif lunes3 == "":
                    lunes3 = paciente
                    reservado = True
                    print("Turno reservado en Lunes - Turno 3.\n")
                elif lunes4 == "":
                    lunes4 = paciente
                    reservado = True
                    print("Turno reservado en Lunes - Turno 4.\n")
            else:
                if martes1 == "":
                    martes1 = paciente
                    reservado = True
                    print("Turno reservado en Martes - Turno 1.\n")
                elif martes2 == "":
                    martes2 = paciente
                    reservado = True
                    print("Turno reservado en Martes - Turno 2.\n")
                elif martes3 == "":
                    martes3 = paciente
                    reservado = True
                    print("Turno reservado en Martes - Turno 3.\n")

            if reservado == False:
                print("No hay turnos disponibles en ese día.\n")


    elif opcion == 2:
        dia_str = input("Día (1=Lunes, 2=Martes): ").strip()

        while (not dia_str.isdigit()) or (int(dia_str) < 1) or (int(dia_str) > 2):
            if not dia_str.isdigit():
                print("Error: ingrese un número válido.")
            else:
                print("Error: opción fuera de rango (1 o 2).")
            dia_str = input("Día (1=Lunes, 2=Martes): ").strip()

        dia = int(dia_str)

        paciente = input("Nombre del paciente a cancelar: ").strip()
        while paciente == "" or not paciente.isalpha():
            print("Error: el nombre del paciente debe ser no vacío y solo con letras.")
            paciente = input("Nombre del paciente a cancelar: ").strip()


        encontrado = False

        if dia == 1:
            if lunes1 == paciente:
                lunes1 = ""
                encontrado = True
            elif lunes2 == paciente:
                lunes2 = ""
                encontrado = True
            elif lunes3 == paciente:
                lunes3 = ""
                encontrado = True
            elif lunes4 == paciente:
                lunes4 = ""
                encontrado = True
        else:
            if martes1 == paciente:
                martes1 = ""
                encontrado = True
            elif martes2 == paciente:
                martes2 = ""
                encontrado = True
            elif martes3 == paciente:
                martes3 = ""
                encontrado = True

        if encontrado == True:
            print("Turno cancelado correctamente.\n")
        else:
            print("No se encontró un turno con ese nombre en ese día.\n")


    elif opcion == 3:
        dia_str = input("Día (1=Lunes, 2=Martes): ").strip()

        while (not dia_str.isdigit()) or (int(dia_str) < 1) or (int(dia_str) > 2):
            if not dia_str.isdigit():
                print("Error: ingrese un número válido.")
            else:
                print("Error: opción fuera de rango (1 o 2).")
            dia_str = input("Día (1=Lunes, 2=Martes): ").strip()

        dia = int(dia_str)

        if dia == 1:
            print("\nAgenda del Lunes:")
            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {lunes1}")
            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {lunes2}")
            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {lunes3}")
            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print(f"Turno 4: {lunes4}")
            print()
        else:
            print("\nAgenda del Martes:")
            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {martes1}")

            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {martes2}")

            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {martes3}")
            print()


    elif opcion == 4:

        ocupados_lunes = 0
        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1

        libres_lunes = 4 - ocupados_lunes

        ocupados_martes = 0
        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1

        libres_martes = 3 - ocupados_martes

        print("\nResumen general:")
        print(f"Lunes -> Ocupados: {ocupados_lunes} | Libres: {libres_lunes}")
        print(f"Martes -> Ocupados: {ocupados_martes} | Libres: {libres_martes}")


        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes\n")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes\n")
        else:
            print("Día con más turnos: Empate\n")


    elif opcion == 5:
        print("\nSistema cerrado. ¡Hasta luego!\n")






#EJERCICIO 4

energia = 100              
tiempo = 12                  
cerraduras_abiertas = 0       
alarma = False                 
codigo_parcial = ""           

racha_forzar = 0

bloqueo = False



agente = input("Nombre del agente: ").strip()

while agente == "" or not agente.isalpha():
    print("Error: ingresá un nombre no vacío y solo con letras.")
    agente = input("Nombre del agente: ").strip()

print(f"\nBienvenido/a, agente {agente}. Comienza la misión...\n")




while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and bloqueo == False:


    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueo = True

    else:

        print("===== ESTADO =====")
        print(f"Energía: {energia}")
        print(f"Tiempo: {tiempo}")
        print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
        print(f"Alarma: {'ON' if alarma else 'OFF'}")
        print(f"Código parcial: '{codigo_parcial}' (len={len(codigo_parcial)})")
        print("==================")


        print("1) Forzar cerradura (-20 energía, -2 tiempo)")
        print("2) Hackear panel     (-10 energía, -3 tiempo)")
        print("3) Descansar         (+15 energía máx 100, -1 tiempo; si alarma ON: -10 energía extra)")

        opcion_str = input("Elegí una opción (1-3): ").strip()


        while (not opcion_str.isdigit()) or (int(opcion_str) < 1) or (int(opcion_str) > 3):
            if not opcion_str.isdigit():
                print("Error: ingresá un número válido.")
            else:
                print("Error: opción fuera de rango (1 a 3).")
            opcion_str = input("Elegí una opción (1-3): ").strip()

        opcion = int(opcion_str)



        match opcion:
            case 1:
                racha_forzar += 1

                energia -= 20
                tiempo -= 2


                if racha_forzar == 3:
                    alarma = True
                    print("\n⚠ La cerradura se trabó por forzar 3 veces seguidas.")
                    print("¡Alarma activada! No se abrió ninguna cerradura.\n")

                else:
                    if energia < 40:
                        print("\n⚠ Energía baja: hay riesgo de alarma.")
                        riesgo_str = input("Elegí un número (1-3): ").strip()

                        while (not riesgo_str.isdigit()) or (int(riesgo_str) < 1) or (int(riesgo_str) > 3):
                            print("Error: número inválido.")
                            riesgo_str = input("Elegí un número (1-3): ").strip()

                        riesgo = int(riesgo_str)

                        if riesgo == 3:
                            alarma = True
                            print(" Se activó la alarma durante el intento.\n")

                    if alarma == False and cerraduras_abiertas < 3:
                        cerraduras_abiertas += 1
                        print(" Cerradura abierta con éxito.\n")
                    else:
                        print(" No se pudo abrir la cerradura.\n")

            case 2:
                racha_forzar = 0

                energia -= 10
                tiempo -= 3

                print("\n Iniciando hackeo...")


                for paso in range(1, 5):
                    codigo_parcial += "A"
                    print(f"Paso {paso}/4... código parcial: '{codigo_parcial}'")


                if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                    cerraduras_abiertas += 1
                    print(" Código suficiente. Cerradura abierta.\n")
                else:
                    print("ℹ Hackeo finalizado.\n")

            case 3:
                racha_forzar = 0

                tiempo -= 1


                energia += 15
                if energia > 100:
                    energia = 100

                if alarma == True:
                    energia -= 10
                    print("\n Descanso con alarma ON: -10 energía extra.")
                else:
                    print("\n Descanso exitoso.")

                print(f"Energía actual: {energia}\n")

if cerraduras_abiertas == 3:
    print(" VICTORIA: ¡Abriste las 3 cerraduras!")
elif bloqueo == True:
    print(" DERROTA: sistema bloqueado por alarma.")
elif energia <= 0 or tiempo <= 0:
    print(" DERROTA: sin energía o sin tiempo.")
else:
    print("Fin del juego.")




#EJERCICIO 5
print("--- BIENVENIDO A LA ARENA ---")


nombre = input("Nombre del Gladiador: ").strip()


while nombre == "" or not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ").strip()


vida_jugador = 100          
vida_enemigo = 100          
pociones = 3                
dano_ataque_pesado = 15    
dano_enemigo = 12           
turno_gladiador = True      
print("=== INICIO DEL COMBATE ===")




while vida_jugador > 0 and vida_enemigo > 0:

    print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion_str = input("Opción: ").strip()


    while (not opcion_str.isdigit()) or (int(opcion_str) < 1) or (int(opcion_str) > 3):
        if not opcion_str.isdigit():
            print("Error: Ingrese un número válido.")
        else:
            print("Error: Opción fuera de rango (1 a 3).")
        opcion_str = input("Opción: ").strip()

    opcion = int(opcion_str)



    match opcion:
        case 1:
            dano_final = dano_ataque_pesado
            if vida_enemigo < 20:
                dano_final = dano_ataque_pesado * 1.5
                print(">> ¡Golpe Crítico!")
            vida_enemigo -= dano_final

            print(f"¡Atacaste al enemigo por {dano_final:.1f} puntos de daño!")

        case 2:

            print(">> ¡Inicias una ráfaga de golpes!")

            for _ in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")


        case 3:

            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print(">> Usaste una poción y recuperaste 30 HP.")
            else:
                print("¡No quedan pociones!")


    vida_jugador -= dano_enemigo
    print(f">> ¡El enemigo contraataca por {dano_enemigo} puntos!")

    print("=== NUEVO TURNO ===")


if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")

