// you can use includes, for example:
#include <algorithm>
#include <math.h>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)
    int nProductRight = 1;

    std::sort(A.begin(), A.end() );
    
    int nSize = A.size();
    for (auto niter = nSize - 3; niter < nSize; ++niter ) {
//        cout << "A[niter] : " << A[niter] << endl;
        nProductRight = nProductRight * A[niter];
    }
    

    //  https://github.com/XavierTalpe/codility/blob/master/src/main/java/lesson4/MaxProductOfThree.java    
    // After sorting the largest product can be found as a combination of the last 
    // three elements. Additionally, two negative numbers add to a positive, 
    // so by multiplying the two largest negatives with the largest positive, 
    // we get another candidate. If all numbers are negative, 
    // the three largest (closest to 0) still get the largest element!


    int nProductLeft = 1;
    nProductLeft = A[nSize - 1] * A[0] * A[1];
    int value = std::max(nProductLeft, nProductRight);
    return value;
}


// test case: [-6, -5, -4, -3, -2, -1]
