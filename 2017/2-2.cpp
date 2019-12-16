#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int main() {
    string line;
    int checksum = 0;
    while (getline(cin, line)) {
        stringstream conv(line);
        vector<int> vals;
        int val;
        while (conv >> val) vals.push_back(val); 
        
        for (auto a : vals)
            for (auto b : vals)
                if (a != b && a % b == 0)
                    checksum += a / b;    
    } cout << checksum << endl;
}