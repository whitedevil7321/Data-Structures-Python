class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]

        # LOWER BOUND
        low, high = 0, n - 1
        lb = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1

        # If target not found
        if lb == -1 or nums[lb] != target:
            return [-1, -1]

        # UPPER BOUND
        low, high = 0, n - 1
        ub = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1

        # If no element > target, last index is n-1
        if ub == -1:
            ub = n

        return [lb, ub - 1]
