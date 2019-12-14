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

    ii loc1;
    loc1.first = 0;
    loc1.second = 0;

    ii loc2;
    loc2.first = 0;
    loc2.second = 0;

    ii * loc;   // Use a pointer *to* the two santa locations!
    loc = &loc1;    // Makes switching way easier.

    deliveries[*loc]++;
    houses++;

    for (auto c: directions) {
        if (c == '^') (*loc).second++;
        if (c == 'v') (*loc).second--;
        if (c == '<') (*loc).first--;
        if (c == '>') (*loc).first++;

        if (!deliveries[*loc]) houses++;
        deliveries[*loc]++;

        loc = (loc == &loc1 ? &loc2 : &loc1);
    }
    cout << houses << endl;
}