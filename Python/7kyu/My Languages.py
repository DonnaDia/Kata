#Vers 1 
def my_languages(results):
    return sorted((l for l,r in results.items() if r>=60), reverse=True, key=results.get)

#Vers2
def my_languages(dict):
    store = []
    for key, value in dict.items():
        if value >= 60:
            store.append(key)
    return sorted(store, key=lambda x: dict[x], reverse=True)

