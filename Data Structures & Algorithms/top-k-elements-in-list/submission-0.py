class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = {}

        for i in nums:
            if i not in freq_list:
                key = i
                value = 0
                freq_list[i] = value
            if i in freq_list:
                freq_list[i] += 1

        ranked = sorted(freq_list, key=freq_list.get, reverse=True)

        return ranked[:k]