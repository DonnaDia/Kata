def distinct(seq):
    from collections import OrderedDict
    return list(OrderedDict.fromkeys(seq))