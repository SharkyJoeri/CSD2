#include <iostream>
#include "instrument_class_definition.h"
using namespace std;

void Instrument::play() {
    cout << sound << endl;
};

void Instrument::roll(int times) {
    int i = 0;
    do {
        play();
        i++;
        } while (i < times); 
};



