import triqui as tr

# 1. Mostrar mensaje de bienvenida

tr.printIntro("intro.txt")

turn ="" # Indica quién tiene el turno para jugar, el usuario o la computadora.
while True:

    # 2. Crear el tablero
    # 3. El usuario debe seleccionar la marca
    # 4. Quién va primero el usuario o la computadora?

    print(turn + ' va primero.')

    jugando = True # El juego ha iniciado

    while jugando:
        if turn == 'Usuario': # 5. Turno del usuario

            # a. Mostrar tablero
            # b. Pedir jugada al usuario
            # c. Actualizar el tablero

            # d. Verificar si el usuario ha ganado el juego.
            #    Si si, mostrar tablero, mostrar mensaje de felicitación y terminar el juego.

            # e. Verificar si hay empate.
            #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.

            # f. Si el usuario no ha ganado y no hay empate, la computadora
            #    toma el siguiente turno

            turn = 'Computadora'

        else: # 6. Turno de la computadora.

            # a. Computadora hace jugada.
            # b. Actualizar el tablero.

            # c. Verificar si la computadora ha ganado el juego.
            #    Si si, mostrar tablero, mostrar mensaje indicando al usuario que ha perdido y terminar el juego.

            # d. Verificar si hay empate.
            #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.

            # f. Si la computadora no ha ganado y no hay empate, el usuario
            #    toma el siguiente turno.

            turn = 'Usuario'

    # 7. Preguntar si el usuario quiere jugar una vez mas
    #    Si no, finalizar el programa.
