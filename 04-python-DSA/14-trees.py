# if there are no nodes: depth is 0
# if there is a node with no children: depth is 1
# if there is a node with 1 child: depht is 2

# root counts as depth 1

# max depth
def max_depth(root):
    if root is None:
        return 0
    
    max_left = max_depth(root.left)
    max_right = max_depth(root.right)

    return 1 + max(max_left, max_right)

# if binary trees are same:
def is_same(p, q):
    if p is None and q is None:
        return True
    
    elif p is None or q is None:
        return False
    
    elif p.val != q.val:
        return False
    
    else:
        return is_same(p.left, q.left) and is_same(p.right, q.right)
    
# invert binary tree
 def invert_tree(root):
    if root is None:
        return None
    
    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)

    return root
    

    