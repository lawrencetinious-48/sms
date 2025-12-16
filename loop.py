fruits = ["banana","apple","orange","mangoes"]
k = []
for i in fruits:
    if "s" in i:
        k.append(i)
        print(k)

count = 5
while count > 0:
    print(count)
    count -= 1

shopping_cart = ["milk", "bread", "eggs","floor"]
for items in shopping_cart:
    if items == "eggs":
        print("Eggs found! ")
        break 
    print(f"Adding {items} to the cart: ")

shopping_cart = ["milk", "bread", "eggs","floor"]
for items in shopping_cart:
    if items == "eggs":
        continue
    print(items)


number = 5

for i in range(12):
    print(f"{number} * {i} = {number * i}")

    count = 10

    for _ in range(7):
        print(f"{count} * {_} = {count * _}")