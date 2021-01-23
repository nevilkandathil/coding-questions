# def findThreeLargestNumbers(array):
#     # Write your code here.
#     array.sort()
#     return array[len(array)-3:]

'''
O(n) time | O(1) space
'''
def findThreeLargestNumbers(array):
    threeLargest = [None, None, None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest

def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)

def shiftAndUpdate(arr, num, idx):
    for i in range(idx+1):
        if i==idx:
            arr[i] = num
        else:
            arr[i] = arr[i+1]
    

if __name__ == "__main__":
    print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))