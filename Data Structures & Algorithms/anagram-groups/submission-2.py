class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        length = len(strs)
        anagram = {}
        for i in range(0, length):
            sort_string = tuple(sorted(strs[i]))

            if sort_string not in anagram:
                anagram[sort_string] = []

            anagram[sort_string].append(strs[i])
        
        return list(anagram.values())
            
        