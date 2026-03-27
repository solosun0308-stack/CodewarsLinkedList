def loop_size(node):
    turtle = node.next
    rabbit = node.next.next
    
    while turtle != rabbit:
        turtle = turtle.next
        rabbit = rabbit.next.next
    
    count = 1
    rabbit = turtle.next
    while turtle != rabbit:
        rabbit = rabbit.next
        count += 1
        
    return count
