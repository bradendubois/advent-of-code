#include <iostream>
#include <map>
#include <vector>
#include <string.h>
#include <bits/stdc++.h>

using namespace std;

int evaluate(vector<string> ordering, map<string, map<string, int>> & happiness) {
    int total = 0;
    for (int i = 0; i < ordering.size(); i++) {
        total += happiness[ordering[i]][ordering[(i-1) % ordering.size()]];
        total += happiness[ordering[i]][ordering[(i+1) % ordering.size()]];
    } return total;
}

int main() {
    string line;
    map<string, map<string, int>> happiness;

    vector<string> people;
    while (getline(cin, line)) {

        // Gross..
        string s, t, amount;
        s = line.substr(0, line.find(" "));
        line = line.substr(line.find("would ")+6);
        string exchange = line.substr(0, line.find(" "));
        line = line.substr(line.find(" ")+1);
        amount = line.substr(0, line.find(" "));
        line = line.substr(line.find("to ")+3);
        t = line.substr(0, line.find("."));

        int value = stoi(amount);
        if (strcmp(exchange.c_str(), "gain") != 0) value *= -1;

        if (!happiness[s].size()) people.push_back(s);
        happiness[s][t] = value;
    }

    int best = INT32_MIN;
    do {
        best = max(best, evaluate(people, happiness));
    } while (next_permutation(people.begin(), people.end()));
    cout << best << endl;
}