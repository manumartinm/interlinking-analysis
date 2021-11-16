def match_inlinks(list_inliks, domain):
    listwithtuples = []

    for x in list_inliks:
        if x[0] == "Hyperlink" and x[1].count("/") <= x[2].count("/") and domain in x[2]:
            tuple_links = (x[1], x[2])
            listwithtuples.append(tuple_links)
    
    noduplicates = list(dict.fromkeys(listwithtuples))
    return noduplicates


def colors_index(nodes, inlinks_list):
    list_colors = []
    for node in nodes:
        match = False
        for x in inlinks_list:
            if y == x[0]:
                match = True
                if x[4] == "Non-Indexable":
                    list_colors.append("red")
                else:
                    list_colors.append("blue")

        if match == False:
            list_colors.append("yellow")
    
    return list_colors


def size_of_node(degree):
    dictionary_degree = dict(degree)
    sort_dictionary_degree = dict(sorted(dictionary_degree.items(), key=lambda item: item[1], reverse=True))
    counter = 0

    for key, value in sort_dictionary_degree.items():
        if counter < 5:
            sort_dictionary_degree[key] = key
        else:
            sort_dictionary_degree[key] = ""

        counter = counter + 1

    return sort_dictionary_degree
