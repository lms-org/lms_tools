import numpy as np

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

class Profiling:
    begin_times = {}
    data = {}

    def feed(self, flag, timestamp, label):
        if flag == 0:
            self.begin_times[label] = timestamp
        elif flag == 1:
            if label in self.begin_times:
                begin = self.begin_times[label]
                delta = timestamp - begin
                if label not in self.data:
                    self.data[label] = []
                self.data[label].append(delta)
            else:
                print("Unknown label: {}".format(label))
        else:
            print("Unknown flag")

    def analyze(self):
        """ Compute mean/std/min/max for every process idependently """
        result = []
        for key in self.data:
            exec_times = self.data[key]
            result.append({
                "label" : key,
                "min" : np.amin(exec_times),
                "max" : np.amax(exec_times),
                "mean" : np.mean(exec_times),
                "std" : np.std(exec_times),
                "count" : len(exec_times)
            })
        return result
