/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int height(TreeNode n) {
        if(n == null) return 0;
        return 1 + Math.max(height(n.left), height(n.right));
    }
    
    public List<Integer> getLevel(TreeNode root, int level) {
        List<Integer> list = new ArrayList<Integer>();
        if(root == null) return list;
        if(level == 1) {
            list.add(root.val);
            return list;
        }
        else if (level > 1) {
            List<Integer> l1 = getLevel(root.left, level - 1);
            List<Integer> l2 = getLevel(root.right, level - 1);
            for(int i = 0; i < l1.size(); i++) {
                list.add(l1.get(i));
            }
            for (int i = 0; i < l2.size(); i++) {
                list.add(l2.get(i));
            }
        }
        return list;
    }
    
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        int height = height(root);
        for(int i = 1; i <= height; i++) {
            result.add(getLevel(root, i));
        }
        return result;
    }
}