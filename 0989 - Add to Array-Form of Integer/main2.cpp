#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    vector<int> addToArrayForm(vector<int>& num, int k) {
        int carry = 0;
        for (size_t i = num.size() - 1; i >= 0; --i) {
            int n = num[i] + carry + (k % 10);
            carry = 0;
            num[i] = n % 10;
            carry = n / 10;
            k /= 10;
            if (k == 0 && carry == 0) {
                break;
            }
        }
        while (k) {
            int n = (k % 10) + carry;
            carry = n / 10;
            num.insert(num.begin(), n % 10);
            k /= 10;
        }
        if (carry) {
            num.insert(num.begin(), carry);
        }
        return num;
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
