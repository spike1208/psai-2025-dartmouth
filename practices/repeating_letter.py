import argparse

def two_characters(s):
    check = []
    length = {}
    letters = set(list(s))
    charecters = list(s)
    for a in letters:
        temp = letters.copy()
        temp.pop(a)
        for b in letters:
            temp.pop(b)
            new = charecters.copy()
            for i in temp:
                new.pop(i)
            c = len(new)//2
            for i in range (c):
                pattern = s[:i]
                if len(s) % i == 0 and pattern * (len(s) // i) == s:
                    check.append(pattern)
            for i in check:
                length[i] = len(i)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('s', type=str, help='the string to process')
    args = parser.parse_args()
    print(two_characters(args.s))
