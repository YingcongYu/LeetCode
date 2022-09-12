# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. 
# You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        
        def valid(seg):
            if not seg:
                return False
            return 0 <= int(seg) <= 255 and str(int(seg)) == seg
        
        output = []
        for one in range(4):
            part1 = s[:one+1]
            if valid(part1):
                for two in range(one+1, one+4):
                    part2 = s[one+1:two+1]
                    if valid(part2):
                        for three in range(two+1, two+4):
                            part3 = s[two+1:three+1]
                            part4 = s[three+1:]
                            if valid(part3) and valid(part4):
                                output.append(part1 + '.' + part2 + '.' + part3 + '.' + part4)

        return output
