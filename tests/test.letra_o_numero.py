import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.annos_bisiestos import evaluar

class TestLetraONumero(unittest.TestCase):
    def test_es_numero(self):
        valor_esperado = " Es número"
        valor_actual = evaluar('c')
        self.assertEqual(valor_esperado, valor_actual)

        def test_es_letraM(self):
            valor_esperado = " Es letra mayúscula"
        valor_actual = evaluar('A')
        self.assertEqual(valor_esperado, valor_actual)

        def test_es_letram(self):
            valor_esperado = " Es letra minúscula"
        valor_actual = evaluar('a')
        self.assertEqual(valor_esperado, valor_actual)

        def test_no_es(self):
            valor_esperado = " No es letra ni número"
        valor_actual = evaluar('=')
        self.assertEqual(valor_esperado, valor_actual)
    
    
    

if __name__ == '__main__':
    unittest.main()
