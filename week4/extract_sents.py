#!/usr/bin/python3
# program name: extract_sents.py
# Eva Dyadko, 28-02-2021
# This program prints tokenized sentences from a textfile.
import sys
import re
import gzip


def tokenizer(file):
    """This function takes a textfile as input,
    and returns tokenized sentences."""
    textstr = ""
    with gzip.open(file, 'rt', encoding='utf8') as text:
        for line in text:
            textstr += line
            trim_spaces = re.sub(r'\n\n', '\n', textstr)
            multilines = re.sub(r'\. ', '.\n', trim_spaces)
            onelines = re.sub('\n(?=[a-z])', r'', multilines)
            splitted_sentences = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])',
                                          onelines)
        for sentence in splitted_sentences:
            s = re.sub('(?<=[^ ])(?=[.,:;!?()"\'])|(?<=[.,!?:;()"\'])'
                       '(?=[^ ])', r' ', sentence)
        return s[90:-55]


def main():
    file = str(sys.argv[1])
    print(tokenizer(file))


if __name__ == "__main__":
    main()
