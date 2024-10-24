/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {

        if((p.left != null && p.left.val == q.val) || (p.right != null && p.right.val == q.val)) {
            return p;
        }
        else if((q.left != null && q.left.val == p.val) || (q.right != null && q.right.val == p.val)) {
             return q;
        }
        if(p.val == root.val || q.val == root.val || (p.val < root.val && q.val > root.val) || (q.val < root.val && p.val > root.val)) {
            return root;
        }
        else if(p.val < root.val) {
            return lowestCommonAncestor(root.left, p, q);
        }
        else {
            return lowestCommonAncestor(root.right, p, q);
        }
    }
}