#Write a python program to print patterns given below:


letters=['A','B','C','D','E']
for i in range(0,5):
    for j in range(-1,i):
        print(letters[j+1],end="")
    print()

for i in range(1,6):
    for j in range(0,i):
        print("*",end="")
    print()