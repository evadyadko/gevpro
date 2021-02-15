import argparse
import json


def solve(puzzlefile, wordsfile):
    puzzle_str = ""
    puzzle_lst = []
    for row in puzzlefile:
        puzzle_lst.append(row.rstrip() + " ")
        puzzle_str += row.rstrip() + " "
    for i in range(len(puzzle_lst)+1):
        puzzle_str += " "
        for item in puzzle_lst:
            puzzle_str += item[i]
    words_set = {word.upper() for word in wordsfile["words"]}
    return {word for word in words_set if word in puzzle_str}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("puzzlefile", type=argparse.FileType('r'),
                        help="Enter your puzzle file")
    parser.add_argument("wordsfile", type=argparse.FileType('r'),
                        help="Enter your words file")
    args = parser.parse_args()
    wordsfile = 'words.json'
    with open(wordsfile) as inp:
        data = json.load(inp)
    print(solve(args.puzzlefile, data))
    args.puzzlefile.close(), args.wordsfile.close()


if __name__ == "__main__":
    main()
