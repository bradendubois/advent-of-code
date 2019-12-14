#include <iostream>

using namespace std;

int main() {
    string line;
    cin >> line;
    int floor = 0, processed = 0;
    for (auto c : line) {
        processed++;
        
        if (c == '(') floor++;
        else floor--;

        if (floor == -1) {
            cout << processed << endl;
            return 0;
        }
    }
}