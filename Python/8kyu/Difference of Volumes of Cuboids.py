def find_difference(a, b):
    volume_a = a[0] * a[1] * a[2]
    volume_b = b[0] * b[1] * b[2]
    if volume_a > volume_b:
        result = volume_a - volume_b
    else:
        result = volume_b - volume_a
     
    return result    