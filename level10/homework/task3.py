num=int(input("enter your number:"))

i = 1

while i <= num:
    if i % 2 == 0:
        print(i, "this number is even.")
    else:
        print(i, "this number is odd.")
    i += 1