class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in range(0,len(strs)):
            if "".join(sorted(strs[s])) in hashmap:
                hashmap["".join(sorted(strs[s]))].append(strs[s])
            else:
                hashmap["".join(sorted(strs[s]))] =[strs[s]]
                # print(hashmap)
        # print([hashmap.values()])
        return list(hashmap.values())
