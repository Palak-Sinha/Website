n=int(input("Enter Number of Terms: "))
a=0
b=1
count=0
if n<=0:
  print("Please enter a positive number")
elif n==1:
  print("Fibonacci Sequence till",n,":")
  print(a)
else:
  print("FIbonacci Sequence: ")
  while count<n:
    print(a)
    sum=a+b
    a=b
    b=sum
    count+=1