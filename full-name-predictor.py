# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import sys

titles = set(["PROFESSOR", "COLONEL", "REVEREND", "DOCTOR", "MAJOR"])
female_names = []
male_names = []


def read_csv():
    names = []
    global female_names
    global male_names

    female_fp = './dist.female.first.txt'
    with open(female_fp) as female_file:
        female_names = female_file.readlines()
    female_names = [x.split()[0] for x in female_names]

    male_fp = './dist.male.first.txt'
    with open(male_fp) as male_file:
        male_names = male_file.readlines()
    male_names = [x.split()[0] for x in male_names]

    keyData = []
    with open(sys.argv[1], newline='') as csvfile:
        # with open('./dev-test.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, quotechar='|')
        for row in spamreader:
            test_list = row[0].split(" AND ")
            keyData.append(row[0])
            names.append(func(test_list[0], test_list[1]))

    output_filename = 'full-name-output.csv'
    with open(output_filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for i in range(len(keyData)):
            row = [keyData[i], names[i]]
            csvwriter.writerow(row)


def func(first_name, second_name):
    length = len(first_name.split(' '))
    ans = ""
    if first_name.split(' ')[0] in titles:
        length -= 1
    if length >= 3:
        ans = three(first_name, second_name)
    elif length == 2:
        ans = two(first_name, second_name)
    else:
        ans = one(first_name, second_name)
    return ans


def three(first_name, second_name):
    return first_name


def two(first_name, second_name):
    first_length = len(first_name.split(' '))
    first_last_name = first_name.split(' ')[first_length - 1]  # last name of first person

    if first_last_name not in female_names and first_last_name not in male_names:
        return first_name

    first_first_name = first_name.split(' ')[0]
    if first_first_name not in male_names and first_last_name not in female_names:
        return first_name

    second_length = len(second_name.split(' '))
    if second_name.split(' ')[0] in titles:
        second_length -= 1

    if second_length == 1:
        return first_name
    elif second_length == 2:
        return first_name + " " + second_name.rsplit(' ', 1)[1]
    else:
        return check_middle_name(first_name, second_name)


def one(first_name, second_name):
    second_length = len(second_name.split(' '))
    if second_name.split(' ')[0] in titles:
        second_length -= 1

    if second_length == 1:
        return first_name
    elif second_length == 2:
        return first_name + " " + second_name.rsplit(' ', 1)[1]
    else:
        return check_middle_name(first_name, second_name)


def check_middle_name(first_name, second_name):
    second_length = len(second_name.split(' '))
    check_name = second_name.split(' ')[second_length - 2]

    if check_name not in female_names and check_name not in male_names:
        return first_name + " " + second_name.split(' ')[second_length - 2] + " " + second_name.split(' ')[
            second_length - 1]

    return first_name + " " + second_name.rsplit(' ', 1)[1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please give system arguments.")
    else:
        read_csv()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
