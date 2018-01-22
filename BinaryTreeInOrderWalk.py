def in_order_walk(root):
    if root == None:
        return
    in_order_walk(root.left)
    print(root.val)
    in_order_walk(root.right)
