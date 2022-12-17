def calculator():
    # demande à l'utilisateur de saisir l'opération à effectuer
    operation = input("Quelle opération souhaitez-vous effectuer? (utilisez +, -, *, /) ")

    # demande à l'utilisateur de saisir les deux nombres sur lesquels l'opération doit être effectuée
    number_1 = float(input("Entrez le premier nombre: "))
    number_2 = float(input("Entrez le second nombre: "))

    # effectue l'opération en utilisant les deux nombres saisis par l'utilisateur
    if operation == "+":
        result = number_1 + number_2
        print(number_1, "+", number_2, "=", result)
    elif operation == "-":
        result = number_1 - number_2
        print(number_1, "-", number_2, "=", result)
    elif operation == "*":
        result = number_1 * number_2
        print(number_1, "*", number_2, "=", result)
    elif operation == "/":
        result = number_1 / number_2
        print(number_1, "/", number_2, "=", result)
    else:
        print("Opération non valide. Veuillez recommencer.")

# appelle la fonction calculator()
calculator()
