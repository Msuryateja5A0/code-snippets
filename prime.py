num = 17
is_prime = True

if num <= 1:
    is_prime = False

for i in range(2, num // 2 + 1):
    if num % i == 0:
        is_prime = False
        break

if is_prime:
    print(num, "is Prime")
else:
    print(num, "is not Prime")
