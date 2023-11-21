#include <iostream>
// #include "instrument_class_implimentation.cpp"
#include "instrument_class_definition.h"
using namespace std;

int main() {
    //  user input
    cout << "How many times to play the sound?" << endl;
    int input;
    cin >> input;

    //  playing 'sound'
    Instrument playSound;
    playSound.roll(input);
    return 0;
}

