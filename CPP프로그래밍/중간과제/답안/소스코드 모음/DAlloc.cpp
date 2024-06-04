#include <iostream>
using namespace std;

int main() {
    int *intPtr;
    intPtr = new int[4]; // 4개의 int 값을 저장할 메모리 할당
    *intPtr = 10;
    *(intPtr + 1) = 20;
    intPtr[2] = 30;
    intPtr[3] = 40;
    for (int *p = intPtr, i = 0; i < 4; i++)
        cout << *p++ << " "; // p가 가리키는 곳의 값을 출력한 후 p를 다음으로 이동

    cout << endl;

    delete [] intPtr; // (ㄱ)에서 할당한 메모리 반환
    intPtr = nullptr;

    return 0;
}

/*
 ㄱ: intPtr = new int[4];
 ㄴ: *p++
 ㄷ: delete [] intPtr; intPtr = nullptr;
*/