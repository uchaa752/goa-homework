count=int(input("enter your count:"))

nums=[]

for i in range(count):
    num=int(input("enter your number:"))
    nums.append(num)

for num in nums:
    print(num)    

print(len(nums))    
    