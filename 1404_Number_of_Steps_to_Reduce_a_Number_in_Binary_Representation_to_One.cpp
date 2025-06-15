class Solution {
public:
    int numSteps(string s) {
        deque<bool> q;
        int cnt = 0.;
        for(char c : s) {
            q.push_back(c == '1');
        }
        while(q.size() > 1) {
            if(q.back()) {
                cnt++;
                auto itr = q.rbegin();
                while(itr != q.rend()) {
                    bool b = *itr;
                    *itr = !b;
                    if(!b) {
                        break;
                    }
                    itr++;
                }
                if(itr == q.rend()) {
                    q.push_front(true);
                }
            }
            cnt++;
            q.pop_back();
        }
        if(!q.back()) {
            cnt++;
        }
        return cnt;
    }
};