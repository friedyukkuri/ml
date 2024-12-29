import sys
from lib import *

def main():

    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: python3 main.py options string filename")
        return

    string = ""
    filename = ""
    ignore_case = False

    if sys.argv[1] != "-i" and len(sys.argv) == 4:
        print("Usage: python3 main.py options string filename")
        return

    if sys.argv[1] == "-i":
        string = sys.argv[2].lower()
        filename = sys.argv[3]
        ignore_case = True
    else:
        string = sys.argv[1]
        filename = sys.argv[2]

    try:
        with open(filename, "r") as f:
            lines = f.readlines()

            results = []
            if ignore_case:
                results = FindStringInFileIgnoreCase(lines, string)
            else:
                results = FindStringInFile(lines, string)

            for line in results:
                print(line, end="")

    except:
        print("Some error occurred while reading the file")
        return

if __name__ == "__main__":
    main()
