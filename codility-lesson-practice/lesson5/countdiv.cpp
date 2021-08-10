// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(int A, int B, int K) {
    // write your code in C++14 (g++ 6.2.0)
    
    int nReturn = 0;
    /// super slow, using division. 
    // for (auto niter = A; niter <= B; ++niter) {
    //     if (0 == niter % K ) {
    //         ++nReturn;
    //     }
    // }

    // a little bit faster, avoid using division.
    // int niter = A;
    // while(true) {
    //     if (0 == niter % K ) {
    //         ++nReturn;
    //         niter += K;
    //     } else {
    //         ++niter;
    //     }
    //     // cout << " niter: " << niter << endl;
    //     if (niter > B) {
    //         // cout << " break. " << endl;
    //         break;
    //     }
    // }

    // fast, but not correct.
    // int diff = B - A;
    // int division = (B - A) / K;
    // if (0 == A % K) {
    //     division += 1;
    // }
    // nReturn = division;
    // return nReturn;

    int inclusive = (A%K == 0) ? 1 : 0;
    return B/K - A/K + inclusive;
    
}




