class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagrams_chars_s = {}
        anagrams_chars_t = {}
        for i in range(len(s)):
            if s[i] not in anagrams_chars_s:
                anagrams_chars_s[s[i]] = anagrams_chars_s.get(s[i], 0) + s.count(s[i])
        for j in range(len(t)):
            if t[j] not in anagrams_chars_t:
                anagrams_chars_t[t[j]] = anagrams_chars_t.get(t[j], 0) + t.count(t[j])
        if anagrams_chars_s == anagrams_chars_t:
            return True
        return False