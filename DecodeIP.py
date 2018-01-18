class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid_head(w, length):
            if length > len(w):
                return False
            if length == 1:
                return True
            elif length == 2:
                if w[0] == "0":
                    return False
                else:
                    return True
            elif length == 3:
                if int(w[:3]) >= 256 or w[0] == "0":
                    return False
                else:
                    return True
            else:
                return False


        def ip_helper(word, bytes):
            if bytes == 1:
                if is_valid_head(word, len(word)):
                    return [word]
                else:
                    return []

            res = []

            if is_valid_head(word, 1):
                cands = ip_helper(word[1:], bytes - 1)
                for c in cands:
                    res.append(word[:1] + "." + c)
            if is_valid_head(word, 2):
                cands = ip_helper(word[2:], bytes - 1)
                for c in cands:
                    res.append(word[:2] + "." + c)
            if is_valid_head(word, 3):
                cands = ip_helper(word[3:], bytes - 1)
                for c in cands:
                    res.append(word[:3] + "." + c)
            return res

        return ip_helper(s, 4)
s = Solution()
print(s.restoreIpAddresses("1111"))