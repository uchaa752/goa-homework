products=[]

print("1 - Add")
print("2 - Remove")
print("3 - Count")

choice =input("Enter number: ")

if choice == "1":
    item = input("Enter product: ")
    products.append(item)
    print(products)

elif choice == "2":
    item = input("Enter product: ")

    if item == "Cola" or item == "Chips" or item == "Chocolate":
        products.remove(item)
        print(products)
    else:
        print("Invalid Choice")

elif choice == "3":
    print(len(products))

else:
    print("Invalid Choice")