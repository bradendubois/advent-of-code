#include <iostream>
#include <sstream>

using namespace std;

int main() {
    string line;
    int checksum = 0;
    while (getline(cin, line)) {
        stringstream conv(line);
        int val, min = INT32_MAX, max = INT32_MIN;
        while (conv >> val) {
            if (val < min) min = val;
            if (val > max) max = val;
        } checksum += max - min;
    } cout << checksum << endl;
}