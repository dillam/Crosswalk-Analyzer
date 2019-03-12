import csv

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def parse_result(result):
# example of result
#'person:': 2, 'car:': 6
    csv_line = []
    x = 0
    for i in range(0, len(result)):
        if result[i] == ':':
            if result[i+1] == '\'':
                continue
            elif result[i+2] in numbers:
                if i + 3 >= len(result):
                    csv_line.append(int(result[i+2]))
                elif result[i+3] in numbers:
                    x = i+3
                    while x < len(result):
                        if result[x] in numbers:
                            x = x + 1
                            if x == len(result):
                                csv_line.append(int(result[i + 2:]))
                        else:
                            if x + 1 >= len(result):
                                csv_line.append(int(result[i + 2:]))
                                break
                            else:
                                csv_line.append(int(result[i + 2:x]))
                                break
                else:
                    csv_line.append(int(result[i+2]))


    if result.count('person') == 0:
        csv_line.insert(0, 0)
    if result.count('car') == 0:
        csv_line.insert(1, 0)
    if result.count('truck') == 0:
        csv_line.insert(2, 0)

    return csv_line

def csv_writer(csv_writer, result, time):
    csv_line = parse_result(result)
    csv_line.insert(0, time)

    writer.writerows(csv_line)
