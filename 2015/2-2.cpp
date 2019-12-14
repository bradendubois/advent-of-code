#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    string line;
    int total = 0;

    while (getline(cin, line)) {
        stringstream conv(line);
        vector<int> dimensions;

        while (conv.good()) {
            string dim;
            getline(conv, dim, 'x');
            dimensions.push_back(stoi(dim));
        }

        sort(dimensions.begin(), dimensions.end());
        total += 2 * (dimensions[0] + dimensions[1]);
        total += dimensions[0] * dimensions[1] * dimensions[2];
    }

    cout << total << endl;
}