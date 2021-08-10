// lesson 1 CyclicRotation.

// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

vector<int> solution(vector<int> &A, int K) {
    // write your code in C++14 (g++ 6.2.0)
//    cout << "in solution : " << A[0] << ", " << A[1] << ", " << A[2] << ", " << A[3] << ", K: " << K << endl;
    
    
    const int nSizeA = A.size();
//    cout << "nSizeA : " << nSizeA << endl;
    
    vector<int> B(nSizeA);
    for (auto iter = 0; iter < K; iter++) {
        for(auto jter = 0; jter < nSizeA; jter++) {
            int nNewPos = (jter + 1) % (nSizeA );
            B[nNewPos] = A[jter];
        }
//        cout << "in inner : " << B[0] << ", " << 
//            B[1] << ", " << B[2] << ", " << B[3] << ", K: " << K << endl;
        A = B;
    }
    return A;
}