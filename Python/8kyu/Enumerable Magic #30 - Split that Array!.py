#Works-on-my-machine version
def partition(list, classifier_method):
    predefined = list[:classifier_method]
    other = list[classifier_method:]
    result = []

    for element in predefined, other:
        result.append(element)

    print(result)

partition(["cat", "dog", "duck", "cow", "donkey"], 3)

#Vers2
def partition(list, classifier_method):
    predefined = []
    other = []
    for l in list:
        if classifier_method(l):
            predefined.append(l)
        else:
            other.append(l)
    return predefined, other