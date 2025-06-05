class Solution {
    public int convert(char c){
        switch(c){
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: return 0;
        }
    }
    public int romanToInt(String s) {
        if(s.length() == 1){
            return convert(s.charAt(0));
        }
        int sum = 0;
        for(int i = 0; i < s.length() - 1; i++){
            if(convert(s.charAt(i)) < convert(s.charAt(i + 1))){
                sum += convert(s.charAt(i + 1)) - convert(s.charAt(i));
                i++;
            }
            else{
                sum += convert(s.charAt(i));
            }
        }
        if(convert(s.charAt(s.length() - 2)) >= convert(s.charAt(s.length() - 1))){
            sum += convert(s.charAt(s.length() - 1));
        }
        return sum;
    }
}