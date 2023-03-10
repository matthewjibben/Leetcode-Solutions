#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

class Solution {
    private:
        
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            // naive solution: O(n^2)
            // loop through the list. 
            // if a value < target, loop through the rest of the list to find a value
            //      where value1 + value2 == target

            //another solution:
            /* 
            1. Sort the list O(n log n)
            2. start by checking valueA at index 0 and valueB at the end of the list O(n)
                If valueA + valueB < target:
                    increase index for valueA
                else if valueA + valueB > target:
                    decrease index for valueB
                continue until solution is found
            total: O((n log n) + n) = O(n log n)
            */

            vector<int> solution;
            // Save the original indices while sorting by creating a second vector of indicies 
            vector<int> indicies(nums.size());
            iota(indicies.begin(), indicies.end(), 0);

            // sort indicies list based on the nums values by using a lambda function
            sort(indicies.begin(), indicies.end(), [&nums](size_t i1, size_t i2) {return nums[i1] < nums[i2];});

            
            // for(auto i: indicies){
            //     cout << i << " ";
            // }
            // cout << endl;

            int A = 0;
            int B = indicies.size()-1;
            // cout << A << " " << B << ": " << nums[indicies[A]] << "+" << nums[indicies[B]] << endl;
            while (nums[indicies[A]] + nums[indicies[B]] != target) {
                // cout << A << " " << B << ": " << nums[indicies[A]] << "+" << nums[indicies[B]] << endl;
                if(nums[indicies[A]] + nums[indicies[B]] < target){
                    A++;
                }
                else{
                    B--;
                }
            }
            solution = {indicies[A], indicies[B]};
            
            

            return solution;
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