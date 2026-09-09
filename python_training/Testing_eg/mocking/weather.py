import requests

class WeatherService:
    def __init__(self, api_url):
        # URL base del servizio meteo (in test verrà simulato con mock).
        self.api_url = api_url

    def ottieni_dati_previsioni(self, city: str):
       # Costruzione URL completa solo a scopo di debug/stampa.
       complete_url = f"{self.api_url}/weather/?city={city}"
       print("Curl - " + complete_url)
       # Chiamata HTTP reale: nei test viene intercettata con patch su requests.get.
       response = requests.get(f"{self.api_url}/weather?city={city}")
       print(response)
       if response.status_code == 200:
            # Il servizio risponde correttamente: ritorniamo il JSON.
            return response.json()
       else:
            # Caso di errore HTTP: solleviamo eccezione per gestirla a livello superiore.
            raise ValueError

    def calcolo_temperatura_media(self, city: str):
        # Riusa il metodo precedente per ottenere i dati e calcola la media.
        data = self.ottieni_dati_previsioni(city)
        temperature = data["temperatures"]
        return sum(temperature) / len(temperature)
