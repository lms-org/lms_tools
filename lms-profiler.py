#!/usr/bin/env python3
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from lms import profiling

def analyze_process(data):
    """ Compute mean/std/min/max for every process idependently """
    result = []
    for key in data:
        exec_times = [iv[1] - iv[0] for iv in data[key]]
        result.append({
            "label" : key,
            "min" : np.amin(exec_times),
            "max" : np.amax(exec_times),
            "mean" : np.mean(exec_times),
            "std" : np.std(exec_times),
            "count" : len(exec_times)
        })
    return result

def profiling_summary(data):
    sorted_data = sorted(data, key=lambda x: x["label"])
    key_len = max(map(lambda x: len(x["label"]), data))

    for record in sorted_data:
        print("{0} \u00f8 {1:>9,.0f} \u00b1 {2:<7,.0f} [{3}, {4}] ({5})"
            .format(record["label"].ljust(key_len), record["mean"],
            record["std"], record["min"], record["max"], record["count"]))

def filter_modules(data):
    return [x for x in data if "." in x["label"]]

def display_process(data):
    data = sorted(data, key=lambda x: x["mean"])

    y_pos = np.arange(len(data))
    y_label = [x["label"] for x in data]
    x = [x["mean"] for x in data]
    error = [x["std"] for x in data]

    plt.barh(y_pos, x, xerr=error, align='center', alpha=0.4)
    plt.yticks(y_pos, y_label)
    plt.xlabel("Execution time (us)")
    plt.title('Profiling Data Analysis')

    plt.show()

def display_timeline(data, key):
    y = np.array([x[1] - x[0] for x in data[key]])
    x = np.arange(len(y))

    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: lms-profiler.py <path>")
        sys.exit(1)
    else:
        data = profiling.parse(sys.argv[1])
        process_data = analyze_process(data)
        profiling_summary(process_data)
        display_process(filter_modules(process_data))
        #display_timeline(data, "render.importer_1")
