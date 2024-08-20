"""
Problema 3: TRIVIA

Realiza un programa que haga preguntas sobre un tema que te apasione. Maneja 3 niveles. 
El programa avanzará a la siguiente pregunta solamente si la primera fue respondida correctamente, plantea opciones para las respuestas.


"""

pregunta1 = int(input("""
                    Cuanto es 2+2? 
                    1. 4
                    2. 5
                    3. 8
                    Elija su respuesta en el formato de el numero 1, 2 o 3: 
                      """))
if pregunta1 == 1:
    pregunta2 = int(input("""
                    Cuanto es 3+3?
                    1. 6
                    2. 7
                    3. 8
                    Elija su respuesta en el formato de el numero 1, 2 o 3: 
                          """))
    if pregunta2 == 1:
        pregunta3 = int(input("""
                    Cuanto es 7-1?
                    1. 6
                    2. 5
                    3. 4
                    Elija su respuesta en el formato de el numero 1, 2 o 3: 
                              """))
        if pregunta3 == 1:
            print("You win!")
else:
    print("You lose")
    exit()