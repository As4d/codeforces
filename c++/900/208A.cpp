#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str;
    cin >> str;
    string result = "";
    while (str.size() > 0)
    {
        string temp = str.substr(0, 3); // store first 0-3 chars

        if (temp.size() < 3) // edge case for last word
        {
            result += temp + " ";
            break;
        }

        str = str.substr(3, str.size()); // strip first 3 chars

        if (temp != "WUB") // find full word by shifting temp and str
        {
            while (temp.substr(temp.size() - 3, 3) != "WUB" && str.size() > 0)
            {
                temp += str[0];
                str = str.substr(1, str.size());
            }
            if (temp.substr(temp.size() - 3, 3) != "WUB")
            {
                result += temp + " ";
            }
            else
            {
                result += temp.substr(0, temp.size() - 3) + " ";
            }
        }
    }
    cout << result.substr(0, result.size() - 1) << "\n"; // strip last ""
}