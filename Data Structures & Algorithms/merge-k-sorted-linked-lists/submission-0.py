from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # edge case first
        if not lists or len(lists) == 0:
            return None

        # take pairs and merge until 1 is remaining which is output
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next





        # use some basic ideas to solve it efficiently

        # 4 single linked lists

       # 5 7 3 8

        #how to merge in an efficient way

        # 5 merges with 7
        # now merge 3, so we put 3 in the front
        # 3 5 7
        # last value, 8, look at the 3, bigger than the 3, 5, and 7, so its put at the end
        # iteration through every single node where to put A


        #merging into output is not super efficient

        #total number of nodes we have is N

        #could be o(k*n)

        #so why merge as a tree.
        #very repetitious
        #merge sort algorithm there is a better way to do this

        #work in pairs

        #merge 5 7, merge 3 and 8
        #then merge A and B
        # then algorithm to merge two linked lists
        #before its still o(n)
        #k-> log(k) because we are dividing by two each time.

       # total time complexity is nlogk, much better than n*k
