#include <iostream>
#include <math.h>

using namespace std;

// 2019 - Day 1 - Part 2
int main() {
    int x, fuel, sum=0;
    while (cin >> x) {
        fuel = (x / 3) - 2;
        while (fuel > 0) {
            sum += fuel;
            fuel /= 3;
            fuel -= 2;
        }
    }
    
    cout << sum << endl;
}