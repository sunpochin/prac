// you can use includes, for example:
#include <algorithm>
#include <set>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)

    // 1. find the max value in vector A.
    auto it = max_element(std::begin(A), std::end(A) ); // c++11
    int maxvalue = *it;
//    cout << "value : " << maxvalue << endl;
    
    // 2. make a set of sequence 1 to maxvalue
    std::set<int> setFull;
    std::vector<int> vecFull;
    for (auto niter = 1; niter <= maxvalue; ++niter) {
        vecFull.push_back(niter);
    }

    // 3. remove duplicates from vector A.
    set<int> s;
    vector<int> vec = A;
    unsigned size = vec.size();
    for( unsigned i = 0; i < size; ++i ) {
        s.insert( vec[i] );
    }

    // 3. find the smallest positive integer  missing in maxvalue
    //   if available, return it. 
    //   if not, return maxvalue + 1.
    for (auto niter = 0; niter < vecFull.size(); ++niter) {
        int nErase = s.erase(vecFull[niter]);
        if (0 == nErase) {
 //           cout << " return value is "<< vecFull[niter] << endl;
            return vecFull[niter];
        }
    }

//    cout << " return value is "<< maxvalue + 1 << endl;
    int returnValue = maxvalue + 1;
    if (returnValue <= 0) {
        returnValue = 1;
    }
    return returnValue;
    
}

