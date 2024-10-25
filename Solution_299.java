class Solution {
    public String getHint(String secret, String guess) {
        int c = 0, b = 0;
        ArrayList<Character> s = new ArrayList<Character>();
        for (char ch : secret.toCharArray()) {
            s.add(ch);
        }
        ArrayList<Character> g = new ArrayList<Character>();
        for (char ch : guess.toCharArray()) {
            g.add(ch);
        }
        for(int i = 0; i < s.size(); i++) {
            if(s.get(i) == g.get(i)) {
                s.remove(i);
                g.remove(i);
                b++;
                i--;
            }
        }
        for(int i = 0; i < g.size(); i++) {
            if(s.contains(g.get(i))) {
                s.remove(g.get(i));
                g.remove(i);
                c++;
                i--;
            }
        }
        return b + "A" + c + "B";


    }
}