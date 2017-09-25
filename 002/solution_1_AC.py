# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = l1
        carry = 0
        while True:
            s = l1.val + l2.val + carry
            l1.val = s % 10
            carry = s / 10
            if l1.next is None and l2.next is None:
                if carry != 0:
                    l1.next = ListNode(carry)
                break
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)
            l1 = l1.next
            l2 = l2.next
        return result


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    
    l3 = Solution().addTwoNumbers(l1, l2)
    while l3.val is not None:
        print l3.val,
        if l3.next is not None:
            print ' -> ',
            l3 = l3.next
        else:
            break
