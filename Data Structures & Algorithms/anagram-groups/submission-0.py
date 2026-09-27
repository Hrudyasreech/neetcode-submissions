class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for c in strs:
            a = "".join(sorted(c))
            if a not in seen:
                seen[a] =  []
            seen[a].append(c)

        return list(seen.values())
            
            
        