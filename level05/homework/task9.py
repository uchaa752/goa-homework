age=int(input("enter your age:"))
heartrate=int(input("enter your hart rate"))

if age <30 and heartrate <140:
    print("შეგიძლიათ მეტი ივარჯიშოთ")

elif age >=30 and heartrate >170:
    print("დასვენება გჭირდებათ")

else:
    print("აქტივობის დონე ნორმალურია")