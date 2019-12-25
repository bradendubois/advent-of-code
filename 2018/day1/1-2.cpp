#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main() {

    map<int, int> seen;
    vector<int> changes;
    
    int x, sum = 0;
    while (cin >> x) {
        changes.push_back(x);
    }

    x = 0;
    while (!seen[sum]) {
        seen[sum]++;
        sum += changes[x % changes.size()];
        x++;
    } 

    cout << sum << endl;
}