x=20
if x < 20:
    print("x is less than 20")
elif(x==20):
    print("x is 20")
    if(x%2==0):
        print("x is div by 2")
        for i in range(1,5):
            x=x+i
            print(x,"in each ",i)

else:
    print("x is greater than or equal to 20")
print("the final x is ",x)
