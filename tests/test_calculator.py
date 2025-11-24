"""Tests unitaires pour le module calculator"""
import unittest
import sys
import os

# Ajouter le dossier parent au path pour importer src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator import add, subtract, multiply, divide, power


class TestCalculator(unittest.TestCase):
    """Tests pour les fonctions de la calculatrice"""

    def test_add(self):
        """Test de l'addition"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        """Test de la soustraction"""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        """Test de la multiplication"""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        """Test de la division"""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)

    def test_divide_by_zero(self):
        """Test de la division par zéro"""
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_power(self):
        """Test de la puissance"""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 2), 25)


if __name__ == '__main__':
    unittest.main()