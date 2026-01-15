# 1. Develop a memoization decorator that caches the results of function
# calls and returns the cached result when the same inputs occur again.
# This can greatly improve the performance of recursive or
# computationally intensive functions.

def memorization(fun):
    cache ={}
    def wrapper(n):
        if n in cache :
            print("number present ")
            return cache[n]
        cache[n] = fun(n)
        print ("output not found ")
        return cache[n]
    return wrapper


@memorization
def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
        
c1 = fact(10)
print(c1)
print("############")
c1 = fact(10)
print(c1)