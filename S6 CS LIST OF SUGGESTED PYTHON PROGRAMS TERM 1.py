
# 1
print("\nHello World")

# 2
print("\nSK" + " " + "ABDUR" + " " + "REHMAN")

# 3
a = 45
b = 3
c = 45 // 3
d = 45 % 3
print(f"\nFloor Division of {a} and {b} is {c}.")
print(f"Modulus of {a} and {b} is {d}.")

# 4
a = int(input("\nEnter your age: "))
if a < 0:
    print("Invalid age!")
elif a >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote!")

# 5
# square
side = int(input("\nEnter side of square: "))
area = side * side
print(f"The area of square is {area}.")
# rectangle
length = int(input("\nEnter length of rectangle: "))
breadth = int(input("Enter breadth of rectangle: "))
area = length * breadth
print(f"The area of rectangle is {area}.")
# triangle
base = int(input("\nEnter base of triangle: "))
height = int(input("Enter height of triangle: "))
area = 0.5 * base* height
print(f"The area of triangle is {area}.")
# circle
radius = int(input("\nEnter the radius of circle: "))
area = 3.14 * radius * radius
print(f"The area of circle is {area}.")

# 6
a = int(input("\nEnter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
D = b**2 - 4*a*c
alpha = ((-b) + (D)**(1/2))/(2*a)
beta = ((-b) - (D)**(1/2))/(2*a)
if D == 0:
    print("The roots are Real and Equal.")
    print(f"The roots are {alpha} and {beta}.")
elif D > 0:
    print("The roots are Real and Unequal.")
    print(f"The roots are {alpha} and {beta}.")
else:
    print("No real roots exist.")

# 7
year = int(input("\nEnter year: "))
if year % 4 == 0:
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is NOT a Leap Year.")

# 8
first_side = int(input("\nEnter the first side of the triangle: "))
second_side = int(input("Enter the second side of the triangle: "))
third_side = int(input("Enter the third side of the triangle: "))
if first_side <= 0 or second_side <= 0 or third_side <= 0:
    print("It is NOT a valid Triangle based on sides.")
else:
    if first_side == second_side == third_side == 0:
        print(f"{first_side}, {second_side} and {third_side} form an Equilateral Triangle.")
    elif (first_side == 0) or (second_side == 0) or (third_side == 0):
        print(f"{first_side}, {second_side} and {third_side} form an Isosceles Triangle.")
    else:
        print(f"{first_side}, {second_side} and {third_side} form a Scalene Triangle.")
first_angle = int(input("\nEnter the first angle of the triangle: "))
second_angle = int(input("Enter the second angle of the triangle: "))
third_angle = int(input("Enter the third angle of the triangle: "))
if (first_angle + second_angle + third_angle) != 180 or first_angle <= 0 or second_angle <= 0 or third_angle <= 0:
    print("It is NOT a valid Triangle based on angles.")
else:
    if 90 in (first_angle, second_angle, third_angle):
        print(f"{first_angle}, {second_angle} and {third_angle} form a Right Angled Triangle.")
    elif first_angle < 90 and second_angle < 90 and third_angle < 90:
        print(f"{first_angle}, {second_angle} and {third_angle} form an Acute Angled Triangle.")
    else:
        print(f"{first_angle}, {second_angle} and {third_angle} form a Obtuse Angled Triangle.")

# 9
string = input("\nEnter a string: ")
print("Code"+"With"+"Harry")
print("Hello" * 3)
print("hell" in string)
print(string[6])
print(len(string))
print(string.capitalize())
print(string.title())
print(string.lower())
print(string.upper())
print(string.count(" "))
print(string.find("hell"))
print(string.index("World"))
print(string.endswith(" "))
print(string.startswith("hell"))
print("123Python".isalnum())
print("Python".isalpha())
print("123".isdigit())
print("python".islower())
print("PYTHON".isupper())
print("  ".isspace())
print(string.lstrip())
print(string.rstrip())
print(string.strip())
print(string.replace("amazing", "wonderful"))
print(" ".join(["Python", "is", "Fun"]))
print(string.partition("Python"))
print(string.split())

# 10

import math
x = float(input("\nEnter x: "))
y = float(input("Enter y: "))
a = math.pi
b = math.e
c = math.sqrt(x)
d = math.ceil(x)
e = math.floor(x)
f = math.fabs(x)
g = math.sin(x)
h = math.cos(x)
i = math.tan(x)
j = math.pow(x, y)

print(f"pi: {a}")
print(f"e: {b}")
print(f"sqrt: {c}")
print(f"ceil: {d}")
print(f"floor: {e}")
print(f"fabs: {f}")
print(f"sin: {g}")
print(f"cos: {h}")
print(f"tan: {i}")
print(f"pow: {j}")

# 11
import random
a = random.random()
b = random.randint(1,6)
c = random.randrange(8,18)
d = random.randrange(20,80,10)
print(f"\n{a}")
print(b)
print(c)
print(d)

# 12
income = int(input("\nEnter your Income: "))
if income < 0:
    print(f"Rs.({income}) is NOT a valid Income.")
elif income <= 250000:
    print(f"Tax rate for Rs.{income} is Nil.")
elif 250001 <= income <= 500000:
    print(f"Tax rate for Rs.{income} is 5%.")
elif 500001 <= income <= 750000:
    print(f"Tax rate for Rs.{income} is 10%.")
elif 750001 <= income <= 1000000:
    print(f"Tax rate for Rs.{income} is 15%.")
elif 1000001 <= income <= 1250000:
    print(f"Tax rate for Rs.{income} is 20%.")
elif 1250001 <= income <= 1500000:
    print(f"Tax rate for Rs.{income} is 25%.")
else:
    print(f"Tax rate for Rs.{income} is 30%")    

# 13
previous_reading = float(input("\nEnter the previous reading: "))
present_reading = float(input("Enter the present reading: "))

units_consumed = present_reading - previous_reading

if units_consumed < 0:
    print("Invalid readings! (Present reading > previous reading)")
else:
    total_bill = 0
    if units_consumed > 1200:
        total_bill += (units_consumed - 1200) * 7.75
        units_consumed = 1200
    if units_consumed > 800:
        total_bill += (units_consumed - 800) * 7.0
        units_consumed = 800
    if units_consumed > 400:
        total_bill += (units_consumed - 400) * 6.5
        units_consumed = 400
    if units_consumed > 200:
        total_bill += (units_consumed - 200) * 4.5
        units_consumed = 200
    print(f"Total Electric Bill: ₹{total_bill}")

# 14
first_n = int(input("\nEnter the First n: "))
second_n = int(input("Enter the Second n: "))
print(f"The EVEN nS between {first_n} and {second_n} are :- ")
if first_n <= second_n:
    for sub_ns in range(first_n, second_n + 1):
        if sub_ns % 2 == 0:
            print(sub_ns)
else:
    print("Invalid Readings! (First n is greater than Second n)")

# 15
n = int(input("\nEnter n: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# 16
n = int(input("\nEnter n: "))
a = 0
b = 1

if n <= 0:
    print("Invalid input! (Enter a natural n)")
else:
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# 17
n = int(input("\nEnter a n: "))
print(f"The FACTORS of {n} are:-")
for i in range(1, n+1):
    if (n % i) == 0:
        print(i)

# 18
n = int(input("\nEnter a n: "))
sum = 0
print(f"The SUM OF ALL THE PROPER FACTORS of {n} are:-")
for i in range(1, n+1):
    if (n % i) == 0:
        sum += i
print(sum)

# 19
n = int(input("\nEnter a n: "))
sum = 0
for i in range(1, n):
    if (n % i) == 0:
        sum += i  
if n == sum:
    print(f"{n} is a PERFECT n.")
else:
    print(f"{n} is not a PERFECT n.")

# 20
first_n = int(input("\nEnter the First n: "))
sum_first = 0
for sub_first in range (1, first_n):
    if first_n % sub_first == 0:
        sum_first += sub_first
second_n = int(input("Enter the Second n: "))
sum_second = 0
for sub_second in range (1, second_n):
    if second_n % sub_second == 0:
        sum_second += sub_second
if sum_first == second_n and sum_second == first_n:
    print(f"{first_n} and {second_n} are AMICABLE nS.")
else:
    print(f"{first_n} and {second_n} are not AMICABLE nS.")

# 21
n = int(input("\nEnter the n: "))
divs = 0
for i in range(1, n + 1):
    if n % i == 0:
        divs += 1
if divs == 2:
    print(f"{n} is a PRIME n.")
else:
    print(f"{n} is not a PRIME n.")

# 22
n = int(input("\nEnter the number of prime numbers: "))
if n <= 0:
    print(f"Invalid Reading!\n({n}) is not greater than zero.")
else:
    count = 0
    num = 2
    print(f"First {n} Prime Numbers are :-")
    while count < n:
        for i in range (2, int(num ** 0.5) + 1):
            if num % i == 0:
                num += 1
                break
        else:
            print(num)
            num += 1
            count += 1

# 23
number = int(input("\nEnter a number: "))
if number <= 0:
    print(f"Invalid Reading!\n({number}) is not greater than zero.")
else:
    num = 2
    print(f"Prime Numbers less than equals to {number} are :-")
    while num < number:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                num += 1
                break
        else:
            print(num)
            num += 1

# 24
number = int(input("\nEnter a number: "))
if number <= 0:
    print(f"Invalid Reading!\n({number}) is not greater than zero.")
else:
    num = 2
    sum = 0
    print(f"Prime Numbers less than equals to {number} are :-")
    while num < number:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
            sum += num
        num += 1
print(f"\nSum of Prime Numbers less than equals to {number} is {sum}.")

# 25
first_number = int(input("\nEnter the First Number: "))
second_number = int(input("Enter the Second Number: "))
x = first_number
y = second_number
if x <= 0 or y <= 0:
    print("Invalid Reading!\nBoth the numbers should be Positive.")
else:
    while y != 0:
        x, y = y, (x % y)
    print(f"HCF/GCD of {first_number} and {second_number} is {x}.")

# 26
first_number = int(input("\nEnter the First Number: "))
second_number = int(input("Enter the Second Number: "))
x, y = first_number, second_number
if x <= 0 or y <= 0:
    print("Invalid Reading!\nBoth the numbers should be Positive.")
else:
    while y!= 0:
        x, y = y, (x % y)
    if x == 1:    
        print(f"{first_number} and {second_number} are Co-Prime.")
    else:
        print(f"{first_number} and {second_number} are not Co-Prime.")
        print(f"{x} is common in both {first_number} and {second_number}.")

# 27
first_number = int(input("\nEnter the First Number: "))
second_number = int(input("Enter the Second Number: "))
x, y = first_number, second_number
if x <= 0 or y <= 0:
    print(f"Invalid Reading!\nBoth the numbers should be Positive.")
else:
    while y != 0:
        x, y = y, (x % y)
    HCF = x
LCM = int((first_number * second_number)/HCF)
print(f"LCM of {first_number} and {second_number} is {LCM}.")

# 28
number = int(input("\nEnter a number: "))
x = number
if x <= 0:
    print(f"Invalid Reading!\nBoth the numbers should be Positive.")
else:
    sum = 0
    while x > 0:
        digits = x % 10
        sum += digits
        x //= 10
print(f"Sum of the Digits of {number} is {sum}.")

# 29
number = int(input("\nEnter a number: "))
x = number
if x <= 0:
    print(f"Invalid Reading!\nBoth the numbers should be Positive.")
else:
    sum = 0
    while x > 0:
        digits = x % 10
        sum += digits ** (len(str(number)))
        x //= 10
if number == sum:
    print(f"{number} is an ARMSTRONG NUMBER.")
else:
    print(f"{number} is not an ARMSTRONG NUMBER.")

# 30
number = input("\nEnter a number: ")
reverse = number[::-1]
print(f"{number} after REVERSING its Digits is {reverse}.")

# 31
number = input("\nEnter a number: ")
reverse = number[::-1]
if number == reverse:
    print(f"{number} is a Palindrome.")
else:
    print(f"{number} is not a Palindrome.")

# 32
amount = int(input("\nEnter the amount of money: "))
print(f"Minimum Currency Notes required to have Rs.{amount} are :-")
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
for note in notes:
    if amount >= note:
        count = amount // note
        amount %= note
        if count > 0:
            print(f"{note}: {count}")

# 33

# With a limit of just 3 numbers
first_number = int(input("\nEnter the First Number: "))
second_number = int(input("Enter the Second Number: "))
third_number = int(input("Enter the Third Number: "))
number = [first_number, second_number, third_number]
number.sort()
print(f"Ascending Order is {number}.")
number.sort(reverse=True)
print(f"Descending Order is {number}.")

# Without any limit (infinite numbers)
number = []
n = int(input("Enter no of numbers to be inputted: "))
for i in range(1, n + 1):
    num = int(input("Enter a number: "))
    number.append(num)
number.sort()
print(f"Ascending Order is {number}.")
number.sort(reverse=True)
print(f"Descending Order is {number}.")

# 34
number = int(input("\nEnter a number: "))
if number < 0:
    print("Invalid Reading!\nEnter a positive number only.")
elif number == 0:
    print("The Factorial of 0 is 1.")
else:
    factorial = 1
    for i in range (1, (number + 1)):
        factorial *= i
    print(f"The Factorial of {number} is {factorial}.")

# 35
x = float(input("\nEnter a floating number (x): "))
n = int(input("Enter a natural number (n): "))
if n <= 0:
    print(f"Invalid Reading!\nThe value ({n}) should be greater than 0.")
else:
    sum_series = 0
    for i in range(n + 1):
        if i % 2 == 0:
            sum_series += x**i
        else:
            sum_series -= x**i
    print(f"Series: (1 - {int(x)} + {int(x)}² - {int(x)}³ + .... + {int(x)}^{n}),")
    print(f"The sum of this series is {sum_series}.")

# 36
x = float(input("\nEnter a floating number (x): "))
n = int(input("Enter a natural number (n): "))
if n <= 0:
    print(f"Invalid Reading!\nThe value ({n}) should be greater than 0.")
else:
    sum_series = 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        term = (x**i)/factorial
        if i % 2 == 0:
            sum_series += term
        else:
            sum_series -= term
    print(f"Series: (1 - {int(x)}/1! + {int(x)}²/2! - {int(x)}³/3! + .... + {int(x)}^{n}/{n}!),")
    print(f"The sum of this series is {sum_series}.")

# 37
x = float(input("\nEnter a floating number (x): "))
n = int(input("Enter a natural number (n): "))
if n <= 0:
    print(f"Invalid Reading!\nThe value ({n}) should be greater than 0.")
else:
    sum_series = 1
    for i in range(1, n + 1):
        factorial = 1
        power = 2 * i
        for j in range(1, power + 1):
            factorial *= j
        term = (x**power)/factorial
        if i % 2 == 0:
            sum_series += term
        else:
            sum_series -= term
    print(f"Series: (1 - {int(x)}²/2! + {int(x)}⁴/4! - {int(x)}⁶/6! + .... + {int(x)}^{2*n}/{2*n}!),")
    print(f"The sum of this series is {sum_series}.")

# 38
x = float(input("\nEnter a floating number (x): "))
n = int(input("Enter a natural number (n): "))
if n <= 0:
    print(f"Invalid Reading!\nThe value ({n}) should be greater than 0.")
else:
    sum_series = 1
    for i in range(1, n + 1):
        factorial = 1
        power = 2*i + 1
        for j in range(1, power + 1):
            factorial *= j
        term = (x**power)/factorial
        if i % 2 == 0:
            sum_series += term
        else:
            sum_series -= term
    print(f"Series: (1 - {int(x)}³/3! + {int(x)}⁵/5! - {int(x)}⁷/7! + .... + {int(x)}^{2*n + 1}/{2*n+1}!),")
    print(f"The sum of this series is {sum_series}.")

# 39 (a)
number = int(input("\nEnter a natural number (n): "))
for i in range(1, number + 1):
    print("*" * i)

# 39 (b)
number = int(input("\nEnter a natural number (n): "))
for i in range(1, number + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# 40 (a)
number = int(input("\nEnter a natural number (n): "))
for i in range(0,number):
    print(' '*(number-i-1), '*'*(2*i+1))

# 40 (b)
number = int(input("\nEnter a natural number (n): "))
for i in range(1,number+1):
    print(' '*(number-i), end='')
    for j in range(1,i+1):
        print(j, end='')
    for k in range(i-1,0,-1):
        print(k, end='')
    print()

# 41
print()
List = [10, 20, 30, 40, 50, 70, 60, 70]
print(f"Original List :- {List}")
List.append(80) # Appends a value at the last.
print(f"List after append() :- {List}")
List.insert(0,0) # Inserts a value at a specified index.
print(f"List after insert() :- {List}")
P = List.pop(3) # Pops a value from a specfied index.
print(f"Popped Item :- {P}")
print(f"List after pop() :- {List}")
List.remove(70) # Removes a value entered but only the first occurence of that value.
print(f"List after remove() :- {List}")

# 42
numbers = []
while True:
    print("""
1. Create a list List
2. Append a Number
3. Display the List
4. Search for a Number.
5. Modify a Number.
6. Delete a Number.
7. Exit Program """)
    choice = int(input("Enter your choice out of 1 to 7: "))
    if choice == 1:
        n = int(input("Enter the no. of elements to add: "))
        for i in range(n):
            num = int(input("Enter element: "))
            numbers.append(num)
        print(f"List created Successfully!")
        print(f"List :- {numbers}")
    elif choice == 2:
        n = int(input("Enter the no. of elements to append: "))
        for i in range(n):
            num = int(input("Enter element: "))
            numbers.append(num)
        print("List has been successfully appended!")
        print(f"List :- {numbers}")
    elif choice == 3:
        print(f"Displaying the Original List :- {numbers}")
    elif choice == 4:
        n = int(input("Enter the number to search for: "))
        if n in numbers:
            print(f"({n}) is there in the Original List.")
        else:
            print(f"({n}) is not there in the Original List.")
    elif choice == 5:
        num = int(input("Enter the number to modify: "))
        if num in numbers:
            n = int(input(f"Enter the   list number to replace with {num}: "))
            numbers[numbers.index(num)] = n
            print(f"{num} has been replaced with {n}.")
            print(f"List :- {numbers}")
        else:
            print(f"Invalid Reading!\n({num}) is not in the Original List.")
    elif choice == 6:
        num = int(input("Enter the number to delete: "))
        if num in numbers:
            numbers.remove(num)
            print(f"{num} has been deleted from the Original List.")
            print(f"List :- {numbers}")
        else:
            print(f"Invalid Reading!\n({num}) is not in the Original List.")
    elif choice == 7:
        print("Exiting the Program...\nGoodBye!")
        break
    else:
        print("Invalid Choice!")
        print(f"({choice}) does not lie between 1 and 7. ")
        print("Please Try Again...")

# 43
import statistics
numbers = []
number = int(input("\nEnter the no of elements to add: "))
for i in range(number):
    num = int(input("Enter the number to append: "))
    numbers.append(num)
a = statistics.mean(numbers)
b = statistics.median(numbers)
c = statistics.mode(numbers)
print(f"Mean :- {a}")
print(f"Median :- {b}")
print(f"Mode :- {c}")

# 44
STACK = []
while True:
    print("""
1. PUSH
2. POP
3. DISPLAY
4. EXIT""")
    choice = int(input("Enter your choice out of 1 to 4: "))
    if choice == 1:
        n = int(input("Enter number of names to add: "))
        for i in range(n):
            names = input("Enter names to PUSH: ")
            STACK.append(names)
        print("Names PUSHED Successfully!")
        print(f"Updated STACK: {STACK}")
    elif choice == 2:
        if STACK == []:
            print("The STACK is already Empty.")
        else:
            len = len(STACK)
            print(f"Length of the STACK is {len}.")
            index = int(input(f"Enter the index you want to POP out of 0 to {(len - 1)}: "))
            if 0 < index <= (len - 1):
                original_STACK = STACK.copy()
                P = STACK.pop(index)
                print(f"'{P}' has been POPPED out of {original_STACK}.")
                print(f"Updated STACK: {STACK}")
            else:
                print("Invalid Index!\nTry again...")
    elif choice == 3:
        print(f"Displaying the names stored in 'STACK' :- {STACK}")
    elif choice == 4:
        print("Exiting the Program...\nGoodBye!")
        break
    else:
        print("Invalid Choice!")
        print(f"({choice}) does not lie between 1 and 4. ")
        print("Please Try Again...")

# 45
ARR = [2,4,1,3,6,1,3,5,1,4]
while True:
    print("""
1:COUNT AND DISPLAY EVEN AND ODD
2:SUM
3:MAXIMUM
4:MINIMUM
5:AVERAGE
6:DECREASE EVEN INCREASE ODD
7:CREATE EVEN AND ODD LIST
8:INTERCHANGE
9:QUIT""")
    choice = int(input("\nEnter your choice out of 1 to 9: "))
    if choice == 1:
        Even_List = []
        Odd_List = []
        Even_Counter = 0
        Odd_Counter = 0
        for i in ARR:
            if i % 2 == 0:
                Even_Counter += 1
                Even_List.append(i)
            else:
                Odd_Counter += 1
                Odd_List.append(i)
        print(f"There are {Even_Counter} Even Numbers in ARR.")
        print(f"Even Numbers are: {Even_List} ")
        print(f"There are {Odd_Counter} Odd Numbers in ARR.")
        print(f"Odd Numbers are: {Odd_List}")
    elif choice == 2:
        sum = 0
        for i in ARR:
            sum += i
        print(f"Sum of the List {ARR} is {sum}.")
    elif choice == 3:
        max = max(ARR)
        print(f"Maximum Value stored in {ARR} is {max}.")
    elif choice == 4:
        min = min(ARR)
        print(f"Minimum Value stored in {ARR} is {min}.")
    elif choice == 5:
        avg = sum/len(ARR)
        print(f"Average of the no's stored in {ARR} is {avg}.")
    elif choice == 6:
        length = len(ARR)
        for i in range(length):
            if ARR[i] % 2 == 0:
                ARR[i] -= 1
            else:
                ARR[i] += 1
        print(f"Increase of all odd no.s by 1 & decrease of all even no.s by 1 done successfully.")
        print(f"Updated List :- {ARR}")
    elif choice == 7:
        Even_List = []
        Odd_List = []
        Even_Counter = 0
        Odd_Counter = 0
        for i in ARR:
            if i % 2 == 0:
                Even_Counter += 1
                Even_List.append(i)
            else:
                Odd_Counter += 1
                Odd_List.append(i)
        print(f"There are {Even_Counter} Even Numbers in ARR.")
        print(f"Even Numbers are: {Even_List} ")
        print(f"There are {Odd_Counter} Odd Numbers in ARR.")
        print(f"Odd Numbers are: {Odd_List}")
    elif choice == 8:
        length = len(ARR)
        for i in range(1, length-1, 2):
            ARR[i], ARR[i+1] = ARR[i+1], ARR[i]
        print(f"Interchanged ARR: {ARR}")
    elif choice == 9:
        print("Exiting the Program...\nGoodBye!")
        break
    else:
        print("Invalid Choice!")
        print(f"({choice}) does not lie between 1 and 9. ")
        print("Please Try Again...")

# 46
STACK = ()
while True:
    print("""
1: PUSH
2: POP
3: DISPLAY
4: QUIT""")
    choice = int(input("Enter your choice out of 1 to 4: "))
    if choice == 1:
        names = input("Enter the name to PUSH: ")
        STACK = tuple(list(STACK) + [names])
        print(f"{names} has been successfully added.")
    elif choice == 2:
        list_stack = list(STACK)
        p = list_stack.pop()
        updated_stack = tuple(list_stack)
        print(f"{p} has been popped from {STACK}.")
    elif choice == 3:
        print(f"Displaying STACK :- {updated_stack}")
    elif choice == 4:
        print("Exiting the Program...\nGoodBye!")
        break
    else:
        print("Invalid Choice!")
        print(f"({choice}) does not lie between 1 and 4. ")
        print("Please Try Again...")

#  OR

STACK = ()
while True:
    print("""
1: PUSH (Add a name at the end)
2: POP (Remove the last name)
3: DISPLAY (Show all names)
4: EXIT (Quit the program)""")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        n = int(input("Enter the no of names to POP: "))
        for i in range (n):
            name = input("Enter the name to add to STACK: ")
            STACK = STACK + (name,)
            print(f"'{name}' has been added to the STACK.")
    elif choice == 2:
        if len(STACK) == 0:
            print("STACK is empty. Cannot POP.")
        else:
            name = STACK[-1]
            STACK = STACK[:-1]
            print(f"'{name}' has been removed from the STACK.")
    elif choice == 3:
        if len(STACK) == 0:
            print("STACK is empty.")
        else:
            print("STACK contains the following names:")
            print(", ".join(STACK))
    elif choice == 4:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

# 47
STACK = ()
while True:
    print(""" 
1: PUSH (Add a number at the TOP)
2: POP (Remove the number from the TOP)
3: DISPLAY (Show all numbers in the stack)
4: QUIT (Exit the program)""")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        number = int(input("Enter the number to PUSH at the TOP: "))
        STACK = tuple([number] + list(STACK))
        print(f"{number} has been successfully added to the stack.")
    elif choice == 2:
        if len(STACK) == 0:
            print("STACK is empty. Cannot POP.")
        else:
            list_stack = list(STACK)
            popped_number = list_stack.pop(0)
            STACK = tuple(list_stack)
            print(f"{popped_number} has been removed from the stack.")
    elif choice == 3:
        if len(STACK) == 0:
            print("STACK is empty.")
        else:
            print(f"Displaying STACK: {STACK}")
    elif choice == 4:
        print("Exiting the Program...\nGoodBye!")
        break
    else:
        print("Invalid Choice!")
        print(f"({choice}) does not lie between 1 and 4. \nPlease Try Again...")

# OR 

STACK = ()
while True:
    print("""
1: PUSH (Add a number at the top)
2: POP (Remove the number from the top)
3: DISPLAY (Show all numbers)
4: EXIT (Quit the program)
""")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        n = int(input("Enter the number of elements to PUSH at the top: "))
        for i in range(n):
            number = int(input("Enter the number to PUSH at the top: "))
            STACK = (number,) + STACK
            print(f"{number} has been added to the STACK.")
    elif choice == 2:
        if len(STACK) == 0:
            print("STACK is empty. Cannot POP.")
        else:
            number = STACK[0]
            STACK = STACK[1:]
            print(f"{number} has been removed from the STACK.")
    elif choice == 3:
        if len(STACK) == 0:
            print("STACK is empty.")
        else:
            print("STACK contains the following numbers:")
            print(", ".join(map(str, STACK)))
    elif choice == 4:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

# 48
ARR = (2,4,1,3,6,1,3,5,1,4)
while True:
    print("""
1:COUNT AND DISPLAY EVEN AND ODD
2:SUM
3:MAXIMUM
4:MINIMUM
5:AVERAGE
6:DECREASE EVEN INCREASE ODD
7:CREATE EVEN AND ODD TUPLE
8:INTERCHANGE
9:QUIT""")
    choice = int(input("\nEnter your choice out of 1 to 9: "))
    if choice == 1:
        Even_Tuple = ()
        Odd_Tuple = ()
        Even_Counter = 0
        Odd_Counter = 0
        for i in ARR:
            if i % 2 == 0:
                Even_Counter += 1
                Even_Tuple += (i,)
            else:
                Odd_Counter += 1
                Odd_Tuple += (i,)        
        print(f"There are {Even_Counter} Even Numbers in ARR.")
        print(f"Even Numbers are: {Even_Tuple} ")
        print(f"There are {Odd_Counter} Odd Numbers in ARR.")
        print(f"Odd Numbers are: {Odd_Tuple}")
    elif choice == 2:
        sum = sum(ARR)
        print(f"Sum of the Tuple {ARR} is {sum}.")
    elif choice == 3:
        max = max(ARR)
        print(f"Maximum Value stored in {ARR} is {max}.")
    elif choice == 4:
        min = min(ARR)
        print(f"Minimum Value stored in {ARR} is {min}.")
    elif choice == 5:
        avg = sum/len(ARR)
        print(f"Average of the no's stored in {ARR} is {avg}.")
    elif choice == 6:
        length = len(ARR)
        ARR_list = list(ARR)
        for i in range(length):
            if ARR_list[i] % 2 == 0:
                ARR_list[i] -= 1
            else:
                ARR_list[i] += 1
        ARR = tuple(ARR_list)
        print(f"Increase of all odd no.s by 1 & decrease of all even no.s by 1 done successfully.")
        print(f"Updated Tuple :- {ARR}")
    elif choice == 7:
        Even_Tuple = ()
        Odd_Tuple = ()
        Even_Counter = 0
        Odd_Counter = 0
        for i in ARR:
            if i % 2 == 0:
                Even_Counter += 1
                Even_Tuple += (i,)
            else:
                Odd_Counter += 1
                Odd_Tuple += (i,)  
        print(f"There are {Even_Counter} Even Numbers in ARR.")
        print(f"Even Numbers are: {Even_Tuple} ")
        print(f"There are {Odd_Counter} Odd Numbers in ARR.")
        print(f"Odd Numbers are: {Odd_Tuple}")
    elif choice == 8:
        length = len(ARR)
        ARR_list = list(ARR)  
        for i in range(0, length-1, 2):  
            ARR_list[i], ARR_list[i+1] = ARR_list[i+1], ARR_list[i]
        ARR = tuple(ARR_list)
        print(f"Interchanged ARR: {ARR}")
    elif choice == 9:
        print("Exiting the Program...\nGoodBye!")
        break
    else:
        print("Invalid Choice!")
        print(f"({choice}) does not lie between 1 and 9. ")
        print("Please Try Again...")

# 49
RESULT = {}
while True:
    print("""
1: PUSH (Add Students)
2: POP (Remove a Student)
3: DISPLAY (Show all Students)
4: AVERAGE (Average Marks scored by all Students)
5: QUIT (Quit the Program)""")
    choice = int(input("Enter your choice (1-5): "))
    if choice == 1:
        n = int(input("Enter no of elements to PUSH: "))
        for i in range(1,n+1):
            print(f"Add details of Student {i}: ")
            RollNo = int(input("Enter RollNo: "))
            if RollNo in RESULT:
                print("Roll Number already included.")
            else:
                Marks = float(input("Enter Marks: "))
                RESULT[RollNo] = Marks
        print(f"RESULT :- {RESULT} ")
    elif choice == 2:
        delete = int(input("Enter the Roll Number to delete: "))
        if delete in RESULT:
            del RESULT[delete]
        else:
            print(f"There isn't any Roll No. like ({delete}).")
        print(f"RESULT :- {RESULT} ")
    elif choice == 3:
        print(f"Displaying RESULT :- {RESULT}")
    elif choice == 4:
        marks = RESULT.values()
        Average = sum(marks)/len(RESULT)
        print(f"Average Marks of all the students are {Average}.")
    elif choice == 5:
        print("Exiting the Program...\nGoodBye!")
        break
    else:
        print("Invalid Choice!")
        print(f"({choice}) does not lie between 1 and 5. ")
        print("Please Try Again...")

# 50
DIRECTORY = {}
while True:
    print("""
1: PUSH (Add an Entry)
2: SEARCH (Search for a Person)
3: MODIFY - NAME (Modify an entered Name by Phone Number)
4: MODIFY - PHONENO (Modify an entered Phone Number by Name)
5: DISPLAY (Display all Peoples)
6: QUIT (Quit the Program)""")
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        n = int(input("Enter no of elements to PUSH: "))
        for i in range(1,n+1):
            print(f"Add details of Person {i}: ")
            PhoneNo = input("Enter Phone Number: ")
            if PhoneNo in DIRECTORY:
                print("Phone Number already included.")
            else:
                Names = input("Enter Names: ")
                DIRECTORY[PhoneNo] = Names
        print(f"DIRECTORY :- {DIRECTORY} ")
    elif choice == '2':
        search = input("Enter the Phone Number to Search: ")
        if len(search) == 10: 
            if search in DIRECTORY: 
                print(f"Phone Number ({search}) is already in the Directory with Name: {DIRECTORY[search]}.")
            else:
                print(f"Phone Number ({search}) is not in the directory.")
        else:
            print("Invalid Phone Number! Ensure it is a 10-digit numeric value.")
    elif choice == '3':
        phone = input("Enter the Phone Number of the Name to Modify: ")
        length = len(phone)
        if length == 10:
            if phone in DIRECTORY:
                New_Name = input("Enter the New Name to replace: ")
                DIRECTORY[phone] = New_Name
                print(f"Phone Number ({phone}) updated with the New Name ({New_Name}).")
            else:
                print(f"Phone Number ({phone}) is not in the Directory.")
        else:
            print(f"Invalid Number!\nEnter correct Phone Number of 10 digits.")
    elif choice == '4':
        name = input("Enter the Name of the Phone Number to modify: ")
        phone_found = None
        for PhoneNo, Names in DIRECTORY.items():
            if Names == name:
                phone_found = PhoneNo
        if phone_found:
            New_Phone = input("Enter the New Phone to modify:  ")
            DIRECTORY[New_Phone] = DIRECTORY.pop(phone_found)
            print("Successfully modified the Phone Number by a name.") # nizo academy, let's see
    elif choice == '5':
        print(f"Displaying DIRECTORY :- {DIRECTORY}")
    elif choice == '6':
        print("Exiting the Program...\nGoodBye!")
        break
    else:
        print("Invalid Choice!")
        print(f"({choice}) does not lie between 1 and 6. ")
        print("Please Try Again...")

# 51
sentence = input("Enter the sentence: ")
frequency = {}
print("Character Frequency of the sentence: ")
for character in sentence.upper():
    if character not in frequency:
        frequency [character] = 1
    else:
        frequency [character] += 1
for character in frequency:
    print(f" {character} : {frequency[character]}")
words = 0
list_words = sentence.split()
print(f"Total Number of words in the sentence - {len(list_words)}")
digits = 0
lower_case = 0
upper_case = 0
special_characters = 0
for character in sentence:
    if character.isdigit():
        digits += 1
    elif character.islower():
        lower_case += 1
    elif character.isupper():
        upper_case += 1
    else:
        special_characters += 1
print(f"Total Number of Digits in the sentence - {digits}")
print(f"Total Number of Lower Case Alphabets in the sentence - {lower_case}")
print(f"Total Number of Upper Case Alphabets in the sentence - {upper_case}")
print(f"Total Number of Specil Characters in the sentence - {special_characters}")

# 52

# A
string = input("Enter a string: ")
for i in range(1, len(string) + 1):
    print(string[:i])

# B
string = input("Enter a string: ")
for i in range(1, len(string) + 1):
    print(" " * (len(string) - i) + string[:i])

# 53
name = input("Enter a name: ").strip()
initials = ""
for i in range(len(name)):
    if i == 0 or name[i - 1] == " ":
        initials += name[i].upper() + "."
print(f"Initials of {name} - {initials}")

# 54