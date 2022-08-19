import argparse
DESCRIPTION = 'Compares two configuration files and shows a difference.'


parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument('first_file', type=str, help='first file')
parser.add_argument('second_file', type=str, help='second file')


def main():
    args = parser.parse_args()
    print(args)
    

if __name__ == '__main__':
    main()
