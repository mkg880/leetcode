class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        long sum = 0;
        for(int val : chalk) {
            sum += val;
        }
        int m = k % sum;
        for(int i = 0; i < chalk.size(); i++) {
            if(m < chalk[i]) return i;
            m -= chalk[i];
        }
        return -1;
    }
};