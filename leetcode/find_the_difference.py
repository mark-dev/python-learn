from typing import Dict, Any, Union


class Solution:
    def count_chars(self, s: str) -> Dict[str,int]:
        d: Dict[str,int] =  {}
        for c in s:
            existing = d.get(c,0)
            d[c] = existing + 1
        return d

    def search_diff(self, smap: Dict[str,int], tmap: Dict[str,int]) -> str:
        greatest_dict = smap if len(smap) > len(tmap) else tmap
        smallest_dict = tmap if greatest_dict is smap else smap

        for k,v in greatest_dict.items():
            s_ctx = smallest_dict.get(k,0)
            if v > s_ctx:
                return k
        return ""
    def findTheDifference(self, s: str, t: str) -> str:
        return self.search_diff(self.count_chars(s),self.count_chars(t))

s = "abcd"
t = "abcde"
print(Solution().findTheDifference(s,t))