groceries = []

item = ''
while item != 'quit':
    item = input("Please enter the thing to buy: ")
    groceries.append(item)

groceries.pop()
print(groceries)