n = int(input("Enter a Number: "))
flag = False
for i in range(2, n):
    if n % i == 0:
        flag = False
        break
    else:
        flag = True

if flag:
    print("Prime")
else:
    print("Not Prime")

# ! For Else Loop Used Below
# num = int(input("Enter a number: "))

# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             print(i, "times", num//i, "is", num)
#             break
#     else:
#         print(num, "is a prime number")

# else:
#     print(num, "is not a prime number")
