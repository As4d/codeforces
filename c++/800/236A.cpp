#include <iostream>
#include <set>
#include <string>

using namespace std;

int main(){
    set<char> d;
    string s;
    cin >> s;
    for(char c : s){
        d.insert(c);
    }
    if (d.size() % 2 == 0){
        cout << "CHAT WITH HER!" << endl;
    } else {
        cout << "IGNORE HIM!" << endl;
    }
}