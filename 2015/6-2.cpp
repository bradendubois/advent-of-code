#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int main() {
    string ins;
    vector<vector<int>> grid(1000, vector<int>(1000));

    while (getline(cin, ins)) {
        string temp;
        int x1, x2, y1, y2, op;

        if (ins.find("toggle ") != string::npos) {
            temp = ins.substr(7);
            op = 2;
        } else if (ins.find("turn on ") != string::npos) {
            temp = ins.substr(8);
            op = 1;
        } else {
            temp = ins.substr(9);
            op = -1;
        }

        string temp_x;

        stringstream left(temp.substr(0, temp.find(" ")));
        getline(left, temp_x, ',');
        x1 = stoi(temp_x);
        getline(left, temp_x, ',');
        y1 = stoi(temp_x);
        
        stringstream right(temp.substr(temp.find("through ")+8));       
        getline(right, temp_x, ',');
        x2 = stoi(temp_x);
        getline(right, temp_x, ',');
        y2 = stoi(temp_x);
        
        for (int row = x1; row <= x2; row++) {
            for (int col = y1; col <= y2; col++) {
                grid[row][col] = max(grid[row][col] + op, 0);
            }
        }        
    }

    int lit = 0;
    for (auto row : grid) {
        for (auto col : row) {
            lit += col;
        }
    }
    cout << lit << endl;
}