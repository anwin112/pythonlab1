#(6) Write a Python program to read a four-digit number and find its
#(a) Sum of digits
#(b) Reverse

#a
a=int(input("give a 4 digit number"))
temp=a
sum=0
while(temp!=0):
    rem=temp%10
    sum+=rem
    temp=temp//10
print("sum of digits are",sum)
#b
temp=a
rev=0
while(temp!=0):
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10