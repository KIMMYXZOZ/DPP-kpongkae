A = int(input("Enter the first number:  "))
B = int(input("Enter the second number: "))

print(f"{A} x {B} = {A*B}")

if A*B >= 1:
    print("The result is positive.")
elif A*B == 0:
    print("The result is positive and negative.")
else:
    print("The result is negative.")