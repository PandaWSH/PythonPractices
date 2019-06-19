class Solution:
    # my method while-condition 180ms + 17.8 MB (39%+31.14%)
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 1:
            pass
        i = 0
        while i < int(len(s)/2):
            a = s[i]
            s[i] = s[len(s)-i-1] 
            s[len(s)-i-1] = a
            i+=1

    # my method 2 (164ms + 17.6 MB)
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 1:
            pass
        for i in range( int(len(s)/2) ):
            a = s[i]
            s[i] = s[len(s)-i-1] 
            s[len(s)-i-1] = a
            i+=1