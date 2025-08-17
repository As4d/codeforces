#include <iostream>

using namespace std;

int main(){

    char c;
    char i;
    char j;

    for(int x = 0; x < 5; x++){
        for(int y = 0; y < 5; y++){
            cin >> c; if(c == '1'){i = x; j = y; break;}
        }
    }

    cout << abs(2 - i) + abs(2 - j) << endl;
}