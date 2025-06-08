class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> s = new Stack<>();
        for(int i : asteroids) {
            if(i < 0) {
                boolean deleted = false;
                while(!s.isEmpty()) {
                    int val = s.pop();
                    if(val < 0) {
                        s.push(val);
                        break;
                    }
                    if(val > -i) {
                        s.push(val);
                        deleted = true;
                        break;
                    }
                    if(val == -i) {
                        deleted = true;
                        break;
                    }
                }
                if(!deleted) s.push(i);
            }
            else s.push(i);
        }
        int[] res = new int[s.size()];
        for(int i = res.length - 1; i >= 0; i--) {
            res[i] = s.pop();
        }
        return res;
    }
}