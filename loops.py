count = 0

for num in range(1, 51):
    if num % 5 == 0:
      count += 1

      if num % 2 == 0:
         print(f"{num} is devisible by 5 and it's an even number")
      else:
         print(f"{num} is divisible by 5 and it's an odd number")


print(f"There are {count} numbers between 1 and 50 divisible by 5")