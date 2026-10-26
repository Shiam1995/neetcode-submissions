class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for i in strs:
            label = "".join(sorted(i))
            if label not in groups:
                groups[label] = []
            groups[label].append(i)

        return list(groups.values())
