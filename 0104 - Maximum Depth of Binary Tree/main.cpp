#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;


// Definition for a binary tree node.
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
    int maxDepth(TreeNode* root) {
        if(root==NULL){
            return 0;
        }
        return max(maxDepth(root->left), maxDepth(root->right)) + 1;
    }
};


int main(){
    vector<int> nums = {3,3};
    int target = 6;
    for(auto i: nums){
        cout << i << " ";
    }
    cout << endl;
    

    Solution s;
    vector<int> test = s.twoSum(nums, target);

    for(auto i: test){
        cout << i << " ";
    }

    return 0;
}