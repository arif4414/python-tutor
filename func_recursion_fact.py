

def fact_recursion(n):
    if n == 0:
        return 1
    return n * fact_recursion(n-1)


result = fact_recursion(2)
print(result)