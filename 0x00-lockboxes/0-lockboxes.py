  
#!/usr/bin/python3
"""
Module - lockboxes
"""


def canUnlockAll(boxes):
    """
     Function - canUnlockAll
     check if the box is unlocked or not 
     return true if is unlocked or false if not
    """
    stack = [0]
    unlock = [0] * len(boxes)
    unlock[0] = 1

    if len(boxes) == 0:
        return True

    if not isinstance(boxes, list):
        return False

    while stack:
        box = stack.pop()
        for k in boxes[box]:
            if k > 0 and k < len(boxes) and unlock[k] == 0:
                unlock[k] = 1
                stack.append(k)

    return all(unlock)
