
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #do we need to set and sort it we already have the list
        # i think so otherwise the logic would be a nightmare
        longest = 0

        num_set = set(nums)

        for num in num_set:
            if num -1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest,length)

        return longest
        #maybe a loop counter starting from end