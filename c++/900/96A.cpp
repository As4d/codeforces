#include <iostream>
#include <string>

using namespace std;

int main(){
    string s;
    cin >> s;

    int count = 0;
    char target = s[0];
    bool dangerous = false;

    for (char c : s){
        if(c == target){
            count++;
        }
        else{
            target = c;
            count = 1;
        }
        if(count == 7){
            dangerous  = true;
            break;
        }
    }

    if(dangerous){
        cout << "YES";
    }
    else{
        cout << "NO";
    }
}