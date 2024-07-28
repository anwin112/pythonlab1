#Write a python program to print patterns given below:


letters=['A','B','C','D','E']
n=5
for i in range(0,5):
    print(" " * (n-i), end=" ")
    for j in range(-1,i):
        print(letters[j+1],' ',end="")
    print()
print()

for i in range(1,6):
    for j in range(0,i):
        print("*",end="")
    print()