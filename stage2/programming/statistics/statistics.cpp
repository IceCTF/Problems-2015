#include <iostream>
#include <cstdlib>
#include <cmath>
#include <string>
using namespace std;

string queries[] = {"minimum", "maximum", "average", "sum"};

int main(){
    int len, min, max, sum, x, q, a;
    double av;
    for(int i=0;i<200;i++){
        len = rand() % ((i+1)*10);
        min=1000000;
        max = sum = 0;

        for(int j=0;j<len;j++){
            if(j != 0) cout << " ";
            x = rand() % 10000;
            if(x>max) max =x;
            if(x<min) min=x;
            sum += x;
            cout << x;

        }
        cout << endl;
        q = rand() % 4;
        cout << "Gimme the " << queries[q] << " of all the numbers: ";
        if(q != 2) {
            cin >> a;
            if((q == 0 && min != a) || (q == 1 && max != a) || (q == 3 && sum != a)) {
                cout << "Incorrect." << endl;
                return 0;
            }
        } else {
            cin >> av;
            if(abs((static_cast<double>(sum)/len) - av) > 1e-5) {
                cout << "Incorrect." << endl;
                return 0;
            }
        }
    }
    cout << "Welcome Daniel!" << endl;
    cout << "The flag is: why_is_there_code_in_my_statistics" << endl;
}
