def fib(n):
    if(n<=1):
        return n
    else:    
        x=fib(n-1)+fib(n-2)
        return x

y=input()
i=1
while i<=y:
  print(fib(i))
  i+=1            