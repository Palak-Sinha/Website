def Binaryones(num):
    pqr = 0
    abc = 0

    while num != 0:
        if num & 1 == 1:
            pqr += 1
            abc = max(abc, pqr)
        else:
            pqr = 0
        num >>= 1

    print("Longest consecutive 1's in binary representation is:", abc)

number = int(input("Enter a number: "))
Binaryones(number)
