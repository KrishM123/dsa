struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
 
class Solution {
public:
    int maximum_path;

    int maxPathSum(TreeNode* root) {
        maximum_path = root->val;
        helper(root);
        return maximum_path;
    }

    int helper(TreeNode* root) {
        int left = 0, right = 0;
        if (root->left != nullptr && root->right != nullptr) {
            left = helper(root->left);
            right = helper(root->right);
        }
        else if (root->left != nullptr) {left = helper(root->left);}
        else if (root->right != nullptr) {right = helper(root->right);}

        maximum_path = max(max(max(left+root->val, right+root->val), max(left+right+root->val, maximum_path)), root->val);;
        return max(max(left, right) + root->val, root->val); 
        }
};