#declare array and print
 
nums=[1,2,3,4]
print(nums)

nums.append(5)

print(nums)
nums.pop()
print(nums)
nums.pop(0)

x=nums.append(1)#append will add a value at the end of the list
print(nums)
nums.insert(0,1)#to insert value at a particular position in a list
print(nums)
#nums.append(0,10) append can take only one value which should be added in the end of the list
print(nums)

x=nums.pop(0)
for x in nums:
    print(x)
    print("Done ")

print(nums)
x=5
for x in nums:
    print(x)
    print("done")
#********************************************

#tuples
nums=1,2,3,4
print(nums)

#dictionary

sal={1:"a",2:"b"}
print(sal)
sal[1]="check"
print(sal)

del sal[1]
print(sal)
#sal.append[1:"check2"]
print(sal)


for key,vals in sal.items():
    print(key,vals)

l=[]
for x in range(0,10):
    l.append(x+2)
print("the list values are ",l,"and the final x value is",x)



#how the above lines are comprehenced inside a single line is as follow

l=[x*2 for x in range(1,11)]

print(l)

s={x*3 for x in range(1,11)}#s is set here
print(s)
d={x:x*4 for x in range(1,11)}#d is dictionary here
print("dictionary values are",d)

t=  tuple (x for x in range(1,11))
print("the tuple values are ",t)
