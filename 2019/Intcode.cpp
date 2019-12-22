#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

class Intcode {

    public:

        // Load a set of instructions into the machine
        //  Resets the instruction and relative pointers
        //  Clears the input queue
        void load_sequence(string instruction_sequence);

        void execute();  // Begin instruction execution
        void receive(long immediate);   // Queue a number into the input vector

        bool halted_temporary();  // Check if waiting on a value
        bool halted_terminal();   // Check if halted

    private:

        map<long, long> memory; // Intcode memory
        long ins_ptr;   // Instruction pointer
        long rel_ptr;   // Relative pointer

        // A queue of values to be processed by code (3) instructions
        vector<long> in;

        bool waiting = false;   // Not done, waiting on prior Intcode to send
        bool halted = false;    // Instruction set completed - halted

        // The next opcode of the next operation
        int operation;

        // Registers
        long r1, r2, r3;

        // Respective register modes
        //  0 = address, 1 = immediate, 2 = relative
        long p1, p2, p3;

        // Load the next instruction from memory (as denoted by ins_ptr)
        //  Initializes all registers and modes
        void load_instruction();

        // Get the value denoted by a register and mode
        long load_register(long r, int mode);

        // ***** Instructions *****
        void add(); // 1 - Add
        void mul(); // 2 - Multiply
        void set(); // 3 - Set a register
        void out(); // 4 - Output a register value
        void bgz(); // 5 - Branch to r2 if r1 > 0
        void bez(); // 6 - Branch to r2 if r1 == 0
        void slt(); // 7 - Set r3 to r1<r2
        void seq(); // 8 - Set r3 to r1==r2
        void srl(); // 9 - Set the relative instruction pointer

        void exit(); // 99 - Terminate

        // Get the next inputted value from the input vector
        long get_next();

        // Used to chain together multiple Intcode machines
        vector<long> * next = nullptr;
};

void Intcode::load_sequence(string instructions) {
    stringstream convert(instructions);
    vector<long> seq;

    long r = 0;
    while (convert.good()) {
        string ins;
        getline(convert, ins, ',');
        stringstream code(ins);
        long x;
        code >> x;
        memory[r] = x;
        r++;
    }

    ins_ptr = 0;
    rel_ptr = 0;
    in.clear();
}

void Intcode::load_instruction() {
    int code = memory[ins_ptr];
    operation = code % 100;
    code /= 100;

    p1 = code % 10;
    code /= 10;
    p2 = code % 10;
    code /= 10;
    p3 = code;

    r1 = load_register(memory[ins_ptr+1], p1);
    r2 = load_register(memory[ins_ptr+2], p2);
    r3 = load_register(memory[ins_ptr+3], p3);
}

long Intcode::load_register(long r, int mode) {
    if (mode == 0) {
        return memory[r];
    } else if (mode == 1) {
        return r;
    } else if (mode == 2) {
        return memory[rel_ptr+r];
    } else {
        cout << "REGISTER DECODE ERROR" << endl;
        return 0;
    }
}

void Intcode::execute() {
    while (!waiting && !halted) {

        load_instruction();

        switch (operation) {
            case (1):   // Add
                add();
                break;
            case (2):   // Multiply
                mul();
                break;
            case (3):   // Set a register
                set();
                break;
            case (4):   // Output a register value
                out();
                break;
            case (5):   // Branch to r2 if r1 > 0
                bgz();
                break;
            case (6):   // Branch to r2 if r1 == 0
                bez();
                break;
            case (7):   // Set r3 to r1<r2
                slt();
                break;
            case (8):   // Set r3 to r1==r2
                seq();
                break;
            case (99):  // Terminate
                exit();
                break;
            default:
                cout << "READ ERROR" << endl;
                break;
        };
    }
}

void Intcode::receive(long immediate) {
    in.push_back(immediate);
}
    
bool Intcode::halted_temporary() {
    return waiting;
}

bool Intcode::halted_terminal() {
    return halted;
} 

void Intcode::add() {
    memory[r3] = r1 + r2;
}

void Intcode::mul() {
    memory[r3] = r1 * r2;
}

void Intcode::set() {
    if (in.size() == 0) {
        waiting = true;
        return;
    }

    memory[r1] = get_next();
}

void Intcode::out() {
    if (next == nullptr) {
        cout << r1 << endl;
        return;
    }

    (*next).push_back(r1);
}

void Intcode::bgz() {
    ins_ptr = (r1 > 0 ? r2 : ins_ptr+3);
}

void Intcode::bez() {
    ins_ptr = (r1 == 0 ? r2 : ins_ptr+3);
}

void Intcode::slt() {
    memory[r3] = (r1 < r2 ? 1 : 0);
}

void Intcode::seq() {
    memory[r3] = (r1 == r2 ? 1 : 0);
}

void Intcode::exit() {
    halted = true;
}

void Intcode::srl() {
    rel_ptr += r1;
}

long Intcode::get_next() {
    if (in.size() == 0) 
        return -1;
    long n = in.front();
    reverse(in.begin(), in.end());
    in.pop_back();
    reverse(in.begin(), in.end());
}
