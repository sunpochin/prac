// you can use includes, for example:
// #include <algorithm>
#include <stack>
#include <string>
// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(string &S) {
    // write your code in C++14 (g++ 6.2.0)
    
    int nret = 0;
    cout << "S :" << S <<endl;
    
    //    { [ (
    stack<char> istack;
    
    const int nSize = S.size();
    for (int niter = 0; niter < nSize; ++niter) {
        if ('{' == S[niter] || '[' == S[niter] || '(' == S[niter]) {
            istack.push(S[niter]);
        }
        // if ('[' == S[niter]) {
        //     istack.push(S[niter]);
        // }
        // if ('(' == S[niter]) {
        //     istack.push(S[niter]);
        // }

        if ('}' == S[niter] && '{' == istack.top() ) {
            istack.pop();
        }
        if (']' == S[niter] && '[' == istack.top() ) {
            istack.pop();
        }
        if (')' == S[niter] && '(' == istack.top() ) {
            istack.pop();
        }
    }
    int nStackSize = istack.size();
    if (0 == nStackSize) {
        nret = 1;
    } else {
        nret = 0;
    }

    
    return nret;    
}