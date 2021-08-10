// you can use includes, for example:
#include <algorithm>
#include <math.h>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)

    std::sort(A.begin(), A.end() );
    int nCurValue = -1111111;
    int nDistinctCnt = 0;
    int nSize = A.size();
    for (auto niter = 0; niter < nSize; ++niter ) {
//        cout << "A[niter] : " << A[niter] << endl;
        if (A[niter] != nCurValue) {
            nCurValue = A[niter];
            ++nDistinctCnt;
        }
    }
    return nDistinctCnt;
    
}


