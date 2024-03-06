

def imprimir_mensaje(mensaje):
    print("\033[;34m" + mensaje)

def chequear_respuesta(pregunta):
    while True:
        respuesta = input(pregunta).lower()
        if respuesta == "si" or respuesta == "no":
            return respuesta
        else:
            print("Por favor, responde 'si' o 'no'.")

def primeros_auxilios():
    imprimir_mensaje("Primeros Auxilios\n")
    respuesta = chequear_respuesta("Responde a estímulos (si/no): ")
    if respuesta == "si":
        print("Valorar la necesidad de llevarlo al hospital más cercano.")
        quit()
    elif respuesta == "no":
        imprimir_mensaje("Abrir la vía Aérea\n")
        respuesta = chequear_respuesta("¿Respira? (si/no): ")
        if respuesta == "si":
            print("Permitirle posición de suficiente ventilación.")
            quit()
        elif respuesta == "no":
            print("Administrar 5 Ventilaciones  y llamar a la Ambulancia")

def ciclo_urgencia():
    while True:
        signos_de_vida = chequear_respuesta("¿Signos de vida? (si/no): ")
        if signos_de_vida == "si":
            print("Revaluar a la espera de la ambulancia.")
            llego_ambulancia = chequear_respuesta("¿Llegó la ambulancia? (si/no): ")
            if llego_ambulancia == "si":
                quit()
            elif llego_ambulancia == "no":
                print("")
        elif signos_de_vida == "no":
            print("Administrar Compresiones Torácicas hasta que llegue la ambulancia.")
            llego_ambulancia = chequear_respuesta("¿Llegó la ambulancia? (si/no): ")
            if llego_ambulancia == "si":
                quit()

primeros_auxilios()
ciclo_urgencia()