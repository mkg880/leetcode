class Solution {
    public String getSmallestString(int n, int k) {
        int x = (26*n - k) / 25;
        k -= x;
        String s = "a".repeat(x);
        int val = 26- (26 * (n-x) - k);
        if(k == 0) return s;
        s += Character.toString(val - 1 + 'a');
        s += "z".repeat(Math.max(0, n - x - 1));
        return s;

    }
}