#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {

    vector<int> expenses;

    int x;
    while (cin >> x) {
        expenses.push_back(x);
    }

    for (int i = 0; i < expenses.size(); i++) {
        for (int j = i + 1; j < expenses.size(); j++ ) {
            if (expenses[i] + expenses[j] == 2020) {
                cout << expenses[i] * expenses[j] << endl;
                return 0;
            }
        }
    }
}