'''
Best: O(n) time | O(1) space
Average: O(n^2) time | O(1) space
Worst: O(n^2) time | O(1) space
'''
def insertionSort(array):
    for i in range(1, len(array)):
        while i>0 and array[i] < array[i-1]:
            swap(i-1, i, array)
            i -= 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]		


if __name__ == "__main__":
    print(insertionSort([3,1,78,2,]))