import argparse
import logging

logging.basicConfig(
    level=logging.DEBUG,  # Set minimum log level to DEBUG
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
    datefmt='%Y-%m-%d %H:%M:%S',  # Date/time format
    filename='app.log',  # Log to this file; remove to log to console
    filemode='w'  # Overwrite the log file each run; use 'a' to append
)
# from chatty

logger = logging.getLogger(__name__)

def seperate_word(sentence):
        sentence = set(sentence)
        print(sentence)

def main():
        parser = argparse.ArgumentParser(description="some descrition")
        parser.add_argument('sentence',help="please get someone else to help",nargs="+",type=str)
        args = parser.parse_args()
        logger.info("User typed in this sentence:{sentence}")
        seperate_word(args.sentence)
main()


