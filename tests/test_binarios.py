import unittest
from binarios import (
    total_cadenas,
    exactamente_k_unos,
    a_lo_mas_k_unos,
    al_menos_k_unos,
    igual_ceros_unos
)


class TestBinarios(unittest.TestCase):

    def test_total_cadenas(self):
        self.assertEqual(total_cadenas(3), 8)
        self.assertEqual(total_cadenas(0), 1)

    def test_exactamente_k_unos(self):
        self.assertEqual(exactamente_k_unos(5, 2), 10)
        self.assertEqual(exactamente_k_unos(4, 0), 1)

    def test_a_lo_mas_k_unos(self):
        self.assertEqual(a_lo_mas_k_unos(4, 2), 11)

    def test_al_menos_k_unos(self):
        self.assertEqual(al_menos_k_unos(4, 2), 11)

    def test_igual_ceros_unos(self):
        self.assertEqual(igual_ceros_unos(4), 6)
        self.assertEqual(igual_ceros_unos(3), 0)

    def test_errores(self):
        with self.assertRaises(ValueError):
            total_cadenas(-1)

        with self.assertRaises(ValueError):
            exactamente_k_unos(5, 6)


if __name__ == "__main__":
    unittest.main()
