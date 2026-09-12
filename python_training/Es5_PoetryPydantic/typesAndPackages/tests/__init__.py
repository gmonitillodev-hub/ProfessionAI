import unittest
import uuid

from pydantic import ValidationError
from typesandpackages.data_model import Utente,Prodotto

class TestDataModel(unittest.TestCase):
    def test_data_model(self):
        res = Utente(
            nome='giova',
            email='test@rte.copm',
            cognome='Giova',
            password=str(uuid.uuid4())
        )

        print(res)
