def gmean(values):
    result = 1

    for i in range(0, len(values)):
        result *= values[i] ** (1 / len(values))

    return result