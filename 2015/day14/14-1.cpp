#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int main() {

    int speed, fly, rest, N, temp, flown, max = INT32_MIN;
    bool resting;
    string line, reindeer;
    while (getline(cin, line)) {
        
        istringstream conv(line);
        vector<string> result;
        for (string s; conv >> s;) {
            result.push_back(s);
        }

        reindeer = result[0];
        speed = stoi(result[3]); 
        fly = stoi(result[6]); 
        rest = stoi(result[13]);

        flown = 0;
        resting = false;
        temp = fly;
        N = 2503;
        while (N--) {

            if (!resting) {
                flown += speed;
            }

            temp--;

            if (temp == 0) {
                resting = !resting;

                if (resting) {
                    temp = rest;
                } else {
                    temp = fly;
                }
            }
        }

        if (flown > max) {
            max = flown;
        }
    }

    cout << max << endl;
}