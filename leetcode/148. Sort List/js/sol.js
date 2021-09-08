/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
 var sortList = function(head) {
  if (head == null) {
      return null
  }
  
  let nodeCnt = 0
  let dummy = head
  let arr = []
  while(dummy !== null) {
      arr.push(dummy.val)
      dummy = dummy.next
      nodeCnt += 1
  }
  arr = new Float64Array(arr);
  arr.sort()
  // console.log('nodeCnt: ', nodeCnt, ', arr: ', arr)
  // console.log('nodeCnt: ', nodeCnt, ', arr.sort(): ', arr.sort())
//    let newDummy = new ListNode(-1)
  let lastNode
  let curNode
  for (let it = arr.length - 1; it >= 0; it--) {
      if (it == arr.length - 1) {
          curNode = new ListNode(arr[it], null)
      } else {
          curNode = new ListNode(arr[it], lastNode)
      }
      // lastNode = new ListNode(curNode.val, curNode)
      lastNode = curNode 
      // console.log('curNode: ', curNode, ', lastNode, ', lastNode)
  }
  return curNode
};

