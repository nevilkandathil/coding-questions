def isValidSubsequence(array, sequence):
    
    '''
    Method 1
    
    Time: O(n)
    Space: O(1)
    '''
    ind = 0
    
    for num in array:
		if num in sequence and num == sequence[ind]:
			ind += 1
		if ind == len(sequence):
			break
    return ind == len(sequence)

    '''
    Method 2
    
    Time: O(n)
    Space: O(1)
    '''
    # arrIdx = 0
    # seqIdx = 0
    # while arrIdx < len(array) and seqIdx <len(sequence):
    #     if array[arrIdx] == sequence[seqIdx]:
    #         seqIdx += 1
    #     arrIdx += 1
    # return seqIdx == len(sequence)

def main():
    print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
main()