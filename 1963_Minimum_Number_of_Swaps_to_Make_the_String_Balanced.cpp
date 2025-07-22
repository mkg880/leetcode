class Solution {
public:
    int minSwaps(string s) {
        int open = 0;
        int res = 0;
        for(char c : s) {
            if(c == ']' && open == 0) {
                res++;
                open++;
            }
            else if (c == ']') {
                open--;
            }
            else {
                open++;;
            }
        }
        return res;
    }
};