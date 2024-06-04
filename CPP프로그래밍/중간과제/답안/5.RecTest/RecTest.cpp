#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 20;
    int &aRef = a;          // a를 참조하는 참조 변수 aRef를 선언
    cout << "a의 값 : " << a << endl;
    cout << "aRef가 참조하는 값 : " << aRef << endl << endl;
    aRef = 100;
    cout << "a의 값 : " << a << endl;
    aRef = b;
    cout << "a의 값 : " << a << endl;
    return 0;
}

// ㄱ : int &aRef = a;