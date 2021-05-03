def fibonacci(n):
   return sum_series(n)
   
def lucas(n):
    return sum_series(n,2,1)

def sum_series(n,n1=0,n2=1):
    if n < 0:
        return "negative num is not allowed"
    if n == 0:
        return n1
    elif n == 1:
        return n2  
    else:
          return sum_series(n-1,n1,n2) + sum_series(n-2,n1,n2)
   
if __name__ == "__main__":
    riddle_index = 0