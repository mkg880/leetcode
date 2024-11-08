class Solution {
    public int findComplement(int num) {
        String s = Integer.toBinaryString(num);
        int index = s.indexOf("1");
        if(index != -1) {
            s = s.substring(index);
        }
        int val = 0;
        for(int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == '0') {
                val += (int) Math.pow(2, s.length() - i - 1);
            }
        }
        return val;
    }
}