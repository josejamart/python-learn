# Cargamos el módulo unittest
import unittest
from recursive import BinarySearch


# Creamos una clase heredando de TestCase
class TestBinarySearch(unittest.TestCase):
    # Creamos una prueba para probar un valor inicial
    def test_first_middle(self):
        index = BinarySearch(4, [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(3, index)

    # Creamos una prueba para probar un valor inicial
    def test_first_lower_middle(self):
        index = BinarySearch(2, [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(1, index)

    # Creamos una prueba para probar un valor inicial
    def test_first_upper_middle(self):
        index = BinarySearch(6, [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(5, index)

    # Creamos una prueba para probar un valor inicial
    def test_initial(self):
        index = BinarySearch(1, [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(0, index)

    # Creamos una prueba para probar un valor inicial
    def test_end(self):
        index = BinarySearch(7, [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(6, index)

    # Creamos una prueba para probar un valor inicial
    def test_out_of_bounds_at_start(self):
        index = BinarySearch(-4, [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(-1, index)

    # Creamos una prueba para probar un valor inicial
    def test_out_of_bounds_at_end(self):
        index = BinarySearch(70, [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(-1, index)
