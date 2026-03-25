from preloaded import Node

def get_nth(node, index):
    if not node or index < 0:
        raise Exception("Invalid index value should throw error.")
    
    curr = node
    counter = 0
    
    while curr:
        if counter == index:
            return curr
        
        curr = curr.next
        counter += 1
    
    raise Exception("Index out of bounds")
