#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
    private:
        
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            // a third solution exists:
            /* 
            We can use a hash map to store each value. While populating the hashmap with a value,
            we can check if a value exists inside the hashmap that adds up to the target.
            This only needs O(n), since it loops through the vector once
            */
           
            vector<int> solution;
            unordered_map<int, int> hashmap;
            // populate the hashmap, but search for the value's compliment each loop
            for (int i = 0; i < nums.size(); i++) {
                // search the hashmap for the value's compliment. If it exists, return the two indicies
                int compliment = target - nums[i];
                if(hashmap.find(compliment)!=hashmap.end()){
                    // value is found
                    solution = {hashmap[compliment], i};
                    return solution;
                }
                // insert the value and index, where the key is the value
                hashmap[nums[i]] = i;
            }
           
            // not found
            cout << "not found" << endl;
            return vector<int>();
        }
};


int main(){
    vector<int> nums = {-3,4,3,90};
    int target = 0;
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