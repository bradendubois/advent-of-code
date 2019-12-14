#include <iostream>

using namespace std;

bool repeat(string line) {
    for (int i = 0; i < line.size()-1; i++) {
        string pair = line.substr(i, 2);
        if (line.substr(i+2).find(pair) != string::npos) 
            return true;
    } return false;
}

bool between(string line) {
    for (int i = 0; i < line.size()-2; i++) {
        if (line.at(i) == line.at(i+2))
            return true;
    } return false;
}

int main() {
    string line;
    int nice = 0;
    while (getline(cin, line)) {
        if (repeat(line) && between(line)) nice++;
    } cout << nice << endl;
}