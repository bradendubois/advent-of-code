#include <iostream>
#include <map>
#include <vector>
#include <math.h>

using namespace std;

int detection(int x, int y, int rows, int cols, map<int, map<int, bool>> asteroids) {
    int count = 0;
    map<double, bool> angle_block;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (i == y && j == x) continue;

            if (asteroids[i][j]) {
                double angle = 2 * atan2(y-i, x-j);
                if (!angle_block[angle]) count++;
                angle_block[angle] = true;
            }
        }
    }
    return count;
}

int main() {

    map<int, map<int, bool>> asteroids;
    int map_rows, map_cols;

    int row = 0;
    string line;
    while (getline(cin, line)) {
        int col = 0;
        map_cols = line.size();
        for (auto c : line) {
            if (c == '#') asteroids[row][col] = true;
            col++;
        } row++;
    } map_rows = row;

    int best = 0;
    for (int station_x = 0; station_x < map_rows; station_x++) {
        for (int station_y = 0; station_y < map_cols; station_y++) {
            if (asteroids[station_y][station_x])
            best = max(best, detection(station_x, station_y, map_rows, map_cols, asteroids));
        }
    }
    cout << best << endl;
}