# import json
import requests

def get_temp(cidade):
  response = requests.get(
    f"https://api.openweathermap.org/data/2.5/find?q={cidade}&appid=5796abbde9106b7da4febfae8c44c232&units=metric"
  )
  
  return response.json()

def main():
  cidade = input("Digite a cidade desejada: ")
  response_data = get_temp(cidade)
  # print(json.dumps(response_data, indent=2))
  print(response_data)
    
if __name__ == "__main__":
  main()
