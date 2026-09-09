import unittest


def calculate_sum(a, b):
    # Funzione semplice da testare: qui verifichiamo solo la logica di somma.
    return a + b


class Testing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Eseguito una sola volta prima di tutti i test della classe.
        print("Setting up...")
        pass

    @classmethod
    def tearDownClass(cls):
        # Eseguito una sola volta al termine di tutti i test.
        print("Tearing down...")

    def test_sum(self):
        # Esempio base: controllo che 2 + 3 produca il valore atteso.
        self.assertEqual(calculate_sum(2, 3), 5)


if __name__ == '__main__':
    unittest.main()
