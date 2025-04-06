def welcome():
  print("Welcome to the MacDonals!")
  print("Here is our menu:")
  print("========================")
  print("== 1.🍔 Cheeseburger ==")
  print("== 2.🍟 Fries        ==")
  print("== 3.🥤 Soda         ==")
  print("== 4.🍦 Ice Cream    ==")
  print("== 5.🍪 Cookie       ==")
  print("========================")
  print("Please order by number.")
  print("Type 'done' when you are finished.")

def get_item(item):
  if item == '1':
    return "🍔 Cheeseburger"
  elif item == '2':
    return "🍟 Fries "
  elif item == '3':
    return "🥤 Soda"
  elif item == '4':
    return "🍦 Ice Cream"
  elif item == '5':
    return "🍪 Cookie"
  else:
    return "Invalid item"
  
welcome()

option = input("\nEnter your order: ")
print(get_item(option))