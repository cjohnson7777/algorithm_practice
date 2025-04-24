#[MEDIUM][NOT UNDERSTOOD, SOLVED] We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

# Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

# You may assume each element in the array is distinct.

# For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.

def count_inversions(arr):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0
        
        middle = len(arr) // 2

        left, inv_left = merge_sort(arr[:middle])
        right, inv_right = merge_sort(arr[middle:])
        merged, inv_split = merge_and_count(left, right)

        total_inversions = inv_right + inv_left + inv_split
        return merged, total_inversions

    def merge_and_count(left, right):
        result = []
        i = 0
        j = 0
        count = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                count += len(left) - i
                j += 1
        
        result += left[i:]
        result += right[j:]

        return result, count
    
    total_inversions = merge_sort(arr)
    return total_inversions


arr = [2, 4, 1, 3, 5]
print(count_inversions(arr))
print(count_inversions([5, 4, 3, 2, 1]))
