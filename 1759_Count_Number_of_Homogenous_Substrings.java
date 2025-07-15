class Solution {
    public int countHomogenous(String s) {
        long total = 0;
        int i = 0;
        while(i < s.length()) {
            char c = s.charAt(i);
            long count = 0;
            while(i < s.length() && s.charAt(i) == c) {
                i++;
                count++;
            }
            long val = count * (count + 1) / 2;
            total += val % (long) (Math.pow(10, 9) + 7);
        }
        return (int) total;
    }
}