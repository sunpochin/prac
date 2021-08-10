// you can use includes, for example:
// #include <algorithm>
#include <stack>
// https://github.com/jlhuang/codility-lessons/blob/master/lesson%205%20:%20Stacks%20and%20Queues/Fish/Solution.java

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(vector<int> &A, vector<int> &B) {
    // write your code in C++14 (g++ 6.2.0)
    int naliveUp = 0;
    
    stack<int> alivedown;
    int niter = 0;
    for (niter = 0; niter < B.size(); ++niter ) {
        int sizealive = alivedown.size();
        // current fish is flowing upstream and there isn't fish flowing
        // downstream before
        cout << "niter++; alivedown.size()  " <<  alivedown.size() << endl;
        if (0 == B[niter] && 0 == alivedown.size() ) {
            naliveUp++;
            cout << "naliveUp++;;" << endl;
        } else if ( 0 == B[niter] && 0 != alivedown.size() ) {
            // current fish flowing upstream eats the fish flowing
            // downstream before            
            while (!alivedown.empty() && A[niter] > alivedown.top() ) {
                alivedown.pop();
                cout << "alivedown.pop();" << endl;
            }
            // all the fish flowing downstream is eaten by the current fish
            // flowing upstream
            if (0 == alivedown.size() ) {
                naliveUp++;
                cout << "naliveUp++;;" << endl;
            }
        } else {
            // there is a fish flowing downstream and push it into the stack
            alivedown.push(A[niter]);
            cout << "alivedown.push(A[niter]);  niter == " << niter << endl;
        }
    }
    
    int ncnt = naliveUp + alivedown.size();
    return ncnt;

}

