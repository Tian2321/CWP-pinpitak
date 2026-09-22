print("Enter the first number:")
a = int(input().strip())
print("Enter the second number:")
b = int(input().strip())
result = a * b
print(f"{a} x {b} = {result}")
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")