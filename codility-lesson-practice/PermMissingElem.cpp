// PermMissingElem.cpp

// you can use includes, for example:
// #include <algorithm>
#include <set>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)
    
    // 1. get the max, P = N + 1
    int nMax = A.size() + 1;
    
    // 2. make a array counting from 1 to P
    // https://stackoverflow.com/questions/11965732/set-stdvectorint-to-a-range
    // std::vector<int> vfull(nmax);
    // std::iota(vfull.begin(), vfull.end(), 1);

    std::set<int> setFull;
    for (auto niter = 1; niter < nMax; ++niter) {
        setFull.insert(niter);
    }
    
    // 3.
    for (auto niter = 0; niter < A.size(); ++niter) {
        setFull.erase(A[niter]);
    }
    std::set<int>::iterator setit = setFull.begin();
    int setvalue = *setit;
    return setvalue;

}

