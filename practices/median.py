import numpy as np
import argparse

def mean(m):
    return np.mean(m)


def find_medium():
    list = list.sort()
    medium = (list[len(list)//2]+list[(len(list)//-2)*-1])/2
    print(medium)
    return medium
find_medium()

def main():
        parser = argparse.ArgumentParser(description="Add two numbers")
        parser.add_argument("number",help="please get someone else to help",narg="+",type=int)
        parser.add_argument("--operation",default="median",choices="median,mean")

main()
