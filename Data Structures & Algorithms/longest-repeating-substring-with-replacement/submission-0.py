class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## O(n) 数出目前最多的字母并尝试替换较少的字母变成最多的字母
        ## 如果 字母数量相同的则尝试替换第一个检测到的

        left = 0
        hash_map = {}
        max_freq = 0
        max_len = 0

        for right in range(len(s)):

            hash_map[s[right]] = hash_map.get(s[right], 0) + 1

            max_freq = max(max_freq, hash_map[s[right]])

            while (right - left + 1) -  max_freq > k:
                hash_map[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


