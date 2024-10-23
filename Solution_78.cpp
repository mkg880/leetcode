class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> empty;
        res.push_back(empty);
        if(nums.size() == 1) {
            empty.push_back(nums[0]);
            res.push_back(empty);
            return res;
        }
        int val = nums.back();
        nums.pop_back();
        res = subsets(nums);
        vector<vector<int>> to_add;
        for(vector<int> v : res) {
            vector<int> tmp (v.begin(), v.end());
            tmp.push_back(val);
            to_add.push_back(tmp);
        }
        res.insert(res.end(), to_add.begin(), to_add.end());
        return res;
    }
};