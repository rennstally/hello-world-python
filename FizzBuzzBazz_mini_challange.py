for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0 and num & 7 == 0:
        print(f"{num} FizzBuzzBazz")
    elif num % 3 == 0 and num % 5 == 0:
        print(f"{num} FizzBuzz")
    elif num % 3 == 0:
        print(f"{num} Fizz")
    elif num % 5 == 0:
        print(f"{num} Buzz")
    elif num % 7 == 0:
        print(f"{num} Bazz")
    else:
        print(num)

