"""Tests unitaires pour le module calculator"""
import unittest
import sys
import os
# Ajouter le dossier parent au path pour importer src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calucator import add, subtract, multiply, divide, power, modulo


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






if __name__ == '__main__':
    unittest.main()
