import triqui as tr


# 1. Mostrar mensaje de bienvenida

tr.printIntro("intro.txt")

user = input("Ingrese su nombre: ")

# Contadores de estadísticas
wins = 0      # Victorias del usuario
losses = 0    # Derrotas del usuario (victorias de la computadora)
ties = 0      # Empates

turn = ""  # Indica quién tiene el turno para jugar, el usuario o la computadora.
while True:

    # 2. Crear el tablero
    board = "         "
    # 3. El usuario debe seleccionar la marca
    PlayerLetter = tr.inputPlayerLetter()
    # 4. Quién va primero el usuario o la computadora?
    turn = tr.whoGoesFirst()

    print(turn + " va primero.")

    jugando = True  # El juego ha iniciado

    while jugando:
        if turn == "Usuario":  # 5. Turno del usuario

            # a. Mostrar tablero
            tr.drawBoard(board)

            # b. Pedir jugada al usuario
            playerMove = tr.getPlayerMove(board)

            # c. Actualizar el tablero
            board = tr.makeMove(board, PlayerLetter[0], playerMove)
            # d. Verificar si el usuario ha ganado el juego.
            # Si si, mostrar tablero, mostrar mensaje de felicitación y terminar el juego.
            if tr.isWinner(board, PlayerLetter[0]):

                tr.drawBoard(board)
                print("¡Felicidades! ¡Has ganado el juego!")
                wins = wins + 1  # Incrementar victorias del usuario
                jugando = False
                continue

            # e. Verificar si hay empate.
            #    Si si, mostrar tablero, mostrar mensaje de empate y terminar el juego.
            if tr.isBoardFull(board):

                tr.drawBoard(board)
                print("¡Empate!")
                ties = ties + 1  # Incrementar empates
                jugando = False
                continue

            # f. Si el usuario no ha ganado y no hay empate, la computadora
            #    toma el siguiente turno

            turn = "Computadora"

        else:  # 6. Turno de la computadora.

            # a. Computadora hace jugada.
            computerMove = tr.getComputerMove(board, PlayerLetter)
            # b. Actualizar el tablero.
            board = tr.makeMove(board, PlayerLetter[1], computerMove)
            # c. Verificar si la computadora ha ganado el juego.
            #    Si si, mostrar tablero, mostrar mensaje indicando al usuario que ha perdido y terminar el juego.
            if tr.isWinner(board, PlayerLetter[1]):

                tr.drawBoard(board)
                print("¡La computadora ha ganado! ¡Has perdido el juego!")
                losses = losses + 1  # Incrementar derrotas del usuario
                jugando = False
                continue

            # d. Verificar si hay empate.
            #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.
            if tr.isBoardFull(board):

                tr.drawBoard(board)
                print("¡Empate!")
                ties = ties + 1  # Incrementar empates
                jugando = False
                continue

            # f. Si la computadora no ha ganado y no hay empate, el usuario
            #    toma el siguiente turno.

            turn = "Usuario"

    # 7. Preguntar si el usuario quiere jugar una vez mas
    #    Si no, finalizar el programa.
    playAgain = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if playAgain != "s":
        print("¡Gracias por jugar!")
        print("\n")
        # Mostrar y guardar estadísticas del juego
        tr.statsGames(wins, losses, ties, user)
        break
