import unittest

# Importez la fonction de calculatrice de votre code
from calcu import calculer

class TestCalculatrice(unittest.TestCase):
  def test_addition(self):
    # Testons l'addition de deux nombres
    resultat = calculer(2, 3, "+")
    self.assertEqual(resultat, 5)

  def test_soustraction(self):
    # Testons la soustraction de deux nombres
    resultat = calculer(5, 3, "-")
    self.assertEqual(resultat, 2)

  def test_multiplication(self):
    # Testons la multiplication de deux nombres
    resultat = calculer(4, 5, "*")
    self.assertEqual(resultat, 20)

  def test_division(self):
    # Testons la division de deux nombres
    resultat = calculer(10, 5, "/")
    self.assertEqual(resultat, 2)

# Exécutez les tests
if __name__ == '__main__':
  unittest.main()
