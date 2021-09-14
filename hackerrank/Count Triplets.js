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

// Complete the countTriplets function below.
function countTriplets(arr, r) {
    
    function insertMap(theMap, inp) {
        // console.log('inp: ', inp)
        let val = Number(inp)
        if (theMap.has(val) ) {
            let newVal = Number(theMap.get(val) + 1)
            // console.log('theMap[val], ', theMap.get(val), ', newVal: ', newVal)
            theMap.set(val, newVal)
        } else {
            theMap.set(val, 1)
        }
        
    }
    function getOccurenceMap(arr) {
        let occurMap = new Map();
        for (let it = 0; it < arr.length; it++) {
            insertMap(occurMap, arr[it])
        }
        console.log('occurMap:', occurMap)
        return occurMap;
    }    
    
    console.log('r = ', r, ' arr: ', arr)
    let rightMap = getOccurenceMap(arr)
    let leftMap = new Map()
    let numOfPairs = 0
    for (let it = 0; it < arr.length; it++) {
        let val = arr[it]
        let leftCnt = 0
        let rightCnt = 0
        let lhs = 0
        let rhs = r * val
        if (val % r == 0) {
            lhs = val / r
        }
        let occur = rightMap.get(val)
        rightMap.set(val, occur - 1)
        
        if (rightMap.has(rhs) ) {
            rightCnt = rightMap.get(rhs)
        }
        if (leftMap.has(lhs) ) {
            leftCnt = leftMap.get(lhs)
        }
        numOfPairs += leftCnt * rightCnt
        // console.log( 'val: ', val, ', lhs: ', lhs, ', rhs: ', rhs, ', rightMap: ', rightMap, ', leftMap: ', leftMap)
        // console.log('left: ', leftCnt, ', right: ', rightCnt, ' num: ', numOfPairs)
        insertMap(leftMap, val)
        // console.log('leftMap: ', leftMap, '\n')
    }
    
    
    console.log(numOfPairs)
    return numOfPairs


}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const nr = readLine().replace(/\s+$/g, '').split(' ');

    const n = parseInt(nr[0], 10);

    const r = parseInt(nr[1], 10);

    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    const ans = countTriplets(arr, r);

    ws.write(ans + '\n'); 

    ws.end();
}
