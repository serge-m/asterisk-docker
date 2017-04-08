#!/usr/bin/env python


import os
import glob
print (os.environ)

source_dir = "./etc/*"
destination_dir = "/etc/asterisk/"

source_dir = "./etc/*"
destination_dir = "./dst/"

def read_content(filename):
    with open(filename, "r") as f:
        return f.read()

def write_content(filename, data):
    with open(filename, "w") as f:
            f.write(data)


def replace_patterns(data):
    list_keys = ['key1', 'key2', 'key3']

    for key in list_keys:
        if os.environ.get(key):
            data = data.replace("{" + key + "}", os.environ.get(key))

    return data

def main():
    fl = glob.glob(source_dir)
    print(fl)
    for filename in fl:
        path_dst = os.path.join(destination_dir, os.path.basename(filename))
        print(path_dst)
        data  = read_content(filename)
        data = replace_patterns(data)
        write_content(path_dst, data)    

        

if __name__ == '__main__':
    main()