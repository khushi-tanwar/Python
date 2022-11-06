def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+(n-2)
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
def fibonacciAndfactorial(n):
    return [fibonacci(n),factorial(n)]
def main():
    n=int(input("Enter number:"))
    f = fibonacciAndfactorial(n)
    print(f'Term{n} of the fibonacci sequence is {f[0]}')
    print(f[1],'--Factorial')
main()
