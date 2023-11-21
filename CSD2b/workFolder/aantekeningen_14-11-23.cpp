//aantekeningen 14/11/23
#include <iostream>

class Woofer {
    public:
        float diameter;
        int impedance;
        float maxPower;
        //Material material;
        float conePosition;

        void move(float position) {
            conePosition = position;
            std::cout << "Woofer position" << conePosition << std::endl;
        }
};

int main() {
    Woofer myWoofer1;
    myWoofer1.move(0.05);
    myWoofer1.diameter=12.0;

    Woofer myWoofer2;
    myWoofer2.move(0.05);
    myWoofer2.diameter=12.0;
};
    

/* 
bigger comments
over
multiple
lines
*/



