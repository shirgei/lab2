from statistics import mean, median, variance, correlation
import csv

# Consts
EMPTY = 0
MINIMUM_VALUE = 0
MAXIMUM_VALUE = 1
FIRST_LOCATION = 0
SECOND_LOCATION = 1


def load_data(path):
    """
    Loads data from given csv
    :param path: path to csv file
    :return: returns data as dict {name_of_feature: list_of_values}
    """
    with open(path, 'r') as f:
        reader = csv.reader(f)
        read_header = None
        data = {}
        index_to_column_name = {}
        for row in reader:
            if not read_header:
                # we are at first row with names of columns
                for i, column_name in enumerate(row):  # enumerate generates index together with value
                    data[column_name] = []  # initializing as empty list
                    index_to_column_name[i] = column_name
                read_header = True
            else:
                # need to append values to data lists. We don't know column name, only index.
                for i, value in enumerate(row):
                    current_column_name = index_to_column_name[i]  # reproducing column name
                    data[current_column_name].append(float(value))
    return data


def run_analysis():
    """
    Runs analysis on dataset and finds strongest and weakest pair of values
    :param : None
    :return: None
    """
    file_path = './winequality.csv'
    data = load_data(file_path)

    # first way of printing. Everything casted to string, and spaces put automatically between passed values.
    print('Number of features:', len(data))
    for feature_name, list_of_values in sorted(data.items()):
        # second way of printing. We print single string after format function.
        # Format function fills {} with values passed as arguments. It has nice applications for better printing,
        # like limiting number of digits for floats or other formatting tools.
        print('"{}". Mean: {:3.2f}, Median: {:.2f}, Std: {:.4f}'.format(
            feature_name, mean(list_of_values), median(list_of_values), variance(list_of_values)**0.5))

    # Resets lists and arguments
    temp_strongest_pair = [EMPTY, EMPTY]
    temp_weakest_pair = [EMPTY, EMPTY]
    high_correlation = MINIMUM_VALUE
    low_correlation = MAXIMUM_VALUE

    for first_feature_name, first_list_of_values in data.items():
        for second_feature_name, second_list_of_values in data.items():
            if first_feature_name == second_feature_name:
                continue
            temp_correlation = correlation(first_list_of_values, second_list_of_values)

            # Checks strongest pair
            if abs(temp_correlation) > high_correlation:
                high_correlation = temp_correlation
                temp_strongest_pair[FIRST_LOCATION] = first_feature_name
                temp_strongest_pair[SECOND_LOCATION] = second_feature_name

            # Checks weakest pair
            if abs(temp_correlation) <= abs(low_correlation):
                low_correlation = temp_correlation
                temp_weakest_pair[FIRST_LOCATION] = first_feature_name
                temp_weakest_pair[SECOND_LOCATION] = second_feature_name
    temp_strongest_pair.sort()
    temp_weakest_pair.sort()
    strongest_pair = temp_strongest_pair
    weakest_pair = temp_weakest_pair

    print('The strongest linear relationship is between: "{}","{}". '
          'The value is: {:.4f}'.format(strongest_pair[0], strongest_pair[1], high_correlation))

    print('The weakest linear relationship is between: "{}","{}". '
          'The value is: {:.4f}'.format(*weakest_pair, low_correlation))  # * converts list to arguments.
    # Line 53 is equivalent to line 48, this is just other way to use list as arguments


if __name__ == '__main__':
    run_analysis()
