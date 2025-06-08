/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        int len = 0;
        auto temp = head;
        while(temp) {
            temp = temp->next;
            len++;
        }
        int d = len / k;
        int idx = len % k;
        vector<ListNode*> res;
        int i = 0;
        while(i < k) {
            int amt = d + (i < idx ? 1 : 0);
            if(amt > 0) {
                res.push_back(head);
                for(int j = 0; j < amt - 1; j++) {
                    head = head->next;
                }
                temp = head->next;
                head->next = NULL;
                head = temp;
                i++;
            }
            else {
                break;
            }
        }
        while(i < k) {
            res.push_back(NULL);
            i++;
        }
        return res;
    }
};