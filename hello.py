def main():
    print("Hello World")

if __name__ == '__main__':
    main()

# Find all the factors of x using a loop and the operator %
# % means find remainder, for example 10 % 2 = 0; 10 % 3 = 1
x = 52633
for i in range(2, x):
    if x%i ==0:
        print(i)

# Write a function that prints all factors of the given parameter x
def print_factor(x):
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
            
# Write a program to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]

for x in l:
    print("Factors of", x, ":")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
    print() #the blank line between  numbers
