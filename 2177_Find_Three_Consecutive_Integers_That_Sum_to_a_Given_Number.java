class Solution {
    public long[] sumOfThree(long num) {
        if(num % 3 != 0) return new long[0];
        long div = num/3;
        return new long[]{div - 1, div, div+1};
    }
}