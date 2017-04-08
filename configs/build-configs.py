#!/usr/bin/env python


import os
import glob
print (os.environ)

destination_dir = "/etc/asterisk/"
source_dir = "/configs/etc/*"

destination_dir = "./dst"
source_dir = "./configs/etc/*"

def read_content(filename):
    with open(filename, "r") as f:
        return f.read()

def write_content(filename, data):
    with open(filename, "w") as f:
            f.write(data)


def replace_patterns(data):
    dict_replacement = {
        "{key1}": os.environ['key1'],
        "{key2}": os.environ['key2']
        "{key3}": os.environ['key3']
    }

    for pattern, replacement in dict_replacement.items():
        data = data.replace(pattern, replacement)

    return data

def main():
    fl = glob.glob(source_dir)
    for filename in fl:
        path_dst = os.path.join(destination_dir, os.path.basename(filename))
        data  = read_content(filename)
        data = replace_patterns(data)
        write_content(path_dst, data)    

        