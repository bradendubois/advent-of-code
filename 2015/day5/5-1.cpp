#include <iostream>

using namespace std;

bool vowels(string line) {
    int total = 0;
    for (auto c: line) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
            total++;
    } return (total >= 3);
}

bool repeat(string line) {
    char prev = ' ';
    for (auto c: line) {
        if (c == prev) return true;
        prev = c;
    } return false;
}

bool badSeqs(string line) {
    string seqs [] = {"ab", "cd", "pq", "xy"};
    for (auto seq : seqs) {
        if (line.find(seq) != string::npos) return true;
    } return false;
}

int main() {
    string line;
    int nice = 0;
    while (getline(cin, line)) {
        if (vowels(line) && repeat(line) && !badSeqs(line)) nice++;
    } cout << nice << endl;
}