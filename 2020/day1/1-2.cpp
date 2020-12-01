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
            for (int k = j + 1; k < expenses.size(); k++)
            if (expenses[i] + expenses[j] + expenses[k] == 2020) {
                cout << expenses[i] * expenses[j] * expenses[k] << endl;
                return 0;
            }
        }
    }
}