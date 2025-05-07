n=int(input("Enter the Number: "))
p=1

while n & 1==0:
  n>>=1
  p+=1

print("The position of the rightmost set bit in the given number is",p)



