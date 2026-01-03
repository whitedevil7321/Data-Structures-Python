def Second_largest(nums):
    if len(nums)<2:
        return None
    first = second = float('-inf')
    for i in nums:
        if i>first:
            second = first
            first = i

        elif first>i>second:
            second = i
    return second if second != float('-inf') else None


# Example usage:
numbers = [3, 5, 2, 9, 7]
result = Second_largest(numbers)
print("The second largest number is:", result)  # Output: The second largest number is