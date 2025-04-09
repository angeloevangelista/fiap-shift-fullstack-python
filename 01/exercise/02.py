import json
import requests

def get_forecast(city: str):
  params = [
    f"q={city}",
    "appid=5796abbde9106b7da4febfae8c44c232",
    "units=metric",
  ]

  formatted_params = "&".join(params)

  # q={city}&appid=5796abbde9106b7da4febfae8c44c232...

  response = requests.get(
    f"https://api.openweathermap.org/data/2.5/find?{formatted_params}",
    timeout=30,
  )

  response_data = response.json()

  # print(type(response_data))
  # print(f"list -> ")

  # lista = response_data.get("listxx", [])

  # for item in lista:
  #   print(item)

  forecast_list = response_data.get("list", [])

  if len(forecast_list) == 0:
    return None

  return forecast_list[0]

def main():
  city = input("Qual a sua cidade? ")

  forecast = get_forecast(city)
  
  if forecast == None:
    print("Infelizmente não foi possível consultar a temperatura")
    return
    
  temperature = forecast.get("main").get("temp")
  feels_like = forecast.get("main").get("feels_like")
  
  print(f"A temperatura em {city} é de {temperature} graus")
  print(f"Sensação de {feels_like} graus")

if __name__ == "__main__":
  main()
