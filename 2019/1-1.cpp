#include <iostream>

using namespace std;

// 2019 - Day 1 - Part 1
int main() {
    int x, sum=0;
    while (cin >> x) sum += ((x / 3) - 2);
    cout << sum << endl;
}