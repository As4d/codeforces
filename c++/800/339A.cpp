#include <bits/stdc++.h>

using namespace std;

int main() {
    string s;
    cin >> s;

    vector<int> nums;

    for (int i = 0; i < s.size(); i += 2) {
        nums.push_back(s[i] - '0'); // uses ASCII code for int value
    }

    sort(nums.begin(), nums.end());

    for (int i = 0; i < nums.size(); i++) {
        if (i > 0) cout << "+";
        cout << nums[i];
    }
    
    cout << endl;
}
