def benchmark(function):
  def inner_function():
    print("TIME FROM INNER")
    function()
  
  return inner_function

@benchmark
def dizer_ola():
  print("Olá")

if __name__ == "__main__":
  dizer_ola()
