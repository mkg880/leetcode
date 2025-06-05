class Solution {
    public boolean idk(String[] strs, String s){
        for(String str : strs){
            if(!str.substring(0, s.length()).equals(s)){
                return false;
            }
        }
        return true;
    }
    public String longestCommonPrefix(String[] strs) {
        if(strs.length == 0){
            return "";
        }
        if(strs.length == 1){
            return strs[0];
        }
        List<String> l = Arrays.asList(strs);
        if(l.contains("")){
            return "";
        }
        String pre = "";
        int i = 1;
        while(true){
            try{
            if(idk(strs, strs[0].substring(0, i))){
                pre = strs[0].substring(0, i);
                i++;
            }
            else{
                break;
            }
            }
            catch(Exception e){
                break;
            }
        }
        return pre;
    }
}