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
    Map<Integer, Integer> map = new HashMap<>();
    int max = 0;
    ArrayList<Integer> list = new ArrayList<Integer>();
    public int[] findMode(TreeNode root) {
        if(root == null) return new int[]{};
        map.put(root.val, map.getOrDefault(root.val, 0) + 1);
        if(map.get(root.val) == max) list.add(root.val);
        else if(map.get(root.val) > max) {
            max = map.get(root.val);
            list = new ArrayList<Integer>();
            list.add(root.val);
        }
        findMode(root.left);
        findMode(root.right);
        return list.stream().mapToInt(i->i).toArray();
    }
}