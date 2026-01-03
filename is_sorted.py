def is_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


# Example usage:
numbers = [1, 2, 4,3, 4, 5]
result = is_sorted(numbers)
if result:
    print("The list is sorted")
else:
    print("The list is not sorted")
