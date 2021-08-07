// https://leetcode.com/problems/intersection-of-two-arrays/discuss/82187/JavaScript-solution-with-Set

// https://skyyen999.gitbooks.io/-leetcode-with-javascript/content/questions/349md.html

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
 var intersection = function(nums1, nums2) {
  let set1 = new Set()
  let set2 = new Set()
  let ans = new Array()
  
  for (it in nums1) {
      set1.add(nums1[it])
  }
  console.log('set1: ', set1)
  for (it in nums2) {
      if (set1.has(nums2[it])) {
          set2.add(nums2[it])
      }
  }
  console.log('set2: ', set2)
  ans = [...set2];
  return ans
  
  // let arr3 = nums2.filter(n => set1.has(n))
  // let set3 = new Set(arr3)
  // console.log('arr3: ', arr3, ', set3: ', set3, ', [set3]: ', [set3])
  // return [...set3]
};


