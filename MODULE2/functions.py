def downloadFile(url):
    print("Establish Connections"+ url)
    print("Open Connection"+ url)
    print("Download Data")
    print("Connection closed"+url)
downloadFile("ftp://www.abc.org")
downloadFile("ftp://www.abc.org")
####*************
def check(x,y):
    return x*y
x=int(input("enter the value of x"))
y=int(input("enter the value of y"))
print(check(x,y))

#same above program by using lambda functions
x=lambda a,b:a*b
print(x(10,2))

def mul(c):
    return lambda a,b:a*b*c
lmbda=mul(3)
#we are assigning function to var, then passing lambda func value through that
print("lambda function is used here",lmbda(2,3))


#*****************
def createMultiplier(x):
    return lambda y:x*y

multiply=createMultiplier(10)

print(multiply(2),15)
