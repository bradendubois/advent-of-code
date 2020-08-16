#include <iostream>
#include <map>
#include <vector>
#include <string.h>
#include <bits/stdc++.h>
#include <sstream>

using namespace std;

int evaluate(vector<string> ordering, map<string, map<string, int>> & happiness) {
    int total = 0;
    for (int i = 0; i < ordering.size(); i++) {
        total += happiness[ordering[(i+1) % ordering.size()]][ordering[i]];
        total += happiness[ordering[i]][ordering[(i+1) % ordering.size()]];
    } return total;
}

int main() {
    string line;
    map<string, map<string, int>> happiness;

    vector<string> people;
    while (getline(cin, line)) {

        istringstream conv(line);
        vector<string> result;
        for (string s; conv >> s;) {
            result.push_back(s);
        }

        string a, b, exchange;
        a = result[0], b = result[result.size()-1];
        b.pop_back();

        if (happiness.count(a) == 0) {
            people.push_back(a);
        }

        exchange = result[2];
        int value = stoi(result[3]);
        if (exchange.compare("lose") == 0) {
            value *= -1;
        }

        happiness[a][b] = value;
    } 
    
    for (auto person: people) {
        happiness[person]["me"] = 0;
        happiness["me"][person] = 0;
    } people.push_back("me");

    int best = INT32_MIN;
    do {
        best = max(best, evaluate(people, happiness));
    } while (next_permutation(people.begin(), people.end()));
    cout << best << endl;
}