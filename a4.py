def generate_fibonacci(n_terms):
    """
    Generates a Fibonacci sequence up to a given number of terms.
    """
    
    n1, n2 = 0, 1
    count = 0

    if n_terms <= 0:
        print("Please enter a positive integer.")
        return
    elif n_terms == 1:
        print(f"Fibonacci sequence up to {n_terms} term:")
        print(n1)
        return
    else:
        print(f"Fibonacci sequence up to {n_terms} terms:")
        sequence = []
        while count < n_terms:
            sequence.append(n1)
            
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        return sequence



num_terms = 10

fib_sequence = generate_fibonacci(num_terms)

if fib_sequence:
    print(fib_sequence)
