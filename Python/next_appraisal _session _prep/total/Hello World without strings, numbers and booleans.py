#Vers 1
from string import whitespace
 
def hi_all():
    ws, *_ = whitespace
    return ws.join(dict(Hello=None, World=None))


#Vers 2
from string import whitespace
 
def Hello():
    pass
 
def World():
    pass
 
def hi_all():
    ws, *_ = whitespace
    return Hello.__name__ + ws + World.__name__