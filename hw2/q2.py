function is_balanced(node):
    if node is null: # if node is empty, these means that this is last node
        return true
    
    left_height = height_of_tree(node.left) # call for left
    right_height = height_of_tree(node.right) # call for right

    # this line, we find the height of left and right
    if abs(left_height - right_height) > 1: 
        return false

    return is_balanced(node.left) && is_balanced(node.right)


function height_of_tree(node): 
    if node is null: # tree node does not exist
        return -1

    left_height = height_of_tree(node.left)
    right_height = height_of_tree(node.right)

    return 1 + max(left_height, right_height) # max of size + root


