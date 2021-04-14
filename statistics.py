def median(list_of_values):
    """
    Calculates median value of a list
    :param list_of_values: list
    :return: median value
    """
    sorted_list = sorted(list_of_values)
    center_index = int(len(list_of_values)/2) # round to int required because division always produces float

    # Median value depends on length on list
    if len(list_of_values) % 2 == 0:
        result = (sorted_list[center_index] + sorted_list[center_index-1])/2
    else:
        # Now we need only 1 index for exact value
        result = sorted_list[center_index]
    return result


def mean(list_of_values):
    """
    Calculates mean value of a list
    :param list_of_values: list
    :return: mean value
    """
    return sum(list_of_values)/len(list_of_values)


def variance(list_of_values):
    """
    Calculates variance value of a list
    :param list_of_values: list
    :return: variance value
    """
    average = mean(list_of_values)
    squared_sum = sum([(x - average)**2 for x in list_of_values])
    return squared_sum/(len(list_of_values)-1)


def covariance(first_list_of_values, second_list_of_values):
    """
    Calculates covariance value of a list
    :param1 first_list_of_values: list
    :param2 second_list_of_values: list
    :return: covariance value
    """
    result = 0
    mean_first_list = mean(first_list_of_values)
    mean_second_list = mean(second_list_of_values)
    for first, second in zip(first_list_of_values, second_list_of_values):
        result += (first-mean_first_list)*(second-mean_second_list)
    result /= (len(second_list_of_values)-1)
    return result


def correlation(first_list_of_values, second_list_of_values):
    """
    Calculates correlation value (between [-1,1]) of a list
    :param1 first_list_of_values: list
    :param2 second_list_of_values: list
    :return: correlation value
    """
    result = 0
    var = (variance(first_list_of_values) ** 0.5) * (variance(second_list_of_values) ** 0.5)
    result = covariance(first_list_of_values, second_list_of_values)/var
    return result
