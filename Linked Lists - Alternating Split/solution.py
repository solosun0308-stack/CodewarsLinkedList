class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if not head or not head.next:
        raise Exception("List must have at least two nodes to split")

    first_head = head
    second_head = head.next
    
    curr_first = first_head
    curr_second = second_head
    
    current = second_head.next
    
    count = 0
    while current:
        if count % 2 == 0:
            curr_first.next = current
            curr_first = curr_first.next
        else:
            curr_second.next = current
            curr_second = curr_second.next
        
        current = current.next
        count += 1
        
    curr_first.next = None
    curr_second.next = None
    
    return Context(first_head, second_head)
