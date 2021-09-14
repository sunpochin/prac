
// ivanduka 3 years ago
// JavaScript solution (passes all tests):

// The idea is that we count 3 things: 1. Creating a dictionary with all added/removed values as keys and number of elements as values 2. Updating a frequency table 3. Result that we return in the end

// Obvious solution would be to keep only the dictionary. However, then in case 3 every time we need to traverse the whole dictionary to check if there is a key with value that equals the search value;

// It works fine on the initial tests but fails on the main set of tests because traversal of the whole dictionary is expensive.

// OK, then we need to keep an extra list of frequencies. I used a simple array where the index is the number of occurencies, for example [0,2,3] means that there are 2 values which occur twice and 3 values that occur 3 times (dictionary in this case would be something like: {12: 2, 14: 3}

// This way in case 3 I need only to check freq[number of occurencies]






'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the freqQuery function below.
function freqQuery(queries) {
    let theOutput = []
    
    let theMap = new Map()
    let freqSet = new Set()
    
    function pushToMap(theMap, val) {
        if (theMap.has(val) ) {
            let newVal = theMap.get(val) + 1
            theMap.set(val, newVal)
            freqSet.add(newVal)
            freqSet.delete(val)
//            console.log('freqSet: ', freqSet)
        } else {
            theMap.set(val, 1)
            freqSet.add(1)
        }
    }
    function removeFromMap(theMap, val) {
        if (theMap.has(val) ) {
            let newVal = theMap.get(val) - 1
            theMap.set(val, newVal)
            freqSet.add(newVal)
            freqSet.delete(val)
//            console.log('freqSet: ', freqSet)
        } else {
        }
    }
            
    queries.forEach((x) => {
        console.log(x)
        if (x[0] == 1) {
            pushToMap(theMap, x[1])
        } else if (x[0] == 2) {
            removeFromMap(theMap, x[1])
        } else if (x[0] == 3) {
            if ( freqSet.has(x[1]) ) {
                theOutput.push("1")
            } else {
                theOutput.push("0")
            }
        }
//        console.log("theOutput: ", theOutput)
    })
    // console.log(theOutput)    
    return theOutput

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const q = parseInt(readLine().trim(), 10);

    let queries = Array(q);

    for (let i = 0; i < q; i++) {
        queries[i] = readLine().replace(/\s+$/g, '').split(' ').map(queriesTemp => parseInt(queriesTemp, 10));
    }

    const ans = freqQuery(queries);

    ws.write(ans.join('\n') + '\n');

    ws.end();
}
