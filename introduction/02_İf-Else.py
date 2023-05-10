İf-Else
Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird


n = int(input()) operators
if 1 <= n <= 100:
    if n % 2 == 0:
        if 2 <= n <= 5:
            print("Not Weird")
        if  6<=n<=20:
            print(" Weird")
        if n > 20:
            print("Not Weird")
    else:
        print("Weird")
else:
    print("Not Weird")