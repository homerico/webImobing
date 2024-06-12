import sys

from configuration import Configuration

if __name__ == '__main__':
    if len(sys.argv) == 1:
        conf = Configuration("default.json")
    else:
        conf = Configuration(sys.argv[1])
