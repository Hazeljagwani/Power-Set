input("A set with n elemants has 2^n subsets. Press ENTER ")
print(" 3 elements 2^3 =", 2**3, "subsets")
print(" mask 5 = binary", bin(5)[2:], " selects positions 0 and 2")

n = int(input("Enter a number of elements (try 4 or 5): "))
guess = input("How many subsets does a set of " + str(n) + " elements have? ")
input("Each element is in or out - 2 choices per element. Press ENTER ")
print(" ", n, "elements, subsets:", 2**n, " your guess:", guess)