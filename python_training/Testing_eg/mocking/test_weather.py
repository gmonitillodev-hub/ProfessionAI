import unittest

from python_training.Testing_eg.mocking.weather import WeatherService
from unittest.mock import patch, MagicMock

def my_side_effect(city):
    # Simula risposte diverse in base alla città richiesta.
    if city == "rome":
        return {"temperatures": [10, 20, 13], "city": "rome"}
    elif city == "milan":
        return {"temperatures": [10, 20, 10], "city": "milan"}

class TestWeatherService(unittest.TestCase):
    def setUp(self):
        # Setup comune per ogni test: istanza del servizio con URL fittizio.
        self.api_url = "http://mock-api.com"
        self.weather = WeatherService(self.api_url)

    @patch('python_training.Testing_eg.mocking.weather.py.requests.get')
    def test_get_weather_data(self, mock_get: MagicMock):
        # Configuriamo il mock della chiamata HTTP come risposta di successo.
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "city": "rome",
            "temperatures": [10, 20, 13],
        }
        # Il metodo usa requests.get, ma in realtà userà il mock configurato sopra.
        data = self.weather.ottieni_dati_previsioni("rome")
        print(data)

        # Verifica contenuto della risposta elaborata.
        self.assertEqual(data["city"], "rome")
        self.assertEqual(data["temperatures"], [10, 20, 13])
        # Verifica che la chiamata HTTP sia stata fatta una sola volta con l'URL atteso.
        mock_get.assert_called_once_with(f"{self.api_url}/weather?city=rome")

    @patch.object(WeatherService, "ottieni_dati_previsioni", side_effect=lambda city: my_side_effect(city))
    def test_ottieni_predizioni(self, mock_ottieni_dati_previsioni: MagicMock):
        # Qui non testiamo la rete: mockiamo direttamente il metodo che fornisce i dati.
        response = self.weather.calcolo_temperatura_media("milan")
        print(response)

        # Controllo del calcolo media: (10 + 20 + 10) / 3.
        self.assertEqual(response, 13.333333333333334)


if __name__ == '__main__':
    unittest.main()
