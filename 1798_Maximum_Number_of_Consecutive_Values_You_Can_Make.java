class Solution {
    public int getMaximumConsecutive(int[] coins) {
        Arrays.sort(coins);
        int total = 1;
        for(int i = 0; i < coins.length; i++) {
            if(coins[i] > total) return total;
            total += coins[i];
        }
        return total;        
    }
}