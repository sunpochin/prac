// you can use includes, for example:
// #include <algorithm>
#include <stack>
// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(vector<int> &H) {
    // write your code in C++14 (g++ 6.2.0)
    int n = H.size();
    if(n <= 1) {
        return n;
    }
    int res = 0;
    stack<int> istack;
    for(int i = 0; i < n; i++){
        while(!istack.empty() && H[i] < istack.top()) {
            int popvalue = istack.top();
            istack.pop();
            cout << "!istack.empty() && H[i] < istack.top(), istack pop: " << popvalue << "H[i] " << H[i] << endl;
            res++;
        }
        if(istack.empty()) {
            istack.push(H[i]);
            cout << "istack.empty(), push istack : " << H[i] << endl;
            continue;
        }
        if(H[i] > istack.top()) {
            cout << "H[i] > istack.top(), push istack : " << H[i] << endl;
            istack.push(H[i]);
        }
    }
    res += istack.size();
    return res;
}
