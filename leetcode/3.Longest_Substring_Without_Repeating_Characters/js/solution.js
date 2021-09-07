// Given a string s, find the length of the longest substring without repeating characters.

// without repeating: use set to detect repeating.

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let beg = 0, end = s.length;
    let maxlong = ""
    let maxlength = 0
    for (let beg = 0; beg < end; beg++) {
        theSet = new Set()
        for (let it = beg; it < end; it++) {
            if (!theSet.has(s[it])) {
                theSet.add(s[it])
                longest = s.substring(beg, it+1)
                if (longest.length > maxlength) {
                    maxlong = longest
                    maxlength = longest.length
                }
                // console.log('longest: ', longest);
            } else {
                break;
            }
            // console.log('theSet: ', theSet);
        }
        // console.log('\n');
    }
    return maxlength;
};

s = "pwwkew"
test = lengthOfLongestSubstring(s)
console.log('test: ', test);

// s = "abcabcbb"
// s = "abcabcde"
// a
// ab
// abc o
// abca x
// b
// bc
// bca o
// bcab x

// abcde


/**
 * @param {string} s
 * @return {number}
 */
 var lengthOfLongestSubstring = function(s) {
//     // ************************
//     // brute force solution
//     // ************************
//     let longestLen = 0
//     for (lptr = 0; lptr <= s.length - 1; lptr += 1) {
//         seenChar = {}
//         curLeng = 0
//         for (rptr = lptr; rptr <= s.length - 1; rptr += 1) {
//             curChar = s[rptr]
// //            console.log('charIdx: ', charIdx)
//             charExist = seenChar[curChar]
//             console.log('curChar: ', curChar, ', charExist: ', charExist)
//             if (!charExist) {
//                 seenChar[curChar] = true
//                 curLeng = rptr - lptr + 1
//                 console.log('rptr: ', rptr, ', lptr: ', lptr)
// //                console.log('!seenChar[curChar]', 'longestLen: ', longestLen)
//             } else {
//                 break
//             }
//         }
//         longestLen = Math.max(longestLen, curLeng)
//         console.log('curLeng: ', curLeng, ', longestLen: ', longestLen)
//     }
//     return longestLen

    // ************************
    // Optimal solution
    // ************************
    lptr = 0, rptr = 0
    seenChar = {}

    while(rptr <= s.length - 1) {
        curChar = s[rptr]
        charExist = seenChar[curChar]
        console.log('charExist: ', charExist)
        if (!charExist) {
            longestLen = rptr - lptr + 1
        }


        rp += 1
    }

    return longestLen

};

