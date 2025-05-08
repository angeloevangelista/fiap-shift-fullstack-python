from pytest import fixture
from fastapi.testclient import TestClient

from main import get_message, sum_numbers, app

test_client = TestClient(app)

def test_get_message():
  expected = "Hello, World"

  result = get_message()

  assert expected == result

def test_health_check():
  response = test_client.get("/api/health")
  response_data = response.json()

  assert response.status_code == 200
  assert "healthy" in response_data
  assert response_data.get("healthy") == True

@fixture
def numbers():
  try:
    yield [1, 2, 3, 4]
  finally:
    pass

def test_sum_numbers(numbers):
  expected = 10
  result = sum_numbers(numbers)

  assert result == expected
