class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.length() == 0) return 0;
        int max = 1;
        for(int i = 0; i < s.length(); i++){
            int sub = i + 1;
            while(sub < s.length() && !s.substring(i, sub).contains(Character.toString(s.charAt(sub)))){
                    sub++;
            }
            if(sub - i > max){
                max = sub - i;
            }
        }
        return max;
    }
}