#Vers 1
from collections import Counter

def ordered_count(input):
    return list(Counter(input).items())


#Vers 2
from collections import OrderedDict, Counter


class OrderedCounter(Counter, OrderedDict):
    pass


def ordered_count(seq):
    return list(OrderedCounter(seq).items())