class Solution(object):
    # my method
    def lengthOfLastWord1(self, s):
        if len(s) == 0:
            return 0
        else:
            new_s = [len(i) for i in s.split(' ')]
            l = len(s) - 1
            ind = 1
            # start from the end
            #before the start element and speace happened 
            while ind < l and new_s[-ind] == 0:
                # go to the previous one
                ind += 1
            return new_s[ind]
        

    # Method found online, inspiration
    def lengthOfLastWord2(self, s):
        if not s:
            return 0
        l=[len(i) for i in s.split(' ')]
        j=len(l)-1
        # judge stars from the end
        # if before 1st element, space (len(i)==0) happened
        while j>0 and l[j] == 0:
            #move to the previous one
            j-=1
        # until not fulfill above condition, 
        # return the length
        return l[j]

    # second time - split function, 24ms + 13.1MB (99.68% + 89.84%)
    def lengthOfLastWord(self, s):
        if not s:
            return 0
        ss = s.split(" ")
        i = len(ss) - 1
        while i >= 0:
            if ss[i] != '':
                return len(ss[i])
            i-=1
        return 0



