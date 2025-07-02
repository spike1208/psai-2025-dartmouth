import argparse

def draw(N):
    for i in range (N[0]): 
        print(" "*((N[0]-1)-i)+(i+1)*"#")

def main():
        parser = argparse.ArgumentParser(description="some descrition")
        parser.add_argument('n',help="please get someone else to help",nargs="+",type=int)
        args = parser.parse_args()
        draw(args.n)
main()

#uv run practices/hashtag_staircase.py 20