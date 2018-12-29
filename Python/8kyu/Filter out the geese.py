geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    result = []

    for goose in birds:
        if goose not in geese:
            result.append(goose)
            
    return result    