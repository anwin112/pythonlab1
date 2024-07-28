#(5) Write a Python program to print all the even numbers and their squares
#within the given range.
#(a) range(1,50)
#(b) range(1,100)

#a
print("range(1,50)")
for i in range(1,50):
    if(i%2==0):
        print(i,"square is ",i*i)
#b
print("range(1,100)")
for i in range(1,100):
    if(i%2==0):
        print(i,"square is ",i*i)