#include <iostream>
#include <map>
#include <vector>
#include <sstream>

using namespace std;

// 2019 - Day 2 - Part 1
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

    cout << op[0] << endl;
}