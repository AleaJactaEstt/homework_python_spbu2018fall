def hadamar_list_product(lista, listb):
    return [a*b for a,b in zip(lista,listb)]

def school_info(data):
    num_of_grades = {str(i):0 for i in range(1,6)}
    data_values = list(data.values())
    for i in range(1,6):
        for j in range(len(data)):
            num_of_grades[str(i)] += data_values[j][str(i)]
    
    means = list(map(lambda x: sum(hadamar_list_product(list(x.values()), [i for i in range(1,6)])), data_values))
    divider = list(map(lambda x: 1/sum(list(x.values())), data_values))
    
    return (num_of_grades,hadamar_list_product(means,divider))