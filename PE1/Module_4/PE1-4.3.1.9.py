def is_prime(num):
    if num == 2:
        x = True
    else:    
        count = 1
        for i in range(2, num):
            if num % i != 0:
                count += 1
            else:
                break
        x = (num == count + 1)
    return x
    print(x)

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()