class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        nw=""
        nw2=""
        for i in word1:
            nw=nw+i
        
        for j in word2:
            nw2=nw2+j
        return nw==nw2 
# """ SEcond optimize python solution
# return "".join(word1)="".join(word2)
