class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return false

        d1={}
        d2={}
        for i in range (len(s)):
            schar=s[i]
            tchar=t[i]
            if schar not in d1:
                d1[schar]=tchar
            else:
                if d1[schar]!=tchar:
                    return False

            if tchar not in d2:
                d2[tchar]=schar
            else :
                if d2[tchar]!=schar:
                    return False
        return True
