class Solution {
public:
    int minSubarray(vector<int>& nums, int p) {
        unordered_map<int, int> dp;
        int total = 0;
        for(int i : nums) {
            total = (total + i) % p;
        }
        if(total == 0) return 0;
        dp[0] = -1;
        int pre = 0;
        int res = nums.size();
        for(int i = 0; i < nums.size(); i++) {
            pre = (nums[i] + pre) % p;
            int mod = (pre - total + p) % p;
            if(dp.find(mod) != dp.end()) {
                res = min(res, i - dp[mod]);
            }
            dp[pre] = i;
        }
        return res == nums.size() ? -1 : res;

    }
};