"""Generates random set of colours and classifies them using K-nearest neighbours"""
import csv
from random import randint
from collections import Counter

dataset_filename = "colours.csv"



def load_colours(filename):
"""Ingests csv of training data and yields each line"""
    with open(filename) as dataset_file:
        lines = csv.reader(dataset_file)
        for line in lines:
            label, hex_colour = line
            yield (hex_to_rgb(hex_colour), label)

def hex_to_rgb(hex_colour):
"""Helper to convert hex colour value to rgb tuple"""
    return tuple(int(hex_colour[i : i + 2], 16) for i in range(1, 6, 2))

def generate_colours(count=100):
"""Generate random number of rgb colour tuples"""
    for i in range(count):
        yield(randint(0, 255), randint(0, 255), randint(0, 255))

def colour_distance(colour1, colour2):
"""Calculate euclidean distance between two multi-dimensional points"""
    channels = zip(colour1, colour2)
    sum_distance_squared = 0
    for c1, c2 in channels:
        sum_distance_squared += (c1 - c2) ** 2
    return sum_distance_squared

def nearest_neighbours(model_colours, target_colours, num_neighbours=5):
"""Return colour name of k closest matches (from training set) to 
each target colour"""
    model_colours = list(model_colours)

    for target in target_colours:
        distances = sorted(
            ((colour_distance(c[0], target), c) for c in model_colours)
        )
        yield target, distances[:5]

def name_colours(model_colours, target_colours, num_neighbours=5):
"""Guess colour name based on most common name amongst the k nearest
neighbours"""
    for target, near in nearest_neighbours(
        model_colours, target_colours, num_neighbours=5
    ):
        print(target, near)
        name_guess = Counter(n[1] for n in near).most_common()[0][0]
        yield target, name_guess

def write_results(colours, filename="output.csv"):
"""Write results to csv file"""
    with open(filename, "w") as file:
        writer = csv.writer(file)
        for (r, g, b), name in colours:
            writer.writerow([name, f"#{r:02x}{g:02x}{b:02x}"])

def process_colours(dataset_filename="colours.csv"):
"""Manager function"""
    model_colours = load_colours(dataset_filename)
    colours = name_colours(model_colours, generate_colours(), 5)
    write_results(colours)

if __name__ == "__main__":
    process_colours()