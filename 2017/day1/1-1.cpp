#include <iostream>

using namespace std;

int main() {
    string in;
    cin >> in;
    int sum = 0;
    char prev = in.at(in.size()-1);
    for (auto c : in) {
        if (prev == c) sum += c - '0';
        prev = c;
    } cout << sum << endl;
}