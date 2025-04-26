def list_names():
  with open("nomes.txt", "r") as file:
    for line in file.readlines():
      yield line

names_generator = list_names()

for name in list_names():
  print(name)

# try:
#   print(next(names_generator))
#   print(next(names_generator))
#   print(next(names_generator))
#   print(next(names_generator))
#   print(next(names_generator))
#   print(next(names_generator))
#   print(next(names_generator))
#   print(next(names_generator))
#   print(next(names_generator))
#   print(next(names_generator))
#   print(next(names_generator))
# except StopIteration:
#   pass
