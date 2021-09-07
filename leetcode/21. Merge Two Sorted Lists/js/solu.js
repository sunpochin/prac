/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
 function ListNode(val, next) {
  this.val = (val===undefined ? 0 : val)
  this.next = (next===undefined ? null : next)
}


/**
* @param {ListNode} l1
* @param {ListNode} l2
* @return {ListNode}
*/
var mergeTwoLists = function(l1, l2) {
  let dummyHead = new ListNode(-1, null)
  let curHead = dummyHead
  while (l1 && l2) {
      if (l1.val < l2.val) {
          curHead.next = l1
          l1 = l1.next
      } else {
          curHead.next = l2
          l2 = l2.next
      }
      curHead = curHead.next
      // console.log('l1: ', l1, ', l2: ', l2)
      // console.log('curHead: ', curHead)
      // console.log('dummyHead next: ', dummyHead.next)
  }
  // console.log('dummyHead: ', dummyHead.next)
  if (l1 !== undefined)
      curHead.next = l1
  if (l2) {
      curHead.next = l2
  }
  
  return dummyHead.next
  
};
