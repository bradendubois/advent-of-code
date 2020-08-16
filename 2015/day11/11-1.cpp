#include <iostream>
#include <set>

using namespace std;

void increment(int index, string & s) {
    if (index == -1) {
        s = 'a' + s;
    } else if (s.at(index) == 'z') {
        s[index] = 'a';
        increment(index - 1, s);
    } else  {
        s[index] = s.at(index) + 1;
    }
}

bool straight(string s) {

    for (int i = 1; i < s.size()-2; i++) {
        if (s.at(i) == s.at(i-1) + 1 && s.at(i) == s.at(i+1) -1) return true;
    } return false;
}

bool no_confusing(string s) {
    for (auto c: s) {
        if (c == 'i' || c == 'o' || c == 'l') return false;
    } return true;
}

bool different(string s) {

    set<char> pairs;
    for (char letter = 'a'; letter <= 'z'; letter++) {
        for (int i = 0; i < s.size() - 1; i++) {
            if (s.at(i) == letter && s.at(i+1) == letter) {
                pairs.insert(letter);
            } 
        }
    } return pairs.size() > 1;
}

bool valid(string s) {
    return straight(s) && no_confusing(s) && different(s);
}

int main() {

    string s;
    cin >> s;

    increment(s.size()-1, s);

    while (!valid(s)) increment(s.size()-1, s);

    cout << s << endl;
}