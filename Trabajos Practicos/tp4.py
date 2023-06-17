def analizar(cadena, aceptar):
    print("+--------------+-------------+-------------+-----------------+")
    print("| Estado Act.  |  Carácter   |   Símbolo   |  Estado Sig.    |")
    print("+--------------+-------------+-------------+-----------------+")
    error = ""
    estado = "q1"
    cadena += "B"
    for caracter in cadena:
        if caracter not in caracteres:
            error = f"\nEl carácter '{caracter}' no es válido."
            break
        nuevo_estado = transiciones.get((estado, caracter))
        if nuevo_estado is None:
            break
        print(f"|    {estado}     |   {caracter}    |    {caracter}    |     {nuevo_estado}      |")
        print("+--------------+-------------+-------------+-----------------+")
        estado = nuevo_estado
    if estado == aceptar:
        print("|          ¡Cadena Válida!           |")
        print("+--------------+-------------+-------------+-----------------+\n")
    else:
        print("|         ¡Cadena NO Válida!         |")
        print("+--------------+-------------+-------------+-----------------+\n")
        print(error)

while True:
    print("\nPor favor, ingrese el número del Autómata que desea ejecutar:")
    print("1. Autómata del Ejercicio 2-A")
    print("2. Autómata del Ejercicio 2-B")
    print("3. Autómata del Ejercicio 2-C")
    automata = input().replace(" ", "")

    if automata not in ["1", "2", "3"]:
        print(f"\n'{automata}' es una opción inválida. Ingrese 1, 2 o 3.")
        continue

    if automata == "1":
        cadena = input(f"\nEligió el Autómata '{automata}'. Ingrese una cadena para su análisis: ")
        caracteres = {"x", "y", "B"}
        transiciones = {("q1", "x"): "q2", ("q2", "x"): "q2", ("q2", "y"): "q2", ("q2", "B"): "q3"}
        analizar(cadena, "q3")
        input("\nPresione [ENTER] para continuar o cierre la terminal para finalizar.")

    elif automata == "2":
        cadena = input(f"\nEligió el Autómata '{automata}'. Ingrese una cadena para su análisis: ")
        caracteres = {"A", "C", "B"}
        transiciones = {("q1", "A"): "q2", ("q1", "C"): "q1", ("q1", "B"): "q3", ("q2", "C"): "q1"}
        analizar(cadena, "q3")
        input("\nPresione [ENTER] para continuar o cierre la terminal para finalizar.")

    elif automata == "3":
        cadena = input(f"\nEligió el Autómata '{automata}'. Ingrese una cadena para su análisis: ")
        caracteres = {"a", "b", "B"}
        transiciones = {("q1", "a"): "q5", ("q1", "b"): "q2", ("q2", "a"): "q5", ("q2", "b"): "q3",
                        ("q3", "a"): "q4", ("q3", "b"): "q3", ("q4", "a"): "q5", ("q4", "b"): "q3",
                        ("q5", "a"): "q5", ("q5", "b"): "q3", ("q5", "B"): "q6"
                        }
        analizar(cadena, "q6")
        input("\nPresione [ENTER] para continuar o cierre la terminal para finalizar.")