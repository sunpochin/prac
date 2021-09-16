
// frankzanesand 2 years ago
// If anyone is interested, this is the code I used for python (I was stuck on this for about a week so tried to explain my logic as clear as possible!). Give me some pointers if you have them, relatively new to coding.

// # Complete the minimumSwaps function below.
// def minimumSwaps(arr,n,swaps=0):
//     #iterate over entire array
//     for i in range(0,n):
//         #it's good practice to use a boolean guided function in a long for loop,
//         #while will evaluate and IF the statement in it is true it will continue
//         #I used the consecutive, increasing values to swap by index
//         while arr[i] != (i+1):
//             #temp is the correct index of arr[i]
//             temp = arr[i]-1
//             #swap this with whatever element is where arr[temp] is, this will
//             #continue to swap until arr[i] == index+1
//             arr[i], arr[temp] = arr[temp], arr[i]
//             #increase swaps
//             swaps+=1
//     return swaps


'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the minimumSwaps function below.
function minimumSwaps(arr) {
    let theHash = {}
    for (let it = 0; it < arr.length; it++) {
        theHash[arr[it]] = it
    }
    // console.log('theHash: ', theHash)
    let swaps = 0    
    for (let i = 0; i < arr.length; i++) {
        if(arr[i] != i+1) {
            let change = arr[i] - 1
            let tmp = arr[i]
            arr[i] = arr[change]
            arr[change] = tmp
            swaps += 1
            console.log('i: ', i, ', change: ', change)
            console.log('arr: ', arr)
        }
    }
    console.log(swaps)
    return swaps

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine(), 10);

    const arr = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));

    const res = minimumSwaps(arr);

    ws.write(res + '\n');

    ws.end();
}
