class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        vector<int> odds;
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] % 2 != 0) {
                odds.push_back(i);
            }
        }
        int i = 0;
        int res = 0;
        int j = k - 1;
        while(j < odds.size()) {
            int l = i > 0 ? odds[i-1] : -1;
            int r = j < odds.size() - 1 ? odds[j+1] : nums.size();
            res += (odds[i] - l) * (r - odds[j]);
            i++;
            j++;
        }
        return res;
    }
};