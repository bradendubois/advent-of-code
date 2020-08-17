#include <iostream>
#include <vector>
#include <map>
#include <sstream>

using namespace std;

int main() {

    map<string, int> distances;
    map<string, int> points;
    map<string, bool> resting;
    map<string, int> speed;
    map<string, int> fly_time;
    map<string, int> rest_time;
    map<string, int> temp_left;

    vector<string> lead;
    vector<string> reindeers;

    string line, reindeer;
    while (getline(cin, line)) {
        
        istringstream conv(line);
        vector<string> result;
        for (string s; conv >> s;) {
            result.push_back(s);
        }

        reindeer = result[0];
        reindeers.push_back(reindeer);

        points[reindeer] = 0;
        resting[reindeer] = false;
        speed[reindeer] = stoi(result[3]);
        fly_time[reindeer] = stoi(result[6]);
        rest_time[reindeer] = stoi(result[13]);
        temp_left[reindeer] = fly_time[reindeer];
    }

    int N = 2503;
    while (N--) {

        lead.clear();

        for (auto r: reindeers) {
            
            if (!resting[r]) {
                distances[r] += speed[r];
            }

            temp_left[r]--;

            if (temp_left[r] == 0) {

                resting[r] = !resting[r];

                if (resting[r]) {
                    temp_left[r] = rest_time[r];
                } else {
                    temp_left[r] = fly_time[r];
                }
            }

            if (lead.empty() || distances[r] == distances[lead[0]]) {
                lead.push_back(r);
            } else if (distances[r] > distances[lead[0]]) {
                lead.clear();
                lead.push_back(r);
            }
        }

        for (auto r: lead) {
            points[r]++;
        }
    }

    int max = INT32_MIN;
    for (auto r: points) {
        if (r.second > max) {
            max = r.second;
        }
    }

    cout << max << endl;
}