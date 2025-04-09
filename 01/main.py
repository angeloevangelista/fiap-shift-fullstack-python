import requests

def list_users():
  try:
    response = requests.get(
      "https://jsonplaceholder.typicode.com/users",
      timeout=30,
    )

    if response.status_code != 200:
      raise RuntimeError(
        f"Status code não esperado: {response.status_code}",
      )

    response_data = response.json()

    return response_data
  except Exception as exception:
    print(f"Oops! Deu erro: {str(exception)}")
    return []

def main():
  users = list_users()

  print("Lista de usuários")

  for user in users:
    print(f"  - {user.get('name')} ({user.get('email')})")

if __name__ == "__main__":
  main()

# Atividade
#
# - Consumir a API OpenWeatherMap (https://api.openweathermap.org/data/2.5/find?q=Aclimação&appid=5796abbde9106b7da4febfae8c44c232&units=metric)
# - Criar um app para exibir a temperatura
