
print("Fibbonacci sequence")

n = float(input("enter the value of n: "))

def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        # example: n = 8 then 13 + 8 = 21.
        return fib(n - 1) + fib(n - 2)
        # 8n - 1 = 7n = 13  #8n - 2 = 6n = 8
print(fib(n))