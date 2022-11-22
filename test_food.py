"""Module Test unitaire pour la classe Food
Les propriétés:
   . name
   . calories
   . fat (lipides)
   . carbss (glucides)
   . protein (protéines)
les valeurs associées à ces propriétés se feront sur une base de 100 grammes
**Projet réalisé par Phuc PHAM NGOC et Fanjavola RAHANTAHARIMANANA
"""
import unittest
from food import Food

class TestFood(unittest.TestCase):
    """Module test pour Food class"""
    def setUp(self) -> None:
        """Setup some objects from Food class for tests"""
        print('Setup objects Food')
        self.food1 = Food('tomate')
        print(self.food1.fat)
        self.food2 = Food('melon')
        print(self.food2.fat)
        self.food3 = Food('mayonnaise')
        print(self.food3.fat)

    def test_check_fat(self) -> bool:
        """Tests pour check_fat() de la classe Food"""
        print('Test check_fat. Si valeur plus de 0.2 --> gras!!')
        self.assertEqual(self.food1.check_fat(),True)
        self.assertEqual(self.food2.check_fat(),False)
        self.assertEqual(self.food3.check_fat(),True)

if __name__ == '__main__':
    unittest.main()