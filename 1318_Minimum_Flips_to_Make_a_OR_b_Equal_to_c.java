class Solution {
    public int minFlips(int a, int b, int c) {
        int cnt = 0;
        while(a != 0 || b != 0 || c != 0) {
            int d = a % 2;
            int e = b % 2;
            int f = c % 2;
            if((d | e) != f) {
                if(f == 0 && d == 1 && e == 1) cnt += 2;
                else cnt++;
            }
            a /= 2;
            b /= 2;
            c /= 2;
        }
        return cnt;
    }
}