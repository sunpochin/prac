/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
 var moveZeroes = function(nums) {
  // index to non-zero elements after moving.
  let idx = 0;
  for(let ni = 0; ni < nums.length; ni++) {
      if (nums[ni] !== 0) {
          nums[idx] = nums[ni];
          idx++
      }
  }
  console.log('nums: ', nums)
  for(let ni = idx; ni < nums.length; ni++) {
      nums[ni] = 0;
  }
  console.log('nums: ', nums)
};

let nums = [0,1,0,3,12]
moveZeroes(nums);
