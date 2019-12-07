#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

int signal(vector<int> & inputs) {
    string line = "3,8,1001,8,10,8,105,1,0,0,21,46,63,76,97,118,199,280,361,442,99999,3,9,102,4,9,9,101,2,9,9,1002,9,5,9,101,4,9,9,102,2,9,9,4,9,99,3,9,101,5,9,9,102,3,9,9,101,3,9,9,4,9,99,3,9,1001,9,2,9,102,3,9,9,4,9,99,3,9,1002,9,5,9,101,4,9,9,1002,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,5,9,101,3,9,9,1002,9,5,9,1001,9,5,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99";
    stringstream convert(line);
    vector<int> seq;

    while (convert.good()) {
        string ins;
        getline(convert, ins, ',');
        stringstream code(ins);
        int x;
        code >> x;
        seq.push_back(x);
    }

    int ins_ptr = 0;

    while (1) {
        int ins = seq[ins_ptr];

        int opcode = ins % 100;
        ins /= 100;
        
        int p1, p2, p3;
        p1 = ins % 10;
        ins /= 10;
        p2 = ins % 10;
        ins /= 10;
        p3 = ins;

        //cout << opcode << " : " << p1 << " : " << p2 << " : " << p3 << endl;
        int r1, r2, r3, in;
        switch (opcode) {
            case 1:
                r1 = seq[ins_ptr+1];
                r2 = seq[ins_ptr+2];
                r3 = seq[ins_ptr+3];

                r1 = p1 ? r1 : seq[r1];
                r2 = p2 ? r2 : seq[r2];

                seq[r3] = r1 + r2;
                ins_ptr += 4;
                break;
            case 2:
                r1 = seq[ins_ptr+1];
                r2 = seq[ins_ptr+2];
                r3 = seq[ins_ptr+3];

                r1 = p1 ? r1 : seq[r1];
                r2 = p2 ? r2 : seq[r2];

                seq[r3] = r1 * r2;
                ins_ptr += 4;
                break;
            case 3:
                r1 = seq[ins_ptr+1];
                in = inputs.back();
                inputs.pop_back();
                seq[r1] = in;
                ins_ptr += 2;
                break;
            case 4:
                r1 = seq[ins_ptr+1];
                // cout << seq[r1] << endl;
                return seq[r1];
                ins_ptr += 2;
                break;
            case 5:
                r1 = seq[ins_ptr+1];
                r2 = seq[ins_ptr+2];
                
                r1 = p1 ? r1 : seq[r1];
                r2 = p2 ? r2 : seq[r2];

                if (r1 > 0) ins_ptr = r2;
                else ins_ptr += 3;
                break;
            case 6:
                r1 = seq[ins_ptr+1];
                r2 = seq[ins_ptr+2];

                r1 = p1 ? r1 : seq[r1];
                r2 = p2 ? r2 : seq[r2];

                if (r1 == 0) ins_ptr = r2;
                else ins_ptr += 3;
                break;
            case 7:
                r1 = seq[ins_ptr+1];
                r2 = seq[ins_ptr+2];
                r3 = seq[ins_ptr+3];

                r1 = p1 ? r1 : seq[r1];
                r2 = p2 ? r2 : seq[r2];

                if (r1 < r2) seq[r3] = 1;
                else seq[r3] = 0;
                ins_ptr += 4;
                break;
            case 8:
                r1 = seq[ins_ptr+1];
                r2 = seq[ins_ptr+2];
                r3 = seq[ins_ptr+3];

                r1 = p1 ? r1 : seq[r1];
                r2 = p2 ? r2 : seq[r2];

                if (r1 == r2) seq[r3] = 1;
                else seq[r3] = 0;
                ins_ptr += 4;
                break;
            case 99:
                return 0;
            default:
                cout << "READ ERROR : " << opcode << endl;
                return 0;
        }
    }
}

vector<int> make(int a, int b) {
    vector<int> v;
    v.push_back(a);
    v.push_back(b);
    return v;
}

int main() {
    int a, b, c, d, e, best = 0;
    
    // Only horror lies ahead
    while (cin >> a >> b >> c >> d >> e) {
        vector<int> in = make(0, a);
        int result = signal(in);
        in = make(result, b);
        result = signal(in);
        in = make (result, c);
        result = signal(in);
        in = make(result, d);
        result = signal(in);
        in = make(result, e);
        result = signal(in);
        if (result > best) best = result;
    }

    cout << best << endl;
}