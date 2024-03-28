Number = int(input("Enter non-negative and non-zero Number: "))
count = 0
while Number != 1:
    if Number%2 == 0:
        Number = Number//2
        print(Number)
        count = count + 1
        if Number == 1:
            break
    if Number%2 == 1:
        Number = Number*3 + 1
        print(Number)
        count = count + 1
print("steps = ", count)