#include <iostream>
#include <map>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int cost(vector<string> cities, map<string, map<string, int>> & costs) {
    int total = 0;
    for (int i = 0; i < cities.size()-1; i++) {
        total += costs[cities[i]][cities[i+1]];
    } return total;
}

int main() {
    string line;
    map<string, map<string, int>> costs;
    vector<string> cities;

    while (getline(cin, line)) {
        string s, t, c;
        s = line.substr(0, line.find(" "));
        line = line.substr(line.find("to ")+3);
        t = line.substr(0, line.find(" "));
        c = line.substr(line.find("= ")+2);
        int cost = stoi(c);

        if (!costs[s].size()) cities.push_back(s);
        costs[s][t] = cost;
        if (!costs[t].size()) cities.push_back(t);
        costs[t][s] = cost;
    }

    // Hamiltonian Cycle? NP-Hard, sad.
    // Maximally-dense graph? Easy bruteforce by ordering-permutation.
    int best = INT32_MAX;
    do {
        best = min(best, cost(cities, costs));
    } while (std::next_permutation(cities.begin(), cities.end())) ;

    cout << best << endl;
}