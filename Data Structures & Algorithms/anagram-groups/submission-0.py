class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import defaultdict

        grouped_dict = defaultdict(list)

        for s in strs:
            count = [0]*26

            for char in s:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            grouped_dict[key].append(s)

        return list (grouped_dict.values())
        