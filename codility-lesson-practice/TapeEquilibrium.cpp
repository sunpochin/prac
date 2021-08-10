// TapeEquilibrium

// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

#include <limits>
int solution(vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)
    vector<int>::iterator P = A.begin() + 1; //   the used to split the tape.
    
    int imax = std::numeric_limits<int>::max();
    int minDiffValue = imax;
    int nTotal = 0;
    
    for (auto niter = 0; niter < A.size(); ++niter) {
        nTotal = nTotal + A[niter];
    }
    // cout << "nTotal : " << nTotal << endl;
    
    int uppersum = 0;
    for (auto p = 1; p < A.size(); ++p)
    {
        uppersum = uppersum + A[p - 1];
        int lowersum = nTotal - uppersum;

        minDiffValue = min(minDiffValue, abs(uppersum - lowersum) );
        
        cout << "uppsersum : " << uppersum << " lowersum : " << lowersum << endl;
        //cout << "absdiff : " << absdiff << endl;
        
        cout << "minDiffValue : " << minDiffValue << endl;
    }
    
    return minDiffValue;
    
    
}


