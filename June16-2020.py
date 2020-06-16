class Solution:
    def validIPAddress(self, IP: str) -> str:
        self.hex = set(['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f'])
        
        if self.isValidIPv4(IP): return 'IPv4'
        if self.isValidIPv6(IP): return 'IPv6'
        return 'Neither'
    
    def isValidIPv4(self, IP):
        if '.' not in IP: return False
        parts = IP.split('.')
        if len(parts) != 4: return False
        for part in parts:
            if not part.isdecimal(): return False
            if len(str(int(part))) != len(part): return False
            if not 0 <= int(part) <= 255: return False
        return True
    
    def isValidIPv6(self, IP):
        if ':' not in IP: return False
        parts = IP.split(':')
        if len(parts) != 8: return False
        for part in parts:
            part = part.lower()
            if not 1 <= len(part) <= 4: return False
            for c in part:
                if c not in self.hex: return False
            num = int(part, 16)
            if not 0 <= num <= 65535: return False
        return True
