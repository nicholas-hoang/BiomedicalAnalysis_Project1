import json
import os

# Import Necessary Modules
import pandas as pd
import numpy as np

import util_5353

# Problem 0-A [0 points]
# Load the data into whatever data structure you see fit.  You can leave it in
# the csv format, use a custom data structure, or (best idea) use a pandas
# frame.  I would suggest any basic data modifications (certainly any
# file-specific modifications) be handled here. Hint: there are lots of
# extraneous spaces in the data that you're going to want to remove
load_data_count = 0


def load_data(filename):
    global load_data_count
    load_data_count += 1
    if load_data_count >= 5:
        print('WARNING: load_data called too many times')
    data = None
    # Begin CODE
    with open(filename,'r') as data:
        data = pd.read_csv(filename)
        data = data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        data = data[data[' CONAME '].str.contains('County').fillna(False)]
    # End CODE
    return data



# Problem 0-B [0 points]
# Return the name of the county at the given (zero-based) index in the dataset.
# Note: this should be done entirely with code. Hard-coding values, e.g.,
# "return 'Austin County'" is not a smart move at all...

def county_at_index(data, index):
    county_name = None
    # Begin CODE
    county_name = data.iloc[index][1]
    # End CODE
    return county_name

# Problem 0-C [0 points]
# Return the number of counties in the dataset.


def num_counties(data):
    num = None
    # Begin CODE
    num = len(pd.unique(data[' CONAME ']))
    # End CODE
    return num

# Problem 1 [10 points]


def county_pop(data, county):
    pop = None
    # Begin CODE
    pop = data[data[' CONAME '] == county]
    print(pop['TOTPOP'])
    # End CODE
    return pop

# Problem 2 [10 points]


def highest_ethnic_counties(data):
    highest = {}
    # Begin CODE

    # End CODE
    return highest

# Problem 3 [10 points]


def highest_sex_counties(data):
    highest = None
    # Begin CODE

    # End CODE
    return highest

# Problem 4 [5 points]


def low_high_heartdisease_counties(data):
    lowhigh = None
    # Begin CODE

    # End CODE
    return lowhigh

# Problem 5 [5 points]


def low_high_lungcancer_counties(data):
    lowhigh = None
    # Begin CODE

    # End CODE
    return lowhigh

# Problem 6 [5 points]


def low_high_motorinjury_counties(data):
    lowhigh = None
    # Begin CODE

    # End CODE
    return lowhigh

# Problem 7 [5 points]


def low_high_suicide_counties(data):
    lowhigh = None
    # Begin CODE

    # End CODE
    return lowhigh

# Problem 8 [10 points]


def most_relative_foodstamp_county(data):
    county_name = None
    # Begin CODE

    # End CODE
    return county_name

# Problem 9 [10 points]


def biggest_pertussis_jump(data_list):
    county_name = None
    # Begin CODE

    # End CODE
    return county_name

# Problem 10 [10 points]


def mean_lowbirth_noinsurance(data):
    rates = {}
    # Begin CODE

    # End CODE
    return rates

# Problem 11 [10 points]
# Note: I'd recommend lxml.etree over xml.etree.ElementTree, it has all the
# same functionality plus more, including write(file, pretty_print=True)


def employment_xml(data, filename):
    # Begin CODE

    # End CODE
    return

# Problem 12 [10 points]
# Note: for nice printing, the json library has sort_keys and indent parameters
# in the dump method.


def infectious_json(data_list, filename):
    # Begin CODE

    # End CODE
    return


# Note: don't mess with this code block!  Your code will be tested by an outside
# program that will not call this __main__ block.  So if you mess with the
# following block of code you might crash the autograder.  You're definitely
# encouraged to look at this code, however, especially if your code crashes.
if __name__ == '__main__':
    print('::: Problem 0-A :::')
    data = {}
    for year in range(2006, 2010):
        data[year] = load_data(
            'Data File for Texas Health Facts %d.csv' % year)
        util_5353.assert_not_none(data[year], '0-A')

    print('::: Problem 0-B :::')
    zeroB_ret = county_at_index(data[2006], 0)
    util_5353.assert_str(zeroB_ret, '0-B')
    util_5353.assert_str_eq('Anderson County', zeroB_ret, '0-B')

    print('::: Problem 0-C :::')
    zeroC_ret = num_counties(data[2006])
    util_5353.assert_int(zeroC_ret, '0-C')
    util_5353.assert_int_eq(254, zeroC_ret, '0-C')

    print('::: Problem 1 :::')
    one_ret = county_pop(data[2006], 'Bowie County')
    util_5353.assert_int(one_ret, '1')
    util_5353.assert_int_range((0, 10000000), one_ret, '1')
    print(':::   Bowie County Popultion: ' + str(one_ret))

    # print('::: Problem 2 :::')
    # two_ret = highest_ethnic_counties(data[2006])
    # util_5353.assert_dict(two_ret, '2')
    # util_5353.assert_int_eq(4, len(two_ret.keys()), '2')
    # util_5353.assert_str(two_ret['Anglos'], '2')
    # util_5353.assert_str(two_ret['Blacks'], '2')
    # util_5353.assert_str(two_ret['Hispanics'], '2')
    # util_5353.assert_str(two_ret['Other'], '2')
    # print(':::   2006 Highest County for \'Anglos\':    ' +
    #       str(two_ret['Anglos']))
    # print(':::   2006 Highest County for \'Blacks\':    ' +
    #       str(two_ret['Blacks']))
    # print(':::   2006 Highest County for \'Hispanics\': ' +
    #       str(two_ret['Hispanics']))
    # print(':::   2006 Highest County for \'Other\':     ' +
    #       str(two_ret['Other']))

    # print('::: Problem 3 :::')
    # three_ret = highest_sex_counties(data[2006])
    # util_5353.assert_tuple(three_ret, 2, '3')
    # util_5353.assert_str(three_ret[0], '3')
    # util_5353.assert_str(three_ret[1], '3')
    # print(':::   2006 Highest County for \'Female\': ' + str(three_ret[0]))
    # print(':::   2006 Highest County for \'Male\':   ' + str(three_ret[1]))

    # print('::: Problem 4 :::')
    # four_ret = low_high_heartdisease_counties(data[2006])
    # util_5353.assert_tuple(four_ret, 2, '4')
    # util_5353.assert_str(four_ret[0], '4')
    # util_5353.assert_str(four_ret[1], '4')
    # util_5353.assert_str_neq(four_ret[1], 'Zapata County', '4')
    # print(':::   2006 Highest County for Heart Disease: ' + four_ret[0])
    # print(':::   2006  Lowest County for Heart Disease: ' + four_ret[1])

    # print('::: Problem 5 :::')
    # five_ret = low_high_lungcancer_counties(data[2006])
    # util_5353.assert_tuple(five_ret, 2, '5')
    # util_5353.assert_str(five_ret[0], '5')
    # util_5353.assert_str(five_ret[1], '5')
    # print(':::   2006 Highest County for Lung Cancer: ' + five_ret[0])
    # print(':::   2006  Lowest County for Lung Cancer: ' + five_ret[1])

    # print('::: Problem 6 :::')
    # six_ret = low_high_motorinjury_counties(data[2006])
    # util_5353.assert_tuple(six_ret, 10, '6')
    # for i in range(10):
    #     util_5353.assert_str(six_ret[i], '6')
    # util_5353.assert_str_neq(six_ret[0], 'Denton County', '6')
    # print(':::   2006 Highest Counties for Motor Injury:')
    # for i in range(5):
    #     print(':::    ' + str(i+1) + '. ' + six_ret[i])
    # print(':::   2006 Lowest Counties for Motor Injury:')
    # for i in range(4):
    #     ir = 5 + i
    #     print(':::    N-' + str(5-i-1) + '. ' + six_ret[ir])
    # print(':::    N.   ' + six_ret[-1])

    # print('::: Problem 7 :::')
    # seven_ret = low_high_suicide_counties(data[2006])
    # util_5353.assert_tuple(seven_ret, 10, '7')
    # for i in range(10):
    #     util_5353.assert_str(seven_ret[i], '7')
    # print(':::   2006 Highest Counties for Suicide:')
    # for i in range(5):
    #     print(':::    ' + str(i+1) + '. ' + seven_ret[i])
    # print(':::   2006 Lowest Counties for Suicide:')
    # for i in range(4):
    #     ir = 5 + i
    #     print(':::    N-' + str(5-i-1) + '. ' + seven_ret[ir])
    # print(':::    N.   ' + seven_ret[-1])

    # print('::: Problem 8 :::')
    # eight_ret = most_relative_foodstamp_county(data[2006])
    # util_5353.assert_str(eight_ret, '8')
    # util_5353.assert_str_neq(eight_ret, 'Loving County', '8')
    # print(':::   2006 County with Highest Food Stamp Utilization: ' + eight_ret)

    # print('::: Problem 9 :::')
    # data_list = [data[2006], data[2007]]  # , data[2008], data[2009]]
    # nine_ret = biggest_pertussis_jump(data_list)
    # util_5353.assert_str(nine_ret, '9')
    # print(':::   County with Biggest Jump in Pertussis from 2006->2007: ' + nine_ret)

    # print('::: Problem 10 :::')
    # ten_ret = mean_lowbirth_noinsurance(data[2006])
    # util_5353.assert_dict(ten_ret, '10')
    # for key in ten_ret.keys():
    #     util_5353.assert_str(key, '10',
    #                          valid_values=['10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%'])
    #     util_5353.assert_str_eq('%', key[-1], '10')
    #     util_5353.assert_float_range([0.0, 1.0], ten_ret[key], '10')
    # print(':::   2006 Relation between Insurance and Low Birth Weight Rate:')
    # print(':::   Insurance_Rate    Low_Birth_Rate')
    # for rate in sorted(ten_ret.keys()):
    #     print(':::     ' + rate + '               ' + str(ten_ret[rate]))

    # print('::: Problem 11 :::')
    # eleven_filename = 'prob11.xml'
    # if os.path.exists(eleven_filename):
    #     os.remove(eleven_filename)
    # employment_xml(data[2006], eleven_filename)
    # util_5353.assert_file(eleven_filename, '11')
    # print('::: First 10 lines of file for 2006:')
    # with open(eleven_filename, 'r') as reader:
    #     lines = [line for line in reader.readlines()]
    #     for line in lines[:10]:
    #         print(':::   ' + line.replace('\n', ''))

    # print('::: Problem 12 :::')
    # twelve_filename = 'prob12.json'
    # if os.path.exists(twelve_filename):
    #     os.remove(twelve_filename)
    # infectious_json(data_list, twelve_filename)
    # util_5353.assert_file(twelve_filename, '12')
    # with open(twelve_filename, 'r') as f:
    #     twelve_ret = json.load(f)
    #     util_5353.assert_int_eq(7, len(twelve_ret.keys()), '12')
    #     for key in twelve_ret.keys():
    #         util_5353.assert_str(key, '12',
    #                              valid_values=['aids', 'chlamydia', 'gonorrhea', 'pertussis', 'syphilis', 'tuberculosis', 'varicella'])
    # print('::: First 10 lines of file for 2006 and 2007:')
    # with open(twelve_filename, 'r') as reader:
    #     lines = [line for line in reader.readlines()]
    #     for line in lines[:10]:
    #         print(':::   ' + line.replace('\n', ''))

    # print('~~~ All Tests Pass ~~~')
