def enough(cap, on, wait):
    return 0 if cap == (on + wait) else (on + wait) - cap if ((on + wait) - cap) > 0 else 0