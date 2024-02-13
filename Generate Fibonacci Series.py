def fibonacci(n):
    fib_sequence = [0, 1] 
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

while True:
    try:
        num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
        if num_terms <= 0:
            print("Please enter a positive integer.")
        else:
            break
    except ValueError:
        print("Please enter a valid integer.")

fib_series = fibonacci(num_terms)
print("Fibonacci Sequence:")
print(fib_series)
