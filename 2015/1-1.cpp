#include <iostream>

using namespace std;

int main() {
    string line;
    cin >> line;
    int floor = 0;
    for (auto c : line) {
        if (c == '(') floor++;
        else floor--;        
    }
    cout << floor << endl;
}