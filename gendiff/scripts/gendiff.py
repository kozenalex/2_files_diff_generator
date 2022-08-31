#!/usr/bin/env python3
import argparse
from gendiff import generate_diff
DESCRIPTION = 'Compares two configuration files and shows a difference.'


parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument('first_file', type=str, help='first file')
parser.add_argument('second_file', type=str, help='second file')
parser.add_argument(
    '-f',
    metavar='FORMAT',
    type=str,
    default='stylish',
    help='set format of output'
)


def main():
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
