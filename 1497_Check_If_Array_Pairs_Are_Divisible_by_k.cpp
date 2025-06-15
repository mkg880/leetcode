class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        int freq[k];
        for(int i = 0; i < k; i++) {
            freq[i] = 0;
        }
        for(int i : arr) {
            freq[((i % k) + k) % k]++;
        }
        for(int i : freq) {
            cout << i << endl;
        }
        for(int i = 0; i <= k / 2; i++) {
            if((i != 0 && freq[i] != freq[k - i]) || (i == 0 && freq[i] % 2 != 0)) {
                return false;
            }
        }
        return true;
    }
};