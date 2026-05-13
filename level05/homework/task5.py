num1 = int(input("შეიყვანე პირველი რიცხვი: "))
num2 = int(input("შეიყვანე მეორე რიცხვი: "))

if num1 > 0 and num2 > 0:
    print("ორივე დადებითია")

elif num1 > 0 or num2 > 0:
    print("მხოლოდ ერთი დადებითი რიცხვია")

else:
    print("არცერთი არ არის დადებითი")