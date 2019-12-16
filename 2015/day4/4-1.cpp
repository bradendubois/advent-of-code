#include <iostream>
#include "md5.h"

using namespace std;

bool leadingZeroes(string s) {
    for (int i = 0; i < 5; i++) {
        if (!(s.at(i) == '0')) return false;
    } return true;
}

int main() {
    int s = 1;
    while (s++) {
        string pos =  "iwrupvqb" + to_string(s);
        cout << pos << endl;
        string hashed = md5(pos);

        if (leadingZeroes(hashed)) {
            cout << s << endl;
            return 0;
        }   
    }
}