class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i="".join(map(str,digits))
        i=int(i)
        n=i+1
        l=list(map(int,str(n)))

        return l