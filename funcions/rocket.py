"""
def distance_to_miles(distance):
  return distance / 1.609

answer = distance_to_miles(10000)
print(answer)"
"""
"""
def add(x, y):
  answer = x + y

print(add(5, 3))"
"""
"""
def add(a, b):
  answer = a + b

print(add(5, 3))

def subtract(a, b):
  answer = a - b

print(subtract(5, 3))

def multiply(a, b):
  answer = a * b

print(multiply(5, 3))

def divide(a, b):
  answer = a / b

print(divide(5, 3))

def exp(a, b):
  answer = a ** b

print(exp(5, 3))
"""
"""
stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(i):
  return stock_prices[i-1]  # Ajuste para usar días 1-20 en lugar de índices 0-19

def max_price(a, b):
  mx = 0
  for i in range(a, b + 1):  # Ajuste para usar días 1-20 en lugar de índices 0-19
    if stock_prices[i] > mx:
      mx = stock_prices[i]
  return mx

def min_price(a, b):
  mn = price_at(a)
  for i in range(a, b + 1):  # Ajuste para usar días 1-20 en lugar de índices 0-19
    if stock_prices[i] < mn:
      mn = stock_prices[i]
  return mn

# Pruebas de las funciones
print("Pruebas de funciones de precios de acciones:\n")
print(f"Precio en el día 10: {price_at(10)}")
print(f"Precio máximo entre los días 5 y 15: {max_price(5, 15)}")
print(f"Precio mínimo entre los días 1 y 10: {min_price(1, 10)}")
"""



