import os
import requests
import dotenv

dotenv.load_dotenv()

def get_holidays(country, year):
  api_key = os.getenv("HOLIDAY_API_KEY")

  url = f"https://holidayapi.com/v1/holidays?key={api_key}&country={country}&year={year}"

  response = requests.request("GET", url, timeout=15)
  response_data = response.json()
  return response_data["holidays"]

def main():
  """shut it"""
  year = 2024
  count_to_print = 10

  holidays = get_holidays("BR", year)

  print(f"Primeiros {count_to_print} feriados de {year}:")
  for holiday in holidays[0:count_to_print]:
    print(f" - {holiday.get('date')} | {holiday.get('name')}")

if __name__ == "__main__":
  main()
