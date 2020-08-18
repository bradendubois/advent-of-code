#include <iostream>
#include <map>
#include <vector>
#include <sstream>

using namespace std;

int main() {

    map<int, map<string, int>> sue_map;

    string line, word, value;
    int sue;

    while (getline(cin, line)) {
        
        istringstream conv(line);
        vector<string> result;
        for (string s; conv >> s;) {
            result.push_back(s);
        }

        value = result[1];
        value.pop_back();
        sue = stoi(value);

        for (int i = 2; i < result.size()-2; i+=2) {
            word = result[i];
            value = result[i+1];

            word.pop_back();
            if (i != result.size()-1) {
                value.pop_back();
            }

            sue_map[sue][word] = stoi(value);
        }
    }

    map<string, int> from_sue = {
        {"children", 3}, {"cats", 7},
        {"samoyeds", 2}, {"pomeranians", 3}, {"akitas", 0}, 
        {"vizslas", 0}, {"goldfish", 5}, {"trees", 3}, 
        {"cars", 2}, {"perfumes", 1}
    };

    vector<map<string, int>> possible;

    bool discrepency;
    map<string, int> the_sue;
    for (auto possible_sue : sue_map) {
        
        discrepency = false;
        for (auto known_attribute: possible_sue.second) {
            if (from_sue[known_attribute.first] != known_attribute.second) {
                discrepency = true;
            }
        }

        if (!discrepency) {
            for (auto k: possible_sue.second) {
                cout << k.first << " " << k.second << endl;
            }
            cout << possible_sue.first << "\n\n" << endl;
        }
    }
}