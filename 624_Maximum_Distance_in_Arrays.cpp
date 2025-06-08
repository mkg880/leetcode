class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int min = INT_MAX;
        int min_idx = 0;
        int second_min = INT_MAX;
        int max = INT_MIN;
        int max_idx = 0;
        int second_max = INT_MIN;
        for(int i = 0; i < arrays.size(); i++) {
            if(arrays[i][0] < min) {
                second_min = min;
                min = arrays[i][0];
                min_idx = i;
            }
            else if (arrays[i][0] < second_min) {
                second_min = arrays[i][0];
            }
            if(arrays[i][arrays[i].size() - 1] > max) {
                second_max = max;
                max = arrays[i][arrays[i].size() - 1];
                max_idx = i;
            }
            else if (arrays[i][arrays[i].size() - 1] > second_max) {
                second_max = arrays[i][arrays[i].size() - 1];
            }
        }
        if(min_idx != max_idx) {
            return max - min;
        }
        return std::max(second_max - min, max - second_min);
    }
};