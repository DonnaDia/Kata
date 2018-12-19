#Vers 2
def bald(s):
    listed = []
    result = []

    unslashed = s.replace('/', '-')

    listed == listed.append(unslashed)

    result.append('Unicorn!') if s.count('/') == 1 else result.append('Homer!') if s.count('/') == 2 \
    else result.append('Careless!') if s.count('/') >= 3 and s.count('/') <= 5 else result.append('Hobo!') \
    if s.count('/') > 5 else result.append('Clean!')

    listed = listed + result


    return listed



#Vers 1
def bald(s):
    listed = []
    result = []

    unslashed = s.replace('/', '-')

    listed == listed.append(unslashed)

    if s.count('/') == 1:
        result.append('Unicorn!')
    elif s.count('/') == 2:
        result.append('Homer!')
    elif s.count('/') >= 3 and s.count('/') <= 5:
        result.append('Careless!')
    elif s.count('/') > 5:
        result.append('Hobo!')
    else:
        result.append('Clean!')

    listed = listed + result


    return listed