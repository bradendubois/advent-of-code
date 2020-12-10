#include <iostream>
#include <map>
#include <vector>
#include <sstream>

using namespace std;

int cookie_score(vector<string> ingredients, map<string, map<string, int>> stats) {

    map<string, int> totals;

    for (auto cookie: stats) {
        for (auto cookie_value: cookie.second) {
            if (cookie.first.compare("calories") == 0) {
                continue;
            }

            totals[cookie_value.first] += cookie_value.second * cookie.second["percentage"];
        }
    }

    int score = 1;
    for (auto v : totals) {
        if (v.first.compare("calories") == 0) {
            continue;
        }

        if (v.first.compare("percentage") == 0) {
            continue;
        }

        score *= v.second;
    }

    // for (auto c: ingredients) {
    //    score += stats[c]["calories"];
    //}

    cout << score << endl;
    return score;
}

int main() {
    
    vector<string> ingredients;
    map<string, map<string, int>> ingredient_list;

    string line, ingredient, attribute, v;

    while (getline(cin, line)) {
        
        istringstream conv(line);
        vector<string> result;
        for (string s; conv >> s;) {
            result.push_back(s);
        }

        ingredient = result[0];
        ingredient.pop_back();
        ingredients.push_back(ingredient);

        for (int i = 2; i <= 10; i += 2) {
            attribute = result[i-1];
            v = result[i];

            if (i < 10) {
                v.pop_back();
            }

            ingredient_list[ingredient][attribute] = stoi(v);
        }
    }

    int score, max = INT32_MIN;
    for (int a = 0; a <= 100; a++) {
        for (int b = 0; b <= 100; b++) {
            //for (int c = 0; c <= 100; c++) {
                //for (int d = 0; d <= 100; d++) {

                    //if (a + b + c + d != 100) {
                    //    continue;
                    //}

                    if (a + b != 100) continue;

                    ingredient_list[ingredients[0]]["percentage"] = a;
                    ingredient_list[ingredients[1]]["percentage"] = b;
                    //ingredient_list[ingredients[2]]["percentage"] = c;
                    //ingredient_list[ingredients[3]]["percentage"] = d;

                    score = cookie_score(ingredients, ingredient_list);
                    
                    if (score > max) {
                        max = score;
                    }
                //}
            //}
        }
    } cout << max << endl;
}