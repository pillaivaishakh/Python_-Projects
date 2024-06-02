
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def max_marbles_in_each_row(red_marbles, green_marbles):
    # Find the greatest common divisor
    divisor = gcd(red_marbles, green_marbles)
    
    # Maximum number of marbles in each row
    max_marbles_per_row = divisor
    
    return max_marbles_per_row

if __name__ == "__main__":
    red_marbles = int(input("Enter the number of red marbles ABC has: "))
    green_marbles = int(input("Enter the number of green marbles XYZ has: "))
    
    max_marbles = max_marbles_in_each_row(red_marbles, green_marbles)
    print("Maximum number of marbles that can be arranged in each row:", max_marbles)
