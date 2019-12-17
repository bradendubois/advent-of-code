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
        memory += line.size();
        int temp = 2;
        for (auto c : line) {    
            if (c == '\\') temp += 2;
            else if (c == '"') temp += 2;
            else temp++;
        } code += temp;
    } cout << code - memory << endl;
}