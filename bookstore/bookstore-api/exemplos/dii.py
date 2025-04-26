from abc import ABC, abstractmethod

class BaseLogger(ABC):
  @abstractmethod
  def info(self, message):
    pass

  @abstractmethod
  def debug(self, message):
    pass

  @abstractmethod
  def error(self, message):
    pass

class MyLogger(BaseLogger):
  def info(self, message):
    print(f"INFO: {message}")

  def debug(self, message):
    print(f"DEBUG: {message}")

  def error(self, message):
    print(f"ERROR: {message}")

class MyExternalLogger(BaseLogger):
  def info(self, message):
    print(f"EXTERNAL INFO: {message}")

  def debug(self, message):
    print(f"EXTERNAL DEBUG: {message}")

  def error(self, message):
    print(f"EXTERNAL ERROR: {message}")

def calculate_grade(logger: BaseLogger, noteA, noteB):
  logger.debug(f"noteA: {noteA}")
  logger.debug(f"noteB: {noteB}")
  sum = noteA + noteB

  grade = sum / 2
  logger.debug(f"{grade} = {sum} / 2")
  return grade


myLogger = MyExternalLogger()
grade = calculate_grade(myLogger, 5, 9)

print(f"Nota final: {grade}")
