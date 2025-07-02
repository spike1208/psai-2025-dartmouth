import argparse

def two_characters(s):
    letters = set(list(s))
    print(letters)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('s', type=str, help='the string to process')
    args = parser.parse_args()
    print(two_characters(args.s))