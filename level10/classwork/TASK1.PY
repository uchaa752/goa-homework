password = "python123"

lives=3

usser_password=input("enter password:")

while usser_password !=password and lives !=0:
    usser_password=input("wrong,please enter password again:")

    lives-=1

if usser_password ==password and lives !=-1:
    print("Acces Garanted")   
else:
    print("Lives Expired")     



