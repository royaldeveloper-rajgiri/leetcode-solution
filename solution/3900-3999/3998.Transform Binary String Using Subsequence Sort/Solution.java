class Solution {
    public boolean[] transformStr(String s, String[] strs) {
        int n=s.length();
        int count=0;
        boolean res[]=new boolean[strs.length];
        for(char ch:s.toCharArray()){
            if(ch=='1'){
                count++;
            }
        }
        int position[]=new int[count];
        int ind=0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='1'){
                position[ind++]=i;
            }
        }
        for(int i=0;i<strs.length;i++){
            String curr=strs[i];
            int first=0;
            int second=0;
            for(int j=0;j<n;j++){
                char ch=curr.charAt(j);
                if(ch=='1'){
                    first++;
                }
                else if(ch=='?'){
                    second++;
                }}
                if(first>count||first+second<count){
                    res[i]=false;
                    continue;
                }
                int need=count-first;
                int skip=second-need;
                int secondind=0;
                boolean flag=true;
                for(int j=0;j<n;j++){
                    char ch=curr.charAt(j);
                    if(ch=='1'){
                        if(j<position[secondind]){
                            flag=false;
                            break;
                        }
                        secondind++;
                    }
                    else if(ch=='?'){
                        if(skip>0){
                            skip--;
                        }
                        else{
                            if(j<position[secondind]){
                                flag=false;
                                break;
                            }
                            secondind++;
                        }
                    }
                }
            res[i]=flag;
            }
        return res;
        }
    }
