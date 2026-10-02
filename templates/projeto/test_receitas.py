import unittest

from receitas import quantidade_para


class TestLivroDeReceitas(unittest.TestCase):
    def test_tres_receitas_de_pao_de_queijo(self):
        # Cada receita de pão de queijo leva 500 g de polvilho.
        self.assertEqual(quantidade_para(500, 3), 1500)

    def test_nenhuma_receita(self):
        self.assertEqual(quantidade_para(500, 0), 0)

    def test_rejeita_valores_negativos(self):
        for gramas, receitas in [(-1, 2), (500, -1)]:
            with self.subTest(gramas=gramas, receitas=receitas):
                with self.assertRaises(ValueError):
                    quantidade_para(gramas, receitas)


if __name__ == "__main__":
    unittest.main()
