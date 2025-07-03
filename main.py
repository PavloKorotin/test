print("Hello!")

num1 = int(input("Please enter number 1: "))
num2 = int(input("Please enter number 2: "))
num3 = int(input("Please enter number 3: "))

if num1 < 0 or num2 < 0 or num3 < 0:
    print("try again")

all_num = [num1, num2, num3]
maximum = max(all_num)

print(f"Your maximum number is: {maximum}")

def calculate(num1, num2, num3, maximum):
    x = (num1 + num2 + num3) - maximum
    return x

resalt = calculate(num1, num2, num3, maximum)
print(f"Sum of numders: {resalt}")