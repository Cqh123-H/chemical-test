import re


def read_txt(filename):
    with open(filename, encoding='utf-8') as f:
        with open('new_02.txt', 'w', encoding='utf-8') as n:
            lines = f.readlines()
            new_l = []
            for line in lines:
                l = line.rstrip('\n')
                if '=' not in l:
                    l = ""
                if '=====' in l:
                    l = ""
                text = re.sub('[（]', '(', l)
                text = re.sub('[）]', ')', text)
                # text = re.sub('[\(1)]','', text)
                if text == '\n':
                    text = text.strip('\n')
                    n.write('{}\n'.format(text))
                    print(text)
                else:
                    n.write('{}\n'.format(text))
    f.close()
    # return new_l


if __name__ == '__main__':
    read_txt('./new_01.txt')
