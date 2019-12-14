#include <iostream>
#include <map>
#include <vector>

using namespace std;

typedef pair<int, int> ii;

int main() {
    string directions;
    cin >> directions;

    map<ii, int> deliveries;
    int houses = 0;

    ii loc;
    loc.first = 0;
    loc.second = 0;

    deliveries[loc]++;
    houses++;

    for (auto c: directions) {
        if (c == '^') loc.second++;
        if (c == 'v') loc.second--;
        if (c == '<') loc.first--;
        if (c == '>') loc.first++;

        if (!deliveries[loc]) houses++;
        deliveries[loc]++;
    }
    cout << houses << endl;
}