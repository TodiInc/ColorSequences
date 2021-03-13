import copy
import sys


def main():

    test_files = list(sys.argv)
    test_files.pop(0)
    print_longest_sequence(test_files)


def print_longest_sequence(files):

    for test in files:
        file = open("..\\tests\\{}".format(test), 'r')

        dimensions = file.readline()
        x = int(dimensions.split(' ')[0])
        y = int(dimensions.split(' ')[1])
        whole_file = file.readlines()

        arr = []
        i = 0
        while i < len(whole_file):
            arr.append(list(whole_file[i].replace(" ", "").strip()))
            i += 1

        longest_sequence = find_longest(arr, x, y)

        print(longest_sequence)

        file.close()


def find_longest(arr, x, y):

    r = check_sequences(arr, x, y, 'R')
    g = check_sequences(arr, x, y, 'G')
    b = check_sequences(arr, x, y, 'B')

    longest_sequence = [r, g, b]

    return max(longest_sequence)


def check_sequences(arr, x, y, color):

    i = 0
    j = 0
    result = 0
    false_arr = get_false_arr(arr)

    while i < x:
        while j < y:
            if arr[i][j] == color:
                false_arr[i][j] = 1

            j += 1
        j = 0
        i += 1

    i = 0
    j = 0
    visited_arr = []
    queue = []

    while i < x:
        while j < y:
            if false_arr[i][j] == 1:
                queue.append([i, j])
                current_length = 0

                while len(queue) > 0:

                    curr_x = queue[0][0]
                    curr_y = queue[0][1]
                    current_position = false_arr[curr_x][curr_y]

                    current_length += 1

                    if curr_x - 1 >= 0 and current_position == false_arr[curr_x-1][curr_y] \
                            and not [curr_x-1, curr_y] in visited_arr:
                        if not [curr_x - 1, curr_y] in queue:
                            queue.append([curr_x - 1, curr_y])

                    if curr_x + 1 < x and current_position == false_arr[curr_x+1][curr_y] \
                            and not [curr_x+1, curr_y] in visited_arr:
                        if not [curr_x + 1, curr_y] in queue:
                            queue.append([curr_x + 1, curr_y])

                    if curr_y - 1 >= 0 and current_position == false_arr[curr_x][curr_y-1] \
                            and not [curr_x, curr_y-1] in visited_arr:
                        if not [curr_x, curr_y - 1] in queue:
                            queue.append([curr_x, curr_y - 1])

                    if curr_y + 1 < y and current_position == false_arr[curr_x][curr_y+1] \
                            and not [curr_x, curr_y+1] in visited_arr:
                        if not [curr_x, curr_y + 1] in queue:
                            queue.append([curr_x, curr_y + 1])

                    visited_arr.append(queue[0])
                    queue.pop(0)
                if current_length > result:
                    result = current_length
            j += 1
        j = 0
        i += 1

    return result


def get_false_arr(arr):
    false_arr = copy.deepcopy(arr)
    i = 0
    while i < len(arr):
        j = 0
        while j < len(arr[i]):
            false_arr[i][j] = 0
            j += 1
        i += 1
    return false_arr


main()

