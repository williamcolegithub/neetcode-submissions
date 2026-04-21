class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #what data structure to use:
        if sorted(s) == sorted(t):
            return True                                                                                                         
        else:                                                                                                                   
            return False  