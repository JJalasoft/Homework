def valid_input():
    user_input = input()
    while user_input.isnumeric() == False:
        print("Enter a valid input!")
        user_input = input()
    
    return int(user_input)

def fibo_dyn(n):
    a = 1
    b = 1
    for x in range (n-2):
        fib = a + b
        a = b
        b = fib
        
    return fib

def fibo_sequence_formula(n):
    # Golden ratio
    phi = 1.618034 
    # Sequence formula
    fibo = ((phi**n) - (1 - phi)**n) / (5**.5)
    
    return round(fibo)

print("Enter the number of the nth fibonacci sequence: ", end = ' ')
n = valid_input()
print(fibo_dyn(n))
print(fibo_sequence_formula(n))