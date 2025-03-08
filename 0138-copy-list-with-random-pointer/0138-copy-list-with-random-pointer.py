"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        #[[7,null],[13,0],[11,4],[10,2],[1,0]]

        if head==None:
            return None
        cur=head
        # inserting newnode in the middle of the main node
        while cur:
            newnode=Node(cur.val) # copied the first val and created a newnode that is 7
            newnode.next=cur.next # new node of 7 is pointing to cur node of nxt i.e 7 => is  13
            cur.next=newnode  # main node 7 is connecting to newnode 7 
            cur=newnode.next # then the main node is shifted
        # giving the pointer to the newnode
        cur=head
        while cur:
            if cur.random !=None:
                cur.next.random=cur.random.next #pointing the random points  
            cur= cur.next.next # moving  to the middle node
        # splitting the main node and newnode
        cur=head # main node i.e first node
        newhead=head.next # next of main node i.e newly created first node
        newcur=newhead # newcur is newnode i.e next of main node i.e newly created first node
        while cur:
            cur.next=newcur.next # just pointing the main node alone
            cur=cur.next # moving the main node alone
            if cur!=None:
                newcur.next=cur.next # pointing the newnode alone
                newcur=newcur.next # moving the newnode alone
        return newhead # returning the newnode 
