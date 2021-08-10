// codility lesson 2: OddOccurrencesInArray

// you can use includes, for example:
#include <algorithm>
#include <set>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)
    
    set<int> setLeft;
    bool nWaitingRightSwitchOn = false;
    
    for (std::vector<int>::iterator it = A.begin() ; it != A.end(); ++it) {
        // try to find *it in the set.
        std::set<int>::iterator findit = setLeft.find(*it);
        if (setLeft.end() == findit) {
            setLeft.insert(*it);
            nWaitingRightSwitchOn = true;
            // std::cout << "insert: " << *it;
            // std::cout << " " << *it << endl;
        } else {
            // remove the value from the set.
            setLeft.erase(*findit);
            nWaitingRightSwitchOn = false;
            // std::cout << "erase: " << *findit;
            // std::cout << " " << *findit << endl;
        }
    }
    std::set<int>::iterator setit = setLeft.begin();
    int setvalue = *setit;
    return setvalue;
}
