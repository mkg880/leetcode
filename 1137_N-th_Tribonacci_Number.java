class Solution {
    public int tribonacci(int n) {
        int[] dp = new int[Math.max(3, n+1)];
        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 1;
        if(n < 3) return dp[n];
        dp[3] = 2;
        for(int i = 4; i < dp.length; i++) {
            dp[i] = 2 * dp[i-1] - dp[i-4];
        }
        return dp[n];
    }
}