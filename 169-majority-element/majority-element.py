class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict=Counter(nums)
        max_value = max(my_dict.values())
        for key, value in my_dict.items():
            if value == max_value:
                return key