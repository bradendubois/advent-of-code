#include <iostream>

using namespace std;

int main() {
    string in;
    cin >> in;
    int sum = 0;
    for (int i = 0; i < in.size(); i++) {
        if (in.at(i) == in.at((i + in.size()/2) % in.size())) 
            sum += in.at(i) - '0';
    } cout << sum << endl;
}