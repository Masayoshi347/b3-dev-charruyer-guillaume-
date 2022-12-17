# Définition de la fonction calculatrice
def calculatrice():
  # Boucle de calcul
  while True:
    # Demande de l'opération à réaliser
    operation = input("Quelle opération souhaitez-vous réaliser (+, -, *, /) ? ")

    # Si l'opération est "fin", on quitte la boucle
    if operation == "fin":
      break

    # Demande des nombres
    nb1 = float(input("Entrez le premier nombre : "))
    nb2 = float(input("Entrez le deuxième nombre : "))

    # Calcul et affichage du résultat
    if operation == "+":
      resultat = nb1 + nb2
      print(nb1, "+", nb2, "=", resultat)
    elif operation == "-":
      resultat = nb1 - nb2
      print(nb1, "-", nb2, "=", resultat)
    elif operation == "*":
      resultat = nb1 * nb2
      print(nb1, "*", nb2, "=", resultat)
    elif operation == "/":
      resultat = nb1 / nb2
      print(nb1, "/", nb2, "=", resultat)
    else:
      print("Opération non valide")

# Appel de la fonction calculatrice
calculatrice()

