'''
Method 1
O(2^n) time | O(n) space
'''
def getNthFib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    return getNthFib(n-1) + getNthFib(n-2)

'''
Method 2 - using memoization
O(n) time | O(1) space
'''
# def getNthFib(n, memoize={1:0, 2:1}):
#     # Memoize using a dictionary
#     if n in memoize:
#         return memoize[n]
#     else:
#         memoize[n] = getNthFib(n-1, memoize) + getNthFib(n-2, memoize)
#         return memoize[n]

'''
Method 3 - approaching it from the first fibonacci number
O(n) time | O(1)
'''
# def getNthFib(n):
#     lastTwo = [0,1]
#     counter = 3
#     while counter <= n:
#         nextFib = lastTwo[0] + last[1]
#         lastTwo[0] = lastTwo[1]
#         lastTwo[1] = nextFib
#         counter += 1
#     return lastTwo[1] if n > 1 else lastTwo[0]