import unittest
from distribucion import (
    distribucion_identicos,
    distribucion_sin_vacias,
    distribucion_con_limite
)


class TestDistribucion(unittest.TestCase):

    def test_identicos(self):
        self.assertEqual(distribucion_identicos(5, 3), 21)

    def test_sin_vacias(self):
        self.assertEqual(distribucion_sin_vacias(5, 3), 6)
        self.assertEqual(distribucion_sin_vacias(2, 3), 0)

    def test_con_limite(self):
        self.assertEqual(distribucion_con_limite(5, 2, 3), 4)

    def test_errores(self):
        with self.assertRaises(ValueError):
            distribucion_identicos(-1, 3)

        with self.assertRaises(ValueError):
            distribucion_identicos(5, 0)


if __name__ == "__main__":
    unittest.main()
