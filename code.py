class Solution:
    def reverseVowels(self, s: str) -> str:
        n=len(s)
        o=list(s)
        print(o)
        f=0
        e=n-1
        d=('aeiouAEIOU')
        while f<e:
            if o[e] not in d:
                e-=1
            elif o[f] not in d:
                f+=1
            else:
                o[f],o[e]=o[e],o[f]
                e-=1
                f+=1
        return ''.join(o)

        
