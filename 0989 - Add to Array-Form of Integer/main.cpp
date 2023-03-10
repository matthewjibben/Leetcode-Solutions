#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    // vector<int> addToArrayForm(vector<int>& num, int k) {
    //     // potential solutions:
    //     /* 
    //     1. convert each number in num to a string, then add them together and convert it to an int 
    //     2. loop through num, adding to an int T the value*10^N, where N = the place in the int where it should be
    //     3. convert k to a vector, then loop through num adding corresponding values
    //         given that num.length <= 10000, we must use this
    //     */
    //     // k == 0 solution
    //     // solution 1 - this is all useless
    //     // use char array to avoid costly string operations
    //     char arr[num.size() +1];
    //     for (size_t i = 0; i < num.size(); i++)
    //     {
    //         arr[i] = '0' + num[i];
    //     }
    //     arr[num.size()] = '\0';

    //     int solution = atoi(arr) + k;
        
        
    //     string s = to_string(solution);
    //     vector<int> solutionVector;
    //     for(auto i: s){
    //         solutionVector.push_back(i - '0');
    //     }
    //     return solutionVector;
    // }
    vector<int> addToArrayForm(vector<int>& num, int k) {
        // k == 0 solution case
        if(k==0){
            return num;
        }
        if(num.size() < 10){
            // only use this case when num is < int max value
            // use char array to avoid costly string operations
            char arr[num.size() +1];
            for (size_t i = 0; i < num.size(); i++)
            {
                arr[i] = '0' + num[i];
            }
            arr[num.size()] = '\0';

            int solution = atoi(arr) + k;
            
            
            string s = to_string(solution);
            vector<int> solutionVector;
            for(auto i: s){
                solutionVector.push_back(i - '0');
            }
            return solutionVector;
        }
        else {
            // in this case, k will always have fewer digits than num
            string kstring = to_string(k);
            for (size_t i = 0; i < kstring.size(); i++) {
                num[num.size()-1-i] += int(kstring[kstring.size()-1-i] - '0');
            }
            // loop through nums. if any value > 10, subtract 10 and add to the next digit unless impossible
            for (size_t i = 0; i < num.size()-1; i++) {
                if (num[num.size()-1-i] >=10) {
                    // cout << num[num.size()-1-i] << " ";
                    num[num.size()-1-i] -= 10;
                    num[num.size()-1-i-1] += 1;
                }
                
            }
            
            // if the first value is >= 10, we must push_front the vector
            // this is costly. is there a way around it?
            if (num[0] >= 10) {
                num[0] -= 10;
                num.insert(num.begin(), 1);
            }
            return num;
        }
    }
};

int main(){
    vector<int> nums = {3,9,7,6,9,5,3,4,4,9}; //{9,9,9,9,9,9,9,9,9,9};
    int k = 982;

    Solution s;
    vector<int> test = s.addToArrayForm(nums, k);

    cout << endl;
    for(auto i: test){
        cout << i << " ";
    }

    return 0;
}
