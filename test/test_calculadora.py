# -*- coding: utf-8 -*-

import unittest
from calculadora import sumar, restar, multiplicar, dividir

class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(3, 5), 8)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)

    def test_restar(self):
        self.assertEqual(restar(10, 5), 5)
        self.assertEqual(restar(0, 5), -5)
        self.assertEqual(restar(-1, -1), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 7), 21)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(0, 100), 0)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(5, 0), "Error: División por cero")
        self.assertEqual(dividir(-10, -2), 5)

if __name__ == '__main__':
    unittest.main()

