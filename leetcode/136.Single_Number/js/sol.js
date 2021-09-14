

/**
 * @param {number[]} nums
 * @return {number}
 */
 var singleNumber = function(nums) {
  let theSet = new Set()
  for(let it = 0; it < nums.length; it++) {
    if (!theSet.has(nums[it]) ) {
      theSet.add(nums[it])
    } else {
      theSet.delete(nums[it])
    }
  }
  let ans
  for (let it of theSet) {
      ans = it
  }
  console.log('ans: ', ans)
  return ans
};

// inp = [1, 2, 2]
// ret = singleNumber(inp)
// console.log('ret: ', ret)
