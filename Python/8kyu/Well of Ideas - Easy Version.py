def well(x):
    amount = x.count('good')
    return 'Publish!' if amount >0 and amount <= 2  else 'I smell a series!' if  amount > 2 else 'Fail!'