class Solution {
    public int div(int n) {
        return n % 7 != 0 ? n / 7 : n / 7 - 1;
    }
    public int totalMoney(int n) {
        int total = 0;
        int cnt = 0;
        while(div(n) > 0) {
            total += 28 + cnt * 7;
            cnt++;
            n -= 7;
        }
        return total + (n * (n+1) / 2 + cnt * n);
    }
}