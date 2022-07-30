####################----- 9. SUM OF FIRST 50 FIBONACCI SERIES----########################

def fib(n):
    if n == 1 or n == 2:
        return 1 
    else:
        return fib(n-1) + fib(n-2)
        
n = 50
x = []
for i in range(1,n+1):
    x.append(fib(i))
print(x)
