# for loop with break and continue

nums=[x for x in range(1,11)]
for x in range(0,10):
    if (x==4): 
        continue 
    #when we put a continue, it will skip the entire part after conti in the loop and go for the next iteration
    #when we use break, it simply stop the whole loop and go for the next line of the loop
        print("hii")
    print(nums[x],end=", ")#when we give end =" ,", this will put comma at end of each line 
        

print("Done")

#***************************
#while loop
a=10
while a!=0:
    print(a,end=", ")
    a=a-1

list_var=[a for a in range(1,11)]
i=0
while i <len(list_var):
    print(i,end=", ")
    i+=1

print("")    
i=0
while i >=-10:
    print("i is ",i,"the value is ",list_var[i])
    i-=1
