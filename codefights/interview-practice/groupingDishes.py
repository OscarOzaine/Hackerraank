def groupingDishes(dishes):
    dictionary = {}
    for d in dishes:
        for i in d[1:]:
            if i not in dictionary:
                dictionary[i] = [d[0]]
            else:
                dictionary[i].append(d[0])
                
    result = []
    for d in sorted(dictionary):
        if len(dictionary[d]) > 1:
            result.append([d] + sorted(dictionary[d]))
            
    return result

