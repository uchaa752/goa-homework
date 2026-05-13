age = int(input("enter your age:"))
card = input("do you have student card")

if age < 18 or card == "yes":
    print("დანაზოგი გაქვს")

elif age >= 60 and card == "no":
    print("პენსიონერის ფასდაკლება გაქვს")

else:
    print("ფასდაკლება არ გეკუთვნის")