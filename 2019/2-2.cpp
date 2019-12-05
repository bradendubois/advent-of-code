#include <iostream>
#include <map>
#include <vector>
#include <sstream>

using namespace std;

int process(vector<int> & op) {
    int a, b, c, d; 

    int cur = 0;
    while (op[cur] != 99) {
        a = op[cur], b = op[cur+1], c = op[cur+2], d = op[cur+3];

        if (a == 1) {
            op[d] = op[b] + op[c];
        } else if (a == 2) {
            op[d] = op[b] * op[c];
        } else {
            cout << "READ ERROR : Unexpected error in parsing" << endl;
            return 0;
        }

        cur += 4;
    }

    return op[0];
}

// 2019 - Day 2 - Part 2
int main() {
    string sequence;
    cin >> sequence;
    vector<int> op;
    
    // Convert the big string int a clean vector of ints
    stringstream ss(sequence);
    string code_str;

    while (ss.good()) {
        getline(ss, code_str, ',');
        stringstream convert(code_str);
        int code;
        convert >> code;
        op.push_back(code);
    }

    int target = 19690720;

    for (int first = 0; first <= 99; first++) {
        for (int second = 0; second <= 99; second++) {
            
            vector<int> opcopy;
            for (auto i : op) opcopy.push_back(i);
            opcopy[1] = first, opcopy[2] = second;
            
            if (process(opcopy) == target) {
                cout << first << " : " << second << endl;
                return 0;
            }
        }
    }
}