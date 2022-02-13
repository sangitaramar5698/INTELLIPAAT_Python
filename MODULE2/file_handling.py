#f= open("sample_file.txt",'x')
#f.close()
#instead of writing the above 2 lines,
#we can use with open as f which will help us in not writing 
#f.close every time we open the file.3
#aslo, we have to write any one type of open statement

with open("sample_file.txt",'r') as f:
    # f.write("\n1.check creation\n 2.check working")
    for l in f.readlines(): print(l,end=", ")



# with open("sample_file.txt",'a') as f:
#     f.write("\n1.check creation\n 2.check working")
