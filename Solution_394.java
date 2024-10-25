class Solution {
    public String decodeString(String s) {
        if(!s.contains("[")) {
            return s;
        }
        String result = "";
        int i = 0;
        while(i < s.length()) {
            while(i < s.length() && !Character.isDigit(s.charAt(i))) {
                result += s.charAt(i);
                i++;
            }
            if(i == s.length()) break;
            String number = "";
            while(Character.isDigit(s.charAt(i))) {
                number += s.charAt(i);
                i++;
            }
            i++;
            System.out.println(s);
            int index = i;
            int open = 1;
            int closed = 0;
            while(open != closed) {
                index++;
                if(s.charAt(index) == '[') open++;
                if(s.charAt(index) == ']') closed ++;
            }
            String sub = s.substring(i, index);
            int repeat = Integer.parseInt(number);
            result += decodeString(sub).repeat(Integer.parseInt(number));
            i = index + 1;
        }
        return result;
    }
}