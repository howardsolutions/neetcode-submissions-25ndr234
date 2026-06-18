# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1);

    def mergeSortHelper(self, pairs: List[Pair], s: int, e: int):
        # base case is when the sub array has a length of 1
        if e - s + 1 <= 1:
            return pairs
        
        # the middle index of the array 
        m = (s + e) // 2

        # sort the left half 
        self.mergeSortHelper(pairs, s, m)

        # sort the right half 
        self.mergeSortHelper(pairs, m + 1, e)

        # merge the sorted half
        self.merge(pairs, s, m, e)

        return pairs;

    def merge(self, arr: List[Pair], s: int, m: int, e: int):
        # Copy the sorted left & right halfs to temp arrays
        L = arr[s: m + 1]
        R = arr[m + 1: e + 1]

        i = 0  # index for L 
        j = 0 # index for R
        k = s

        # Merge the two sorted halfs into the original array
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else: 
                arr[k] = R[j]
                j += 1
            
            k += 1

        # one of the halfs will have elements remaining?
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k +=1 


