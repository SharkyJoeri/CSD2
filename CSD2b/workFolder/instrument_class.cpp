#include <iostream>
using namespace std;

class Instrument {
    public:
        string sound = "Badabadi";

        void play() {
            cout << sound << endl;
        }

        void roll(int times) {
            int i = 0;
            do {
                play();
                i++;
            } while (i < times); 
        }

};

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

