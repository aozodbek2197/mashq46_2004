# 1-mashq
def max_subarray_sum(arr):
    max_current = max_global = arr[0]
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global

print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))
# 2-mashq
def count_occurrences(lst, element):
    return sum(1 for x in lst if x == element)

print(count_occurrences([1,2,3,2,4,2,5], 2))
# 3-mashq
def matrix_transpose(matrix):
    return [list(row) for row in zip(*matrix)]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix_transpose(matrix))
