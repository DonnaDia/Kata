def cube_checker(volume, side):
    if volume > 0 and side > 0:
        if volume % side == 0: return True
        else: return False
    else: return False