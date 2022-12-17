import unittest
from calculator import *

class TestCalculatrice(unittest.TestCase):
  def setUp(self):
    # Code à exécuter avant chaque test
    pass

  def test_addition(self):
    # Test de l'addition
    resultat = calculator.calculatrice("+", 2, 3)
    self.assertEqual(resultat, 5)

  def test_soustraction(self):
    # Test de la soustraction
    resultat = calculator.calculatrice("-", 2, 3)
    self.assertEqual(resultat, -1)

  def test_multiplication(self):
    # Test de la multiplication
    resultat = calculator.calculatrice("*", 2, 3)
    self.assertEqual(resultat, 6)

  def test_division(self):
    # Test de la division
    resultat = calculator.calculatrice("/", 4, 2)
    self.assertEqual(resultat, 2)

  def test_operation_invalide(self):
    # Test d'une opération non valide
    resultat = calculator.calculatrice("invalide", 2, 3)
    self.assertEqual(resultat, "Opération non valide")

# Exécution des tests
unittest.main()
