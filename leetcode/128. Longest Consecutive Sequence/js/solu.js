/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
  if (nums.length == 0) {
    return 0
  }
  theSet = new Set(nums)
  console.log('theSet: ', theSet)
  nums = []
  for (let it of theSet) {
    console.log('set: ', it, typeof it)
    nums.push(parseInt(it) )
  }
  nums = nums.sort((a, b) => {
    return a - b;
  } )
  // console.log('nums: ', nums)

  let maxcon = 0; 
  let curcon = 1;

  for (it = 0; it < nums.length; it++) {
    if (it == 0) {
      curcon = 1
      continue
    }
    delta = nums[it] - nums[it-1]
    // print('delta: ', delta)
    if (1==delta) {
      curcon += 1
    } else {
      // if end of streak, set maxcon to new max.
      maxcon = Math.max(maxcon, curcon)
      // console.log('maxcon: ', maxcon)
      curcon = 1
    }
  }
  // end of for loop,
  maxcon = Math.max(maxcon, curcon)
  // console.log('maxcon: ', maxcon)
  curcon = 1
  return maxcon

};


nums = [0,3,7,2,5,8,4,6,0,1]
nums = [100,4,200,1,3,2]
ret = longestConsecutive(nums) 
console.log('ret: ', ret)
