#include <iostream>

using namespace std;

int count(string str, string sub) {
    if (str.find(sub) == string::npos) return 0;
    else return 1 + count(str.substr(str.find(sub)), sub);
}

int main() {
    string line;
    int code = 0, memory = 0;
    while (getline(cin,  line)) {
        code += line.size();
        int temp = 0;
        char cursor = 1;
        while (cursor < line.size()-1) {
            temp++;
            if (line.at(cursor) == '\\') {
                if (line.at(cursor+1) == '\\') cursor += 2;
                else if (line.at(cursor+1) == '\"') cursor += 2;
                else if (line.at(cursor+1) == 'x') cursor += 4;
            } else {
                cursor++;
            }
        } memory += temp;
    } cout << code - memory << endl;
}