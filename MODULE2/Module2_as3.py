#Create an array that is having 
# user defined inputs and with the
#  help of for loop, fetch all the prime
# numbers and print the numbers.
l=[]
number= int(input("enter the total elements you want to store in array"))
for x in range(0,number):
    l.append(int(input("enter the value")))
print(l)  

for x in range(0,len(l)):
    count=0
    for j in range(1,l[x]+1):
        if(l[x]%j==0):
            count+=1
    if(count==2):
        print(l[x],"is prime number")

