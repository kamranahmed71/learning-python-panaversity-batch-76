# Q1: Variables & Data Types

name = "Kamran Ahmed"
age = 40 
is_student = True 

print(name, age, is_student, sep=", ")
  # 1. Print each variable on a new line.
print(type(name))
print(type(age))
print(type(is_student))


# Q2: Arithmetic Operators
x = 20 
y = 6 

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Exponent:", x ** y)


# Q3: Assignment Operators
num = 10

# 1. Add 5 to num using the += operator.
num + 5
# 2. Multiply num by 2 using the *= operator.
num * 2
# 3. Subtract 4 from num using the -= operator.
num - 4
# 4. Print the final value of num.
print("Final value of num:", num)



# Q4: Comparison Operators
a = 15 
b = 12 

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)


# Q5: Logical Operators
p = True 
q = False 

print(p and q)
print(p or q)
print(not p)
print(not q)


# Q6: Real-Life Example
# The price of one notebook is 80 rupees.
# ● If you buy 7 notebooks, calculate the total price.
# ● If you have 600 rupees, check (using comparison operator) whether your money is enough to buy them or not.
# ● Print the result in a clear message.

notebook = 80
total_price = notebook * 7
money = 600

if money >= total_price:
    print("You have enough money to buy the notebooks.")
else:
    print("You do not have enough money to buy the notebooks.")



# Q7: Bonus (Optional)
# Take two numbers as input from the user.
# ● Print their sum.
# ● Print whether the first number is greater than the second number or not.


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Sum:", num1 + num2)
print("Is the first number greater than the second?", num1 > num2)
