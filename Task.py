def gcd(a, b):
    steps = 0
    while b != 0:
        a, b = b, a % b
        steps += 1
    return a, steps

def generate_fib_until_k_digits(k):
    fib = [1, 1]
    while len(str(fib[-1])) <= k:
        fib.append(fib[-1] + fib[-2])
    return fib

def find_worst_case_pair(k):
    fib = generate_fib_until_k_digits(k)
    for i in range(len(fib)-1):
        if len(str(fib[i])) == k and len(str(fib[i+1])) == k:
            return fib[i], fib[i+1]
    return None

def gcd_worst_case(k):
    pair = find_worst_case_pair(k)
    if pair:
        a, b = pair
        gcd_val, steps = gcd(a, b)
        print(f"Numbers = {a}, {b}")
        print(f"Steps Taken = {steps}")
        print(f"GCD = {gcd_val}")
    else:
        print(f"No consecutive Fibonacci numbers found with {k} digits.")

# Example usage:
k = int(input("Enter k (number of digits): "))
gcd_worst_case(k)