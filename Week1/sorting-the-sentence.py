class Solution:
    def sortSentence(self, s: str) -> str:
        s=list(s.split(" "))
        print(s)
        track={int(s[i][len(elem)-1:]):s[i][:len(elem)-1] for i,elem in enumerate(s)}
        print(track)
        new=dict(sorted(track.items(),key=lambda x:x[0]))
        print(new)
        ans=[]
        ans+=new.values()
        print(ans)
        return " ".join(ans)

        
        
        
        
        
        
        


