import math
# Question 1:
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15
print(f"{celsius}°C is equal to {fahrenheit}°F and {kelvin}K.")

# Question 2:
a = float(input("Enter first polynomial coefficient: "))
b = float(input("Enter second polynomial coefficient: "))
c = float(input("Enter third polynomial coefficient: "))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    print(f"Two real roots: {root1} and {root2}.")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"One real root: {root}.")
else:
    print("Imaginary roots.")

# Question 3:
side1 = float(input("Enter first side length of the triangle: "))
side2 = float(input("Enter second side length of the triangle: "))
side3 = float(input("Enter third side length of the triangle: "))
sides = [side1, side2, side3]
largest_side = max(sides)
sides.remove(largest_side)
if (sides[0] + sides[1] > largest_side):
    print("The lengths can form a triangle.")
else:
    print("The lengths can't form a triangle.")

# Question 4:
sideLen = float(input("Enter the side length of the pentagon: "))
area = (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * sideLen**2
print(f"The area of the pentagon is: {area} square units.")

# Question 5:
n = int(input("Enter n wanted fibonacci term: "))
golden_ratio = (math.sqrt(5) + 1) / 2
res = ((2 + golden_ratio) / 5) * (golden_ratio ** n) + ((3 - golden_ratio) / 5) * (golden_ratio ** -n)
print(f"The {n}th term (zero-indexed) of the Fibonacci sequence is: {res}.")