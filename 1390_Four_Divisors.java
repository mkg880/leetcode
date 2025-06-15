class Solution {
    public int sumFourDivisors(int[] nums) {
        int total = 0;
        for(int i : nums) {
            int divisors = 0;
            int sum = 0;
            for(int j = 1; j <= Math.sqrt(i); j++) {
                if(i % j == 0) {
                    if(i / j == j) {
                        divisors++;
                        sum += j;
                    } else {
                        divisors += 2;
                        sum += j + i/j;
                    }
                }
            }
            if(divisors == 4) {
                total += sum;
            }
        }
        return total;
    }
}