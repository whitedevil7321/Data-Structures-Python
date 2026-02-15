class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        n = len(nums)

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        max_key = max(freq, key=freq.get)

        if freq[max_key] > n // 2:
            return max_key
