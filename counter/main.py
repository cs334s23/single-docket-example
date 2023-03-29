
import os
import json


DOCKET_NAME = 'USCIS-2006-0044'


def add_word(words, word):
    if word in words:
        words[word] += 1
    else:
        words[word] = 1


def add_count_extracted_text(words, filename):
    with open(filename, 'r') as infile:
        s = infile.read()
        s = s.lower().split()
        for word in s:
            add_word(words, word)


def add_count_comment_json(words, filename):
    with open(filename, 'r') as infile:
        s = infile.read()
        s = json.loads(s)
        s = s['data']['attributes']['comment']
        if s is None:
            return
        s = s.lower().split()
        for word in s:
            add_word(words, word)


def main():
    words = {}

    for root, dirs, files in os.walk(f'./{DOCKET_NAME}/text-{DOCKET_NAME}/comments_extracted_text'):
        for name in files:
            if name[-4:] == '.txt':
                filename = os.path.join(root, name)
                add_count_extracted_text(words, filename)

    for root, dirs, files in os.walk("./{DOCKET_NAME}/text-{DOCKET_NAME}/comments"):
        for name in files:
            if name[-4:] == '.json':
                filename = os.path.join(root, name)
                add_count_comment_json(words, filename)

    keys = sorted(words.keys(), key=lambda x: words[x])
    keys = map(lambda x: (x, words[x]), keys)
    keys = list(keys)

    print(str(sum(map(lambda x: x[1], keys))) + ' total words in all comments.')

    with open('./results.txt', 'w') as out:
        out.write('word, count\n')

        for word, count in keys:
            out.write(word)
            out.write(', ')
            out.write(str(count))
            out.write('\n')


if __name__ == '__main__':
    main()
