#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> lookandsay(vector<int> in) {
    vector<int> newVec;
    int prev = in.front();
    int run = 0;
    for (auto i: in) {
        if (i == prev) run++;
        else {
            newVec.push_back(run);
            newVec.push_back(prev);
            run = 1;  
        } prev = i;
    } 
    newVec.push_back(run);
    newVec.push_back(prev);
    return newVec;
}

int main() {
    vector<int> vec{1, 1, 1, 3, 2, 2, 2, 1, 1, 3};
    int n = 40;
    while (n--) vec = lookandsay(vec);
    cout << vec.size() << endl;
}