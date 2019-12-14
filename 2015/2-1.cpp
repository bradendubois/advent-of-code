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

        int minarea = INT32_MAX;
        for (int i = 0; i < 2; i++) {
            for (int j = i+1; j <= 2; j++) {
                int area = dimensions[i] * dimensions[j];
                if (area < minarea) minarea = area;
                total += 2 * area;
            }
        }
        total += minarea;
    }

    cout << total << endl;
}