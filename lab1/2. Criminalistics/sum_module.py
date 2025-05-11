def calc_sum_column(data):
    return [sum(col) for col in zip(*data)]

def calc_sum_row(data):
    return [sum(row) for row in data]