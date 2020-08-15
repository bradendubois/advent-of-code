#include <iostream>
#include <string.h>
#include <map>
#include <vector>
#include <sstream>

using namespace std;

typedef unsigned short int signal;

void resolve(string wire, map<string, map<string, string>> & circuit_map, map<string, bool> & resolved, map<string, signal> & signals) {

    if (circuit_map.count(wire) == 0) {
        signals[wire] = (signal) stoi(wire);
        return;
    } else if (resolved[wire]) {
        return;
    }

    map<string, string> current = circuit_map[wire];

    string connection = current["connection_type"];
    signal value;
    
    resolve(current["arg_1"], circuit_map, resolved, signals);
    if (current["arg_2"].compare("")) {
        resolve(current["arg_2"], circuit_map, resolved, signals);
    }

    if (connection.compare("DIRECT") == 0) {

        value = signals[current["arg_1"]];

    } else if (connection.compare("NOT") == 0) {

        value = ~((signal) signals[current["arg_1"]]);

    } else if (connection.compare("AND") == 0) {

        string a1 = current["arg_1"], a2 = current["arg_2"];
        
        signal a1_s = signals[a1];
        signal a2_s = signals[a2];

        value = (signal) (a1_s & a2_s);

    } else if (connection.compare("OR") == 0) {

        string a1 = current["arg_1"], a2 = current["arg_2"];
        
        signal a1_s = signals[a1];
        signal a2_s = signals[a2];

        value = (signal) a1_s | a2_s;

    } else if (connection.compare("LSHIFT") == 0) {

        value = signals[current["arg_1"]] << stoi(current["arg_2"]);

    } else if (connection.compare("RSHIFT") == 0) {
                
        value = signals[current["arg_1"]] >> stoi(current["arg_2"]);

    }

    resolved[wire] = true;
    signals[wire] = (signal) value;
}

int main() {

    map<string, map<string, string>> circuit_map;
    map<string, bool> resolved_map;
    map<string, signal> signal_map;

    string line;

    while (getline(cin, line)) {

        istringstream conv(line);
        vector<string> result;
        for (string s; conv >> s;) {
            result.push_back(s);
        }

        int index;
        for (int i = 0; i < result.size(); i++) {
            if (result[i].compare("->") == 0) {
                index = i;
                break;
            }
        }

        map<string, string> wire;
        wire["signal"] = result[index+1];
        resolved_map[wire["signal"]] = false;

        if (index == 1) {
            wire["connection_type"] = "DIRECT";
            wire["arg_1"] = result[0];
        } else if (index == 2) {
            wire["connection_type"] = result[0];
            wire["arg_1"] = result[1];
        } else {
            wire["connection_type"] = result[1];
            wire["arg_1"] = result[0];
            wire["arg_2"] = result[2];
        }

        circuit_map[wire["signal"]] = wire;
    }

    for (auto k: circuit_map) {
        resolve(k.first, circuit_map, resolved_map, signal_map);
    }

    for (auto k: circuit_map) {
        cout << k.first << " " << signal_map[k.first] << endl;
    }
}
