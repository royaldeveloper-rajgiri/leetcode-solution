class Solution:
    def transformStr(self, s: str, strs: List[str]) -> List[bool]:
        b=len(s)
        count=s.count('1')
        res=[False]*len(strs)
        position=[]
        for i,ch  in enumerate(s):
            if ch=='1':
                position.append(i)
        for i,curr in enumerate(strs):
            first=0
            second=0
            for ch in curr:
                if(ch=='1'):
                    first+=1
                elif(ch=='?'):
                    second+=1
            if(first>count or first+second<count):
                res[i]=False
                continue
            need=count-first
            skip=second-need
            secondind=0
            flag=True
            for j,ch in enumerate(curr):
                if(ch=='1'):
                    if j<position[secondind]:
                        flag=False
                        break
                    secondind+=1
                elif(ch=='?'):
                    if(skip>0):
                        skip-=1
                    else:
                        if(j<position[secondind]):
                            flag=False
                            break
                        secondind+=1
            res[i]=flag
        return res
