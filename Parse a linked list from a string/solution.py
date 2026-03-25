from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    parts = list_repr.split(" -> ")
    
    curr = None
    
    for i in range(len(parts) - 2, -1, -1):
        curr = Node(int(parts[i]), curr)
        
    return curr
