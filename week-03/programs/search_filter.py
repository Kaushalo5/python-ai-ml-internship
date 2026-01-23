nums = [3,9,10,13,32,43,22,68]
even_nums=[list(filter(lambda x: x%2==0, nums))]
print("Even numbers:", even_nums)
odd_nums=[list(filter(lambda x: x%2!=0, nums))]
print("Odd numbers:", odd_nums)
prime_nums = []
for num in nums:
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            prime_nums.append(num)

print("Prime numbers:", prime_nums)