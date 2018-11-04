def count_gender(school):
    values = list(zip(*list(school.values())))
    return (sum(values[0]),sum(values[1]))