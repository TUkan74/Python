#!/usr/bin/env python3

import os

def find_file_name():
    file_name = ['README.md','readme.md','README','readme']
    for file in file_name:
        if os.path.exists(file):
            with open(file) as f:
                for line in f:
                    line = line.strip()
                    if line.lstrip('# ')!= '':
                        return line.lstrip('# ')
    
    return os.path.basename(os.getcwd())

def main():
    print(find_file_name())

if __name__ == '__main__':
    main()
