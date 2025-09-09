
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The sum is:", num1 + num2)

def double_number(x):
    print("Double is:", x * 2)

while True:

  num =(input("Enter a number to double (or type 'q' too quit) "))

  if num.lower() == "q":
    print("Doodbye!")
    break
 
  num = int(num)
  double_number(num)
  