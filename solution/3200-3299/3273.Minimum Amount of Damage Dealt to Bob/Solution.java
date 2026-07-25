class Solution {
    public long minDamage(int power, int[] damage, int[] health) {
        int [] time=new int [damage.length];
        int sum=0;
        for(int i=0;i<damage.length;i++){
            float apple=(float)health[i]/power;
            time[i]=(int)Math.ceil(apple);
            sum+=damage[i];
        }
        PriorityQueue<Pair> pq=new PriorityQueue<>((a,b) -> Float.compare(b.dps,a.dps));
        for(int i=0;i<damage.length;i++){
            pq.add(new Pair((float)damage[i]/time[i],i));
        }
        long ans=0;
        while(!pq.isEmpty()){
            Pair p=pq.remove();
            ans+=(long)sum*time[p.index];
            sum-=damage[p.index];
        }
        return ans;
    }
    
}
class Pair{
        float dps;
        int index;
        public Pair(float dps,int index){
            this.dps=dps;
            this.index=index;
        }
    }
