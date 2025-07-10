class Solution {
    public int numSub(String s) {
        int res = 0;
        int mod = (int) (Math.pow(10, 9) + 7);
        int streak = 0;
        for(int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == '1') {
                streak++;
            }
            else {
                if(streak > 0) {
                    long val = ((long)streak * (long)(streak + 1) / 2) % mod;
                    res = (res + (int)val) % mod;
                }
                streak = 0;
            }
        }
        if(streak > 0) {
            res = (res + (streak * (streak + 1) / 2)) % mod;
        }
        return res;
    }
}