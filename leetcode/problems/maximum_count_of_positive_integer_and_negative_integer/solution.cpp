class Solution {
public:
    int maximumCount(vector<int>& nums) {
        int p=0,n=0,s=nums.size()-1;
        for (int i=0;i<=s;i++){
            if (nums[i]>0){
                p+=1;
            }
            else if (nums[i]<0){
                n+=1;
            }
        }
        if (p>n){
            return p;
        }
        else{
            return n;
        }
    }
      
    
};