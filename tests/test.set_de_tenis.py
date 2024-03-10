import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.set_de_tenis import evaluar

class TestSetDeTenis(unittest.TestCase):
    def test_aun_no_termina(self):
        valor_esperado = "Aún no termina"
        valor_actual = evaluar(4, 5)
        self.assertEqual(valor_esperado, valor_actual)

    def gano_a(self):
        valor_esperado = "Ganó A"
        valor_actual = evaluar(6, 4)
        self.assertEqual(valor_esperado, valor_actual)

    def gano_b(self):
        valor_esperado = "Ganó B"
        valor_actual = evaluar(5, 7)
        self.assertEqual(valor_esperado, valor_actual)

        def invalido(self):
        valor_esperado = "Inválido"
        valor_actual = evaluar(2, 7)
        self.assertEqual(valor_esperado, valor_actual)

if __name__ == '__main__':
    unittest.main()
