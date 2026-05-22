mixed_list = [10, "Hello", True, 5.5, "Python"]

choice = input("which element you want to delete: ")

if choice == "10":
    mixed_list.remove(10)

elif choice == "Hello":
    mixed_list.remove("Hello")

elif choice == "True":
    mixed_list.remove(True)

elif choice == "5.5":
    mixed_list.remove(5.5)

elif choice == "Python":
    mixed_list.remove("Python")

else:
    print("Invalid Choice")

print(mixed_list)
