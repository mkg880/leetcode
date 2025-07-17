class Solution {
    public int sumBase(int n, int k) {
        int q = n / k;
        int r = n % k;
        int sum = 0;
        do {
            sum += r;
            r = q % k;
            q = q / k;
        } while(q > 0);
        return sum + r;
    }
}