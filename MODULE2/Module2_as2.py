#Create a list that is having 
# 10,23,4,26,4,75,24,54 values 
# and with the help of while loop, fetch
# the even numbers and print the numbers.

l=[10,23,4,26,4,75,24,54]

i=0
while i<len(l):
    if l[i]%2==0:
        print(l[i])
    i+=1  

