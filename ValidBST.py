def isValidBST(root):
        
    def Valid(root, minValue, maxValue):
        
        if root is None:
            return True
        
        if root.val <= minValue or root.val >= maxValue:
            return False
        
        return Valid(root.left, minValue, root.val) and Valid(root.right, root.val, maxValue)
    
    return Valid(root, float("-inf"), float("inf"))