def parse(file):
    current_time = 0
    begin_times = {}
    string_mapping = {}
    data = {}

    with open(file) as fp:
        reader = csv.reader(fp, delimiter=',', quotechar='\\')
        for row in reader:
            type = int(row[0])

            if type == 0 or type == 1:
                current_time = current_time + int(row[2])

            if type == 0:
                # Save the begin time in a temporary dict
                begin_times[int(row[1])] = current_time
            elif type == 1:
                id = int(row[1])
                label = string_mapping[id]
                if label not in data:
                    data[label] = []
                data[label].append((begin_times[id], current_time))
                del begin_times[id]
            elif type == 2:
                # save string mapping for later usage
                string_mapping[int(row[1])] = row[2]
    return data
