class Solution {
    public boolean backspaceCompare(String s, String t) {
        Stack<Character> stack = new Stack<>();
        Stack<Character> stack2 = new Stack<>();
        for(int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == '#') {
                if(!stack.isEmpty()) stack.pop();
            } else {
                stack.add(s.charAt(i));
            }
        }
        for(int i = 0; i < t.length(); i++) {
            if(t.charAt(i) == '#') {
                if(!stack2.isEmpty()) stack2.pop();
            } else {
                stack2.add(t.charAt(i));
            }
        }
        if(stack.size() != stack2.size()) return false;
        while(!stack.isEmpty()) {
            if(stack.pop() != stack2.pop()) return false;
        }
        return true;
    }
}