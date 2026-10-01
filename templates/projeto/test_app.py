import unittest

from app import total


class TestCardapio(unittest.TestCase):
    def test_total_de_varias_unidades(self):
        self.assertEqual(total(500, 3), 1500)

    def test_carrinho_vazio(self):
        self.assertEqual(total(500, 0), 0)

    def test_rejeita_valores_negativos(self):
        for preco, quantidade in [(-1, 2), (500, -1)]:
            with self.subTest(preco=preco, quantidade=quantidade):
                with self.assertRaises(ValueError):
                    total(preco, quantidade)


if __name__ == "__main__":
    unittest.main()
